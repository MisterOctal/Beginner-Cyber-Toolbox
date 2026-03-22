import requests
import sys

# Function to perform subdomain enumeration
def enumerate_subdomains(domain, wordlist_path):
    print(f"\n--- Scanning Subdomains for: {domain} ---")
    
    try:
        # Open the wordlist file
        with open(wordlist_path, "r") as f:
            for line in f:
                # Clean the whitespace and build the URL
                subdomain = line.strip()
                if not subdomain:
                    continue
                
                url = f"http://{subdomain}.{domain}"
                
                try:
                    # We use a short timeout (2s) to keep the script moving
                    response = requests.get(url, timeout=2)
                    
                    # If the request succeeds, the subdomain is likely active
                    if response.status_code == 200:
                        print(f"[+] Found: {url} (Status: 200)")
                    else:
                        print(f"[!] Found: {url} (Status: {response.status_code})")
                        
                except requests.ConnectionError:
                    # This happens if the subdomain does not exist
                    pass
                except requests.Timeout:
                    # Skip if the server takes too long to respond
                    pass

    except FileNotFoundError:
        print(f"[-] Error: Wordlist file '{wordlist_path}' not found.")
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        sys.exit()

if __name__ == "__main__":
    print("--- Subdomain Enumerator Tool ---")
    
    # Target domain (e.g., scanme.nmap.org)
    target_domain = input("Enter the target domain (e.g., google.com): ")
    
    # Path to your wordlist file
    wordlist = input("Enter path to subdomain wordlist (e.g., subs.txt): ")

    if target_domain and wordlist:
        enumerate_subdomains(target_domain, wordlist)
    else:
        print("[-] Error: Domain and Wordlist path are required.")
        sys.exit()

    print("\nTask completed.")