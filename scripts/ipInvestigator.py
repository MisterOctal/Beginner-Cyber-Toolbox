import requests
import sys

# Function to get IP data with a fallback API
def get_ip_info(ip):
    # Primary API: ip-api.com
    # Secondary API: ipinfo.io (No key needed for basic usage)
    apis = [
        f"https://ip-api.com/json/{ip}?fields=status,message,country,isp,org,as,query",
        f"https://ipinfo.io/{ip}/json"
    ]

    print(f"\n--- Investigating IP: {ip} ---")

    for url in apis:
        try:
            print(f"[*] Trying {url.split('/')[2]}...")
            response = requests.get(url, timeout=10) # Increased timeout to 10s
            
            if response.status_code == 200:
                data = response.json()
                
                # Handling different JSON structures from different APIs
                print(f"[+] IP Address:  {data.get('query') or data.get('ip')}")
                print(f"[+] Organization: {data.get('org') or data.get('asn')}")
                print(f"[+] ISP/Service:  {data.get('isp') or data.get('company', {}).get('name', 'N/A')}")
                print(f"[+] Location:     {data.get('country')}")
                
                return # Exit function once we have success
                
        except requests.exceptions.RequestException as e:
            print(f"[-] Failed to connect to this API. Moving to fallback...")
    
    print("[-] Error: All API attempts timed out or failed. Check your internet connection.")

if __name__ == "__main__":
    print("--- Robust API-Based WHOIS Tool ---")
    target_ip = input("Enter IP (e.g., 45.33.32.156): ")
    
    if target_ip:
        get_ip_info(target_ip)
    else:
        print("[-] Error: No input provided.")
        sys.exit()


    print("\nTask completed.")
