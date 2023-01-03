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

# Concept:
trafficThief enables SSL/TLS keylogging on a remote host and feeds the keylog along with packet capture data back to you locally for viewing decrypted traffic in Wireshark in real-time.

Depending on your access to the target machine, trafficThief can interact with the target machine over ssh and feed the data back to you or craft a payload to transfer to the target machine to execute. trafficThief will set up a HTTP server in a payloads directory for payload transfer.

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

# Module Status:
- Linux modules only at this time. Should work on any Debian-based linux target. Probably others.
- Windows modules are in progress.

# Disclaimer:
You are fully responsibility for your actions related to trafficThief's use. This is proof of concept code and is still under development and may or may not be useful.
