import sys
import os

# Import the functions from scripts
try:
    from scripts import caesarCipher, integrityCheck, ipInvestigator, packetSniffer
    from scripts import passwordEvaluator, passwordGenerator, pingSweeper
    from scripts import portScanner, subdomainEnum, bannerGrabber
except ImportError as e:
    print(f"[-] Error: Could not import scripts. {e}")
    sys.exit(1)

def main_menu():
    # Dispatcher dictionary to map choices to functions/logic
    tools = {
        "1": {"name": "Caesar Cipher", "func": lambda: print(f"\nResult: {caesarCipher.caesar_cipher(input('Message: '), int(input('Shift: ')), input('Mode (E/D): ').lower())}")},
        "2": {"name": "File Integrity Checker", "func": integrityCheck.run_integrity_checker},
        "3": {"name": "IP Investigator", "func": lambda: ipInvestigator.get_ip_info(input("Enter IP: "))},
        "4": {"name": "Simple Packet Sniffer", "func": lambda: print("[*] Launching Sniffer...") or packetSniffer.main()}, 
        "5": {"name": "Password Auditor", "func": lambda: [print(f"[!] {s}") for s in passwordEvaluator.evaluate_password(input("Enter password: "))]},
        "6": {"name": "Password Generator", "func": lambda: print(f"[+] Generated: {passwordGenerator.generate_password(int(input('Length: ')))}")},
        "7": {"name": "Ping Sweeper", "func": pingSweeper.ping_sweeper},
        "8": {"name": "Port Scanner", "func": lambda: portScanner.scan_ports(portScanner.get_valid_ip(), *portScanner.get_valid_port_range())},
        "9": {"name": "Subdomain Enumerator", "func": lambda: subdomainEnum.enumerate_subdomains(input("Domain: "), input("Wordlist path: "))},
        "10": {"name": "Banner Grabber", "func": lambda: bannerGrabber.scan_and_grab(bannerGrabber.get_valid_ip(), *bannerGrabber.get_valid_port_range())}
    }

    while True:
        print("\n--- Octal's Beginner Cyber Toolbox ---")
        for key, tool in tools.items():
            print(f"[{key}] {tool['name']}")
        print("[0] Exit")

        choice = input("\nSelect a tool: ")

        if choice == '0':
            print("\nExiting toolbox.")
            break

        # Execute the selected tool logic
        if choice in tools:
            try:
                tools[choice]["func"]()
            except Exception as e:
                print(f"[-] An error occurred: {e}")
        else:
            print("[-] Invalid selection. Please try again.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n[-] Toolkit stopped by user.")
        sys.exit()