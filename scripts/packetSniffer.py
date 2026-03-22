from scapy.all import sniff, IP, TCP, UDP, ICMP
import sys

# Function to process and format each captured packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        protocol = "OTHER"

        # Determine the protocol for clearer output
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        print(f"[+] {protocol} Packet: {ip_layer.src} -> {ip_layer.dst}")

        # If it's a TCP packet, show the ports (similar to your banner grabber logic)
        if packet.haslayer(TCP):
            print(f"    Ports: {packet[TCP].sport} -> {packet[TCP].dport}")

# Main execution block
if __name__ == "__main__":
    print("--- Simple Network Packet Sniffer ---")
    print("[*] Note: This script requires Administrative/Sudo privileges.")
    
    try:
        interface = input("Enter interface to sniff (e.g., eth0, wlan0, or leave blank): ")
        count = input("Enter number of packets to capture (0 for infinite): ")
        
        # Convert count to integer
        packet_count = int(count) if count.strip() else 0
        
        print(f"\n--- Starting capture on {interface if interface else 'default interface'} ---")
        print("--- Press Ctrl+C to stop ---\n")

        # Start sniffing
        # iface: the network interface; prn: callback function; count: number of packets
        sniff(iface=interface if interface else None, prn=packet_callback, count=packet_count)

    except PermissionError:
        print("[-] Error: Permission denied. Please run as Root/Administrator.")
    except KeyboardInterrupt:
        print("\nSniffing stopped by user.")
        sys.exit()
    except Exception as e:
        print(f"[-] An error occurred: {e}")

    print("\nCapture completed.")