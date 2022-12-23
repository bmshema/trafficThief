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

# trafficThief
A post-exploitation utility to stream traffic and SSL/TLS keys to Wireshark from a remote host.

# Dependencies:
- sshpass
- Wireshark
```
sudo apt install sshpass wireshark
```
- Riposte
```
cd trafficThief
pip install -r requirements.txt
```

# Usage:
```
sudo python3 trafficThief.py
```
