import dpkt
import socket
import sys


def print_pcap(pcap):
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data

            # read the source IP in src
            src = socket.inet_ntoa(ip.src)
            # read the destination IP in dst
            dst = socket.inet_ntoa(ip.dst)

            # Print the source and destination IP
            print(f"Source: {src} \t Destination: {dst}")


def main():
    # Open pcap file for reading
    # http://tcpreplay.appneta.com/wiki/captures.html
    pcap_fname = sys.argv[1]
    f = open(pcap_fname, "rb")

    # pass the file argument to the pcap.Reader function
    pcap = dpkt.pcap.Reader(f)
    print_pcap(pcap)


if __name__ == "__main__":
    main()

