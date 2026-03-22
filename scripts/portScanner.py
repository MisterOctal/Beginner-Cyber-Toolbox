import socket
import ipaddress
import sys

# Function to get and validate IP address input
def get_valid_ip():
    while True:
        ip_input = input("Enter the target IP address: ")
        try:
            # Validate IP address
            return str(ipaddress.ip_address(ip_input))
        except ValueError:
            print("Invalid IP address format. Please try again (e.g., 192.168.1.1).")

# Function to get and validate port range input
def get_valid_port_range():
    while True:
        try:
            start_port = int(input("Enter start port (1-65535): "))
            end_port = int(input("Enter end port (1-65535): "))
            
            # Validate port range
            if 1 <= start_port <= 65535 and 1 <= end_port <= 65535:
                if start_port <= end_port:
                    return start_port, end_port
                else:
                    print("Error: Start port must be less than or equal to end port.")
            else:
                print("Error: Ports must be between 1 and 65535.")
        except ValueError:
            print("Error: Please enter valid numerical port numbers.")

# Function to scan ports in the specified range, the main program logic
def scan_ports(ip, start, end):
    print(f"\n--- Scanning {ip} from port {start} to {end} ---")
    try:
        # Scan each port in the specified range
        for port in range(start, end + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5) # Set timeout for socket
                result = s.connect_ex((ip, port))
                if result == 0:
                    print(f"[+] Port {port} is OPEN")
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        sys.exit()
    except socket.error:
        print("\nCouldn't connect to server.")
        sys.exit()

if __name__ == "__main__":
    target_ip = get_valid_ip()
    start_p, end_p = get_valid_port_range()
    scan_ports(target_ip, start_p, end_p)
    print("\nScan completed.")
