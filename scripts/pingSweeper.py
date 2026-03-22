import os
import platform
import ipaddress

# Function to perform a ping sweep on a given network
def ping_sweeper():
    target_input = input("Enter the network prefix (e.g., 192.168.1.0/24): ")
    try:
        # Validate and create the network object
        network = ipaddress.ip_network(target_input, strict=False)
        print(f"\n--- Scanning {network} ---")
    except ValueError:
        print("Error: Invalid IP address or CIDR format. Try something like 192.168.1.0/24")
        return

    # Determine the ping command parameter based on the OS
    # Windows uses '-n', Unix-based systems use '-c'
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Iterate through all hosts in the network
    for host in network.hosts():
        ip = str(host)
        
        null_device = "nul" if platform.system().lower() == "windows" else "/dev/null"
        command = f"ping {param} 1 -w 500 {ip} > {null_device} 2>&1"
        
        response = os.system(command)

        if response == 0:
            print(f"[+] {ip} is ACTIVE")
        else:
            pass

    print("\n--- Sweep Complete ---")

if __name__ == "__main__":
    ping_sweeper()