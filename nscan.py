import argparse
from scapy.all import *


def arp_scan(ip):
    
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return result


def tcp_scan(ip, ports):
    
    try:
        syn = IP(dst=ip) / TCP(dport=ports, flags="S")
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(ip))

    ans, unans = sr(syn, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        if received[TCP].flags == "SA":
            result.append(received[TCP].sport)

    return result


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        dest="command", help="Command to perform.", required=True
    )

    arp_subparser = subparsers.add_parser(
        'ARP', help='Perform a network scan using ARP requests.'
    )
    arp_subparser.add_argument(
        'IP', help='An IP address (e.g. 192.168.1.1) or address range (e.g. 192.168.1.1/24) to scan.'
    )

    tcp_subparser = subparsers.add_parser(
        'TCP', help='Perform a TCP scan using SYN packets.'
    )
    tcp_subparser.add_argument('IP', help='An IP address or hostname to target.')
    tcp_subparser.add_argument(
        'ports', nargs='+', type=int,
        help='Ports to scan, delimited by spaces. When --range is specified, scan a range of ports. Otherwise, scan individual ports.'
    )
    tcp_subparser.add_argument(
        '--range', action='store_true',
        help='Specify a range of ports. When this option is specified, <ports> should be given as <low_port> <high_port>.'
    )

    args = parser.parse_args()

    if args.command == 'ARP':
        result = arp_scan(args.IP)

        for mapping in result:
            print('{} ==> {}'.format(mapping['IP'], mapping['MAC']))

    elif args.command == 'TCP':
        if args.range:
            ports = tuple(args.ports)
        else:
            ports = args.ports
        
        try:
            result = tcp_scan(args.IP, ports)
        except ValueError as error:
            print(error)
            exit(1)

        for port in result:
            print('Port {} is open.'.format(port))


if __name__ == '__main__':
    main()
