import argparse
from scapy.all import *

def main():
    parser = argparse.ArgumentParser(description='Network Packet Sniffer')
    parser.add_argument('-i', '--interface', default='eth0', help='Network interface')
    parser.add_argument('-f', '--filter', default='tcp', help='BPF filter')
    parser.add_argument('-o', '--output', help='Output file')
    args = parser.parse_args()

    print(f"[*] Sniffing on {args.interface} with filter: {args.filter}")
    
    def packet_handler(packet):
        # ... (packet analysis logic from previous implementation) ...
        if args.output:
            wrpcap(args.output, packet, append=True)

    sniff(iface=args.interface, filter=args.filter, prn=packet_handler, store=0)

if __name__ == "__main__":
    main()