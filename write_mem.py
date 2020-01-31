#!/usr/bin/env python3

import re
import sys
from sys import byteorder
from print_contents import printc

print(byteorder)

if len(sys.argv) != 2:
    print('Usage: python3 read_mem.py PID') 
    exit(1)

maps_file = open('/proc/{}/maps'.format(sys.argv[1]), 'r')
mem_file = open('/proc/{}/mem'.format(sys.argv[1]), 'r+b')

mem_sectors = []

## Filters out any sections of memory that are not readable
for line in maps_file.readlines():
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r][-w])', line)
    if m.group(3) == 'rw':
        start = int(m.group(1), 16)
        end = int(m.group(2), 16)
        mem_sectors.append([start, end])
        print("{}".format(line), end="")

maps_file.close()

## Queries the user as to which section of memory to write to
flag = False
choice = 0

while not flag:
    choice = int(input("\nYou can write to any specified sector if you have write permission for the mem file."/
    "Specify a writable memory address in hexadecimal:"), 16)

    for sector in mem_sectors:
        if sector[0] <= choice and choice <= sector[1]:
            flag = True
            break

num = bytes([int(input("\nPlease specify the number you want to insert for this byte:"))])
mem_file.seek(choice)
mem_file.write(num)
mem_file.close()
