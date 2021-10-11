<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">N-Scan</h3>

  <p align="center">
    A python based script for Local Network Scanning. 
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
      <li><a href="#prerequisites">Getting Started</a></li>
      <li><a href="#prerequisites">Prerequisites</a></li>
    <ul>
        <li><a href="#cloning">Cloning</a></li>
      </ul>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#arp-scan">ARP Scan</a></li>
        <li><a href="#tcp-scan">TCP Scan</a></li>
        <li><a href="#common-errors">Common Errors</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
# About The Project
 Simple network scanner built with Scapy(Python) for Local network Scanning.
 
<!-- GETTING STARTED -->
## Getting Started
You can use the scirpt for scanning your local network. Network scanning helps to detect all the active hosts on a network and maps them to their IP addresses. Here we use ARP and TCP scan to scan for active devices and their ports.

<!-- PREREQUISITES -->
## Prerequisites
These are the things you need to perform in order to use it.  
Install :
* [Python 3](https://www.python.org/download/releases/3.0/)
* Scapy 
```sh
   pip install scapy
   ```
### Cloning
1. Open terminal
2. Go to your desired directory
3. Clone the repo
   ```sh
   git clone https://github.com/0xr4Gn4R/N-Scan.git
   ```
3. Get into the directory
   ```sh
   cd N-Scan
   ```

<!-- USAGE -->
## Usage
Perform either an ARP scan or TCP scan.
- An ARP scan will send ARP requests to all devices on the local network, and collect the ARP replies to discover IP address to MAC address mappings.
- A TCP scan will send TCP SYN packets to all specified ports, and collect the SYN+ACK replies to discover which ports are open.

If you are on a UNIX-based system, please run the script as root (use sudo).
```
usage: python3 nscan.py [-h] {ARP,TCP} ...

positional arguments:
  {ARP,TCP}   Command to perform.
    ARP       Perform a network scan using ARP requests.
    TCP       Perform a TCP scan using SYN packets.

optional arguments:
  -h, --help  show this help message and exit
```
### ARP Scan
Either an IP address or IP address range can be used. For example, ```python3 nscan.py ARP 192.168.2.1/24``` scans all IP addresses in the 192.168.2.0/24 subnet.
```
usage: python3 nscan.py ARP [-h] IP

positional arguments:
  IP          An IP address (e.g. 192.168.1.1) or address range (e.g.
              192.168.1.1/24) to scan.

optional arguments:
  -h, --help  show this help message and exit
```

### TCP Scan
Either specific ports or a range of ports can be used. For example, ```python3 nscan.py TCP 192.168.2.1 --range 0 1000``` scans all ports from 0 to 1000.
```
usage: python3 nscan.py TCP [-h] [--range] IP ports [ports ...]

positional arguments:
  IP          An IP address or hostname to target.
  ports       Ports to scan, delimited by spaces. When --range is specified,
              scan a range of ports. Otherwise, scan individual ports.

optional arguments:
  -h, --help  show this help message and exit
  --range     Specify a range of ports. When this option is specified, <ports>
              should be given as <low_port> <high_port>.
```

### Common Errors
If you receive ```AttributeError: 'L2bpfSocket' object has no attribute 'ins'```, you likely need to run the script as root (use sudo).
See https://stackoverflow.com/questions/55881295/l3packetsocket-object-has-no-attribute-ins-when-using-send-command

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make is *highly appreciated*.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Your Name - [Subhajit Sahana](https://www.linkedin.com/in/subhajit-sahana) - sahanasubhojit@gmail.com

Project Link: [https://github.com/0xr4Gn4R/N-Scan](https://github.com/0xr4Gn4R/N-Scan)

# THIS IS ONLY FOR EDUCATIONAL PURPOSES!
