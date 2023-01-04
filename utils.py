import functools
import os
import re
from menus import *
from riposte import Riposte
from riposte.printer import Palette


class Application:
    def __init__(self):
        self.module = None
        self.c2 = None
        self.target = None
        self.http_server = None
        self.ssh_keyloc = None
        self.ssh_password = None
        self.ssh_user = None
        self.traffic_port = None
        self.keylog_port = None


def check_ip(ip):
    ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)" \
               "{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(ip_regex, ip):
        return ip
    else:
        print(Palette.YELLOW.format("[-] Invalid IP address"))


def check_port(port):
    port_regex = "^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|" \
                 "65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
    if re.search(port_regex, port):
        return port
    else:
        print(Palette.YELLOW.format("Invalid port number..."))


def start_banner():
    os.system("clear")
    print(Palette.BLUE.format(banner))


def start_wireshark():
    """Starts Wireshark on interface /tmp/loot"""
    os.system("wireshark -k -i /tmp/loot 2>/dev/null 1>/dev/null &")
    os.system("clear")


def dump_prep():
    """
    - Creates a named pipe locally at /tmp/loot for Wireshark to listen to.
    - Creates a TLS keylog file at /trafficThief/keyloot.log to load into Wireshark.
    - Creates a payloads directory in trafficThief/ to pre-stage payloads\
      for transfer to the target machine.
    """
    make_pipe = os.system('mkfifo /tmp/loot 2>/dev/null')
    if make_pipe == 0:
        print(Palette.GREEN.format('[+] Pipe created at /tmp/loot for wireshark interface'))
    else:
        print(Palette.YELLOW.format('[W] Pipe /tmp/loot already exists'))
        pass

    make_keylog = os.system('touch $PWD/keyloot.log 2>/dev/null')
    if make_keylog == 0:
        print(Palette.GREEN.format(f'[+] SSL/TLS keylog file for wireshark at /traffiThief/keyloot.log'))
    else:
        print(Palette.YELLOW.format("[W] Not sure whats happening...."))

    make_staging = os.system('mkdir -p $PWD/payloads 2>/dev/null ')
    if make_staging == 0:
        print(Palette.GREEN.format(f'[+] payloads directory located at trafficThief/payloads\n'))
    else:
        print(Palette.YELLOW.format("[W] Not sure whats happening...."))


