banner = """
                ████████╗██████╗  █████╗ ███████╗███████╗██╗ ██████╗
                ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔════╝
                   ██║   ██████╔╝███████║█████╗  █████╗  ██║██║     
                   ██║   ██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██║██║     
                   ██║   ██║  ██║██║  ██║██║     ██║     ██║╚██████╗
                   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝ ╚═════╝

                        ████████╗██╗  ██╗██╗███████╗███████╗                
                        ╚══██╔══╝██║  ██║██║██╔════╝██╔════╝                
                           ██║   ███████║██║█████╗  █████╗                  
                           ██║   ██╔══██║██║██╔══╝  ██╔══╝                  
                           ██║   ██║  ██║██║███████╗██║                     
                           ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚═╝                                   
            A post-exploitation utility to stream traffic and SSL/TLS 
               keys to Wireshark from a remote host because why not

Global Commands:   help   |   show modules   |   use <module name>   |  unuse  |
"""


def global_help():
    # os.system("clear")
    print('\n'
          'Global Commands:\n'
          '\n'
          '     help                Print this menu\n'
          '     clear               Resets the CLI\n'
          '     exit                Exits trafficThief\n'
          '     use <module name>   Select a module to use\n'
          '     unuse               De-select the current module\n'
          '     networking          Display network interfaces\n'
          '     http-on             Serves HTTP server for payloads dir\n'
          '     http-off            Shuts down HTTP server\n'
          '\n'
          'Current Modules:\n'
          '\n'
          '     linux-ssh:           Exfil traffic and keys over ssh session\n'
          '     linux-tcp:           Crafts a payload locally to transfer to the target\n'
          '                          to execute and exfil over reverse TCP connection\n'
          '     windows-ssh:         Exfil traffic and keys over ssh session\n'
          '     windows-tcp:         Crafts a payload locally to transfer to the target\n'
          '                          to execute and exfil over reverse TCP connection\n')


def show_modules():
    print('\nCurrent Modules:\n'
          '\n'
          '     linux-ssh:               Exfil traffic and SSL/TLS keys over ssh session\n'
          '     linux-tcp:               Crafts a payload locally to transfer to the target\n'
          '                              to execute and exfil over reverse TCP connection\n'
          '\n'
          '\nIn Progress Modules:\n'
          '     windows-ssh:             Exfil traffic and SSL/TLS keys over ssh session\n'
          '     windows-tcp:             Crafts a payload locally to transfer to the target\n'
          '                              to execute and exfil over reverse TCP connection\n'
          '\n')


def tcp_help():
    print('\nModule Commands:\n'
          '\n'
          '     show options                Shows the option values for the current module\n'
          '     run                         Runs the current module with set options\n'
          '     set <option name> <value>   Set an option in the current module\n'
          '     payload                     Crafts payload with all current options\n'
          '     http-on                     Serves HTTP server (ctrl+c to stop)\n'
          '\n'
          'Usage: \n'
          '- The payload will be crafted in the trafficThief/payloads directory\n'
          '- The HTTP server will be served in the payloads directory\n'
          '- Any other fun payloads can be put in payloads too\n'
          '- Execute run to start the module locally before executing the payload\n'
          '  on the target machine\n'
          '- Add keyloot.log to Wireshark:\n'
          '  Edit > Preferences > Protocols > TLS > Pre-Master Secret log filename\n')


def ssh_help():
    print('\nModule Commands:\n'
          '\n'
          '     show options                Shows the option values for the current module\n'
          '     run                         Runs the current module with set options\n'
          '     set <option name> <value>   Set an option in the current module\n'
          '\n')
