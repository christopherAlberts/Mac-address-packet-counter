#! /usr/local/bin/python3.5

import socket
import struct
import os
import uuid


# Display amount of packets sent with same destination MAC-address
def mac_des_count():

    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    n = 0
    mac_destination = []
    amount = []

    full = [mac_destination,  amount]

    localMac = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))

    localMac = localMac.upper()

    while True:

        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)

        if str(dest_mac) not in mac_destination:
            mac_destination.append(str(dest_mac))
            amount.append(1)
            n += 1

        elif str(dest_mac) in mac_destination:
            amount[mac_destination.index(str(dest_mac))] += 1

        else:
            print("Something went wrong")

        nnn = 0
        os.system('clear')

        print("     MAC DESTINATION COUNT")
        print("==============================")
        print("|       MAC       |  AMOUNT  |")
        print("==============================")
        print("Local MAC: " + localMac)
        print("------------------------------")

        while nnn < len(mac_destination):

            print(full[0][nnn], full[1][nnn], sep=" | ")

            nnn += 1
        print("------------------------------")


# Display amount of packets sent with same source MAC-address
def mac_src_count():

    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    n = 0
    mac_source = []
    amount = []

    full = [ mac_source,  amount]

    localMac = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))

    localMac = localMac.upper()

    while True:

        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)

        if str(src_mac) not in mac_source:
            mac_source.append(str(src_mac))
            amount.append(1)
            n += 1

        elif str(src_mac) in mac_source:
            amount[mac_source.index(str(src_mac))] += 1

        else:
            print("Something went wrong")

        nnn = 0
        os.system('clear')

        print("       MAC SOURCE COUNT")
        print("==============================")
        print("|       MAC       |  AMOUNT  |")
        print("==============================")
        print("Local MAC: " + localMac)
        print("------------------------------")

        while nnn < len(mac_source):

            print(full[0][nnn], full[1][nnn], sep=" | ")

            nnn += 1
        print("------------------------------")


# Unpacking ethernet frame
def ethernet_frame(data):

    dest_mac, src_mac, proto  = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac),socket.htons(proto), data[14:]


# Return  properly formatted MAC address (ie AA:BB:CC:DD:EE)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()
    # return mac_address


# mac_des_count()
# mac_src_count()
