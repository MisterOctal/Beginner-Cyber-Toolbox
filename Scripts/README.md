## 🚀 Included Scripts
### 1. Port Scanner 
* **Purpose:** Identifies open TCP ports on a target IP.
* **Concepts:** TCP Handshake, Scanning using `socket`, Input Validation.

### 2. Banner Grabber
* **Purpose:** An advanced version of the Port Scanner that now also grabs the banner of an open port.
* **Concepts:** TCP Handshake, Scanning using `socket`, Banner grabbing using `recv`, Input Validation.

### 3. Ping Sweeper
* **Purpose:** Identifies active devices on a target Network.
* **Concepts:** ICMP Echo Requests, OS Detection using `platform`, Command Execution using `os`, Input Validation.

### 4. Caesar Cipher
* **Purpose:** Encrypts and decrypts messages using the Caesar cipher technique. Also includes a brute-force attack function to crack the cipher.
* **Concepts:** String manipulation, Character shifting, Brute-force attack.

### 5. Password Evaluator
* **Purpose:** Examines an input password to determine complexity.
* **Concepts:** String examination using `re`, Password Hygiene, Security Awareness.

### 6. File Integrity Checker 
* **Purporse:** Detects unauthroized changes to a file by comparing its current cryptographic hash against a saved basline. Also includes a SHA-256 hash generator.
* **Concepts:** Data Integrity (CIA Triad), SHA-256 Hashing using `hashlib`, FILE I/O, Baseline Managemenet.

### 7. IP Investigator
* **Purporse:** Performs reconnaissance on a target IP address by querying external APIs to retrieve registration data, geographical location, and organizational ownership.
* **Concepts:** Threat Intelligence, API Integration using `requests`, JSON Parsing, and OSINT (Open Source Intelligence).

### 8. Subdomain Enumerator
* **Purpose:** Performs reconnaissance on a target domain by attempting to resolve common subdomains from a wordlist to map out a target's web infrastructure.
* **Concepts:** DNS Discovery, HTTP Status Codes, File I/O (Wordlist handling), and Request Handling using  `requests`.

### 9. Simple Packet Sniffer
* **Purpose:** Intercepts and analyzes real-time network traffic to identify protocols and data transmission patterns.
* **Concepts:**  Network Layers (OSI Model), Packet Decapsulation, Raw Sockets, and Traffic Analysis using `scapy`.
---

### ⚠️ Legal Disclaimer
These tools must only be used on systems, networks, and data where you have explicit, written permission from the owner. Use on any third-party infrastructure (including public websites, company networks, or home Wi-Fi you do not own) without authorization is strictly prohibited and may be illegal under the Computer Misuse Act 1990. 

For safe and legal testing, please use services explicitly designed for this purpose, such as `scanme.nmap.org` (ensure you follow their specific rules) or your own local virtual machines.
