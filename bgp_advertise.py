import eventlet

# BGPSpeaker needs sockets patched
eventlet.monkey_patch()

# initialize a log handler
# this is not strictly necessary but useful if you get messages like:
#    No handlers could be found for logger "ryu.lib.hub"
import logging
import sys
import commands
import re
import datetime
import json
import time

db_from_bgp = {}
IP_PRIVATE = "169.254"
FORMAT = "%(asctime)s %(process)s %(message)s"

ovn_db_ips = ["192.168.0.22","192.168.0.23","192.168.0.24"]
ovn = 'ovn-nbctl --db tcp:'
port = ':6641'

logging.basicConfig(level=logging.INFO, format=FORMAT, filename='/root/ryu/bgp_advertise.log')
log = logging.getLogger()

log.addHandler(logging.StreamHandler(sys.stderr))

from ryu.services.protocols.bgp.bgpspeaker import BGPSpeaker


# obtain the env log_bgp_info ,if not ,declare -x log_bgp_info
# for logging info if log_bgp_info is 1 ,set info to log to /home/ryu/bgp_advertise.log
# if cancle info to /home/ryu/bgp_advertise.log ,unset log_bgp_info


def dump_remote_best_path_change(event):
    print
    'the best path changed:', event.remote_as, event.prefix, \
    event.nexthop, event.is_withdraw


def detect_peer_down(remote_ip, remote_as):
    print
    'Peer down:', remote_ip, remote_as


def _valid_str(lst,str_list):
    '''
    :param lst: list from db
    :param str_list: check the str in lis or not
    :return:
    '''
    for ip in lst:
        if ip.startswith(str_list):
            return ip
    else:
        return None

# def _get_db_ips():
#
#     '''
#       nee to test vondb ip is alive , ping will take long time with seconds?
#     '''
#     ovn_db_ips = []
#     ovn_db_ips.append(IP1)
#     ovn_db_ips.append(IP2)
#     ovn_db_ips.append(IP3)
#     return ovn_db_ips


def _get_router_info():
    for ip in ovn_db_ips:
        router = commands.getoutput(ovn + ip+ port + " show" + '| grep "^router"' + '| awk \'{if ($NF ~ "vgw.*") print $2,$NF}\'')
        if router.startswith('ovn-nbctl'):
            continue
        else:
            return router, ip
    else:
        raise Exception("can't get db info")


def _get_ip_gateway_info(router_id, db_ip):

    '''

    :param router_id: str
    :param db_ip: str
    :return:
    '''
    """
     need to check the cluster change the master ip
    """
    flag = False
    static_router = commands.getoutput(
        ovn + db_ip + port + " lr-route-list " + router_id + "| awk '{if($1 !~ \"IPv.*\") print}'")
    gateway_ip = commands.getoutput(
        ovn + db_ip + port + " show " + router_id + ' |awk "/network/{print}"' + " |awk '!/.*169.*/{print}'")

    """
       if at this time , cluster changed ,need set flag true,
    """
    if static_router.startwith('ovn-nbctl') or gateway_ip.startwith('ovn-nbctl'):
        flag = True
    return static_router, gateway_ip, flag


def get_gateway_ip():
    info_from_db = {}
    '''
       if cluster already down, don't withdraw route
    '''
    try:
        router, db_ip = _get_router_info()
    except:
        #raise Exception("can't get db info ,cluster is down??")
        logging.critical("cluster down ???")
        return info_from_db,False

    router_id = router.split('\n')
    for i in router_id:
        routeinfo = i.split(" ")
        logging.info('Route id is {} name is {}'.format(routeinfo[0], routeinfo[1]))

        static_router, gateway_ip,flag = _get_ip_gateway_info(routeinfo[0], db_ip)
        '''
        if flag is true meaning that when get route and gateway,cluster changed ,info is wrong,
        nee to return dircetly
        '''
        if flag:
            logging.warning("cluster warning,will not do anything!! ")
            return info_from_db,flag
        if not gateway_ip:
            continue
        gateway = re.findall("\"(.*)/.*\"", gateway_ip) # if gateway is null ?????
        if gateway is None:
            continue
        if not static_router:
            continue
        static_route_lst = static_router.splitlines()
        for ip in static_route_lst:
            tmp = {}
            iplst = ip.strip().rsplit()
            if _valid_str(iplst,'dst-ip'):
                iplst.remove('dst-ip')
            ip_network = _valid_str(iplst,IP_PRIVATE)
            if ip_network is None:
                continue
            iplst.remove(ip_network)
            logging.info('Statis route  is {}'.format(iplst))
            iplst = set(iplst)
            if gateway[0] in info_from_db:
                info_from_db[gateway[0]] |= iplst
            else:
                tmp = {gateway[0]: iplst}
                info_from_db.update(tmp)
    return info_from_db


def compare_db():
    db_from_ovs = {}
    db_from_ovs,flag = get_gateway_ip()
    if flag:
        logging.warning("cluster changed or down, will not do compare db!! ")
        return
    logging.info("*******************begin compare db *********************")
    logging.info('time is {}'.format(datetime.datetime.now()))
    if db_from_ovs:
        if not db_from_bgp:
            logging.info('this is first advertise route to bgp')
            for gateway, ips_from_ovs in db_from_ovs.items():
                for ip in ips_from_ovs:
                    speaker.prefix_add(ip, next_hop=gateway)
                    logging.info("{} {}".format(gateway, ip))
        else:
            for gateway, ips_from_ovs in db_from_ovs.items():
                # gateway in some both db ,and check ip list change or not
                logging.info('there is change in db ,begin to check ~~~~~~~~~~~~~')
                if gateway in db_from_bgp:
                    ips_from_bgp = db_from_bgp[gateway]
                    # belong to db bgp but dont belong to ovs db
                    ips_in_bgp_not_in_ovs = ips_from_bgp.difference(ips_from_ovs)
                    for ip in ips_in_bgp_not_in_ovs:
                        speaker.prefix_del(ip)
                        logging.info('ip in bgpdb but not in ovsdb,need to del:{} {}'.format(gateway, ip))
                    # belong to ovs db but dont belong to bgp db
                    ips_in_ovs_not_in_bgp = ips_from_ovs.difference(ips_from_bgp)
                    for ip in ips_in_ovs_not_in_bgp:
                        speaker.prefix_add(ip, next_hop=gateway)
                        logging.info('ip in ovsdb but not in bgp,need to add :{} {}'.format(gateway, ip))
                else:
                    logging.info("this is gateway not in bgp")
                    # gateway in ovs db but not in bgp db ,add to bgp
                    for ip in ips_from_ovs:
                        speaker.prefix_add(ip, next_hop=gateway)
                        logging.info('ovs add new gateway need to add :{} {}'.format(gateway, ip))
            for gateway, ips_from_bgp in db_from_bgp.items():
                if gateway not in db_from_ovs:
                    for ip in ips_from_bgp:
                        speaker.prefix_del(ip)
                        logging.info('gateway in bgp db but not in ovsdb need to del :{} {}'.format(gateway, ip))

    else:
        if db_from_bgp:
            logging.info('empty in ovsdb and need to del route in bgp')
            for gateway, ips_from_bgp in db_from_bgp.items():
                for ip in ips_from_bgp:
                    speaker.prefix_del(ip)
                    logging.info('empty in ovsdb,need to del in bgp :{} {}'.format(gateway, ip))

        if not db_from_bgp:
            logging.info('this is not any info from db and bgp db ,dont do any thing')
    # update bgp db
    db_from_bgp.clear()
    db_from_bgp.update(db_from_ovs)
    logging.info(" ***************** this end **********************")
    logging.info('end time is {}'.format(datetime.datetime.now()))


def get_bgp_status():
    null = ''
    true = 'True'
    false = 'False'
    Flag = False
    status_bgp = speaker.neighbor_state_get()
    status = json.loads(status_bgp)
    for key in status.keys():
        if status[key]['info']['bgp_state'] != 'Established':
            logging.info('neighbor is abornamal .please check peer {}'.format(key))
            Flag = True
    return Flag


if __name__ == "__main__":
    speaker = BGPSpeaker(as_number=100, router_id='10.0.0.82',
                         best_path_change_handler=dump_remote_best_path_change,
                         peer_down_handler=detect_peer_down)

    speaker.neighbor_add('10.0.0.81', 100)

    # uncomment the below line if the speaker needs to talk with a bmp server.
    # speaker.bmp_server_add('192.168.177.2', 11019)
    time.sleep(5)
    while True:
        print(datetime.datetime.now())
        if (get_bgp_status()):
            logging.warning("~~~~~~~~~~~~~~~~~~~~~")
            db_from_bgp.clear()
        else:
            compare_db()
        eventlet.sleep(6)
