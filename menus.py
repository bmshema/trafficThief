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
               keys to Wireshark from a remote host because fuck it

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
          '     http-on             Serves HTTP server for staging_area\n'
          '     http-off            Shuts down HTTP server\n'
          '\n'
          'Current Modules:\n'
          '\n'
          '     linux-ssh:           Exfil traffic and keys over ssh session\n'
          '     linux-tcp:           Stages a payload locally to send to target to\n'
          '                          exfil over reverse TCP connection\n'
          '     windows-ssh:         Exfil traffic and keys over ssh session\n'
          '     windows-tcp:         Stages a payload locally to send to target to\n'
          '                          exfil over reverse TCP connection\n')


def show_modules():
    print('\nCurrent Modules:\n'
          '\n'
          '     linux-ssh:                  Exfil traffic and SSL/TLS keys over ssh session\n'
          '     linux-tcp:                  Stages a payload locally to send to target to\n'
          '                                 exfil over reverse TCP connection\n'
          '     windows-ssh:                Exfil traffic and SSL/TLS keys over ssh session\n'
          '     windows-tcp:                Stages a payload locally to send to target to\n'
          '                                 exfil over reverse TCP connection\n'
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
          'Notes: \n'
          '- The payload will be crafted in the trafficThief/staging_area directory\n'
          '- The HTTP server will be served in the staging_area directory\n'
          '- Any other fun payloads can be put in the staging_area also\n'
          '- Add keyloot.log to Wireshark:\n'
          '  Edit > Preferences > Protocols > TLS > Pre-Master Secret log filename\n')


def ssh_help():
    print('\nModule Commands:\n'
          '\n'
          '     show options                Shows the option values for the current module\n'
          '     run                         Runs the current module with set options\n'
          '     set <option name> <value>   Set an option in the current module\n'
          '\n')
