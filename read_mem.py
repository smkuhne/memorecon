import re
import sys
from sys import byteorder
from print_contents import printc

print(byteorder)

if len(sys.argv) != 3:
    print('Usage: python3 read_mem.py <PID> <filename>'); 
    exit(1)

maps_file = open('/proc/{}/maps'.format(sys.argv[1]), 'r')
mem_file = open('/proc/{}/mem'.format(sys.argv[1]), 'rb')
save_file = open('{}'.format(sys.argv[2]), 'w+')
max_read = 1

mem_sectors = []

## Filters out any sections of memory that are not readable
for line in maps_file.readlines():
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    if m.group(3) == 'r':
        start = int(m.group(1), 16)
        end = int(m.group(2), 16)
        mem_sectors.append([start, end])
        print("({}) {}".format(len(mem_sectors), line), end="")

maps_file.close()

## Queries the user as to which section of memory to read from
choice = input("\nWhich section of memory do you want to read? ({} - {})".format(1, len(mem_sectors)))
mem_file.seek(mem_sectors[int(choice) - 1][0])
chunk = mem_file.read(mem_sectors[int(choice) - 1][1] - mem_sectors[int(choice) - 1][0])
start = mem_sectors[int(choice) - 1][0]

## Allows the user to choose how to display the segments of memory
type_choice = input("\nWould you like to display hexadecimal, numbers, or chars? (x/n/c)\n")
full_text = printc(type_choice, start, chunk)

## Writes outputs to file then closes the mem file so that it can be refreshed
save_file.write('\n =====================================\n')
save_file.write(full_text)
mem_file.close()

narrow_down = input ("Do you want to narrow down your search results? (y/n)\n")

## Allows the user to narrow down found memory locations
while(narrow_down == 'y'):
    ## Reopens memory file and gets all the chunks
    mem_file = open('/proc/{}/mem'.format(sys.argv[1]), 'rb')

    mem_file.seek(mem_sectors[int(choice) - 1][0])
    chunk = mem_file.read(mem_sectors[int(choice) - 1][1] - mem_sectors[int(choice) - 1][0])
    start = mem_sectors[int(choice) - 1][0]

    ## Filters through new chunks based on previously narrowed down results
    full_text = printc(type_choice, start, chunk, narrow=True, last_text=full_text)
    save_file.write('\n =====================================\n')
    save_file.write(full_text)

    ## Closes the file so that it can be refreshed and asks user whether or not to continue
    mem_file.close()

    narrow_down = input ("Do you want to narrow down your search results? (y/n)\n")

