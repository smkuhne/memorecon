def printc(choice, start, chunk, narrow=False, last_text=''):
    full_text = ''
    search_choice = input("\nAre you looking for a particular value? <int,char,none> <value>\n")
    search_choice = search_choice.split(" ")
    if search_choice[0] == 'char':
        search_choice[1] = ord(search_choice[1])
    elif search_choice[0] == 'int':
        search_choice[1] = int(search_choice[1])

    if choice == 'x':
        ## Saves the current line to print

        for i in range(0, len(chunk)):
            if i % 16 == 0:
                full_text += '\n{} '.format(hex(start + i + 1))
                print ('\n{} '.format(hex(start + i + 1)), end="")
            elif i % 4 == 0:
                full_text += '     '
                print ('     ', end="")

            full_text += '%02x'%chunk[i]
            print ('%02x'%chunk[i], end="")

    elif choice == 'n':
        ## Saves the current value of the integer until all have been added
        cur_int = 0

        ## Saves the current line to print
        to_print = ''

        ## Saves a flag saying whether or not the current line should be printed
        flag = False
        for i in range(0, len(chunk)):
            ## Start new line and print only filtered results
            if i % 16 == 0:
                if flag == True or search_choice[0] != 'int':
                    if narrow:
                        try:
                            last_text.index(hex(start + i - 15))
                        except ValueError:
                            to_print = '{} '.format(hex(start + i + 1))
                            flag = False
                            continue
                    full_text += to_print + '\n'
                    print(to_print)
                    flag = False
                to_print = '{} '.format(hex(start + i + 1))

            ## Show numbers as 4 byte integers by putting chunks together
            if i % 4 == 0:
                cur_int += chunk[i]
                to_print += '{}     '.format(cur_int)
                if search_choice[0] == 'int' and search_choice[1] == cur_int:
                    flag = True
                cur_int = 0
            elif i % 3 == 0:
                cur_int += 256 * chunk[i]
            elif i % 2 == 0:
                cur_int += (256 * 256) * chunk[i]
            elif i % 1 == 0:
                cur_int += (256 * 256 * 256) * chunk[i]

    elif choice == 'c':
        ## Saves the current line to print
        to_print = ''

        ## Saves a flag saying whether or not the current line should be printed
        flag = False
        for i in range(0, len(chunk)):

            ## Prints out the line if search result was found
            if i % 16 == 0:
                if flag == True or search_choice[0] != 'char':
                    if narrow:
                        try:
                            last_text.index(hex(start + i - 15))
                        except ValueError:
                            to_print = '{} '.format(hex(start + i + 1))
                            flag = False
                            continue
                    full_text += to_print + '\n'
                    print(to_print)
                    flag = False
                to_print = '{} '.format(hex(start + i + 1))
            elif i % 4 == 0:
                to_print += '     '

            char = chr(chunk[i])
            if char == '\n':
                to_print += '\\n'
            else:
                to_print += char

            if search_choice[0] == 'char' and chunk[i] == search_choice[1]:
                flag = True

    print("\n")
    return full_text