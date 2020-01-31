def printc(opt_type, start, chunk, narrow=False, last_text=''):
    searched_text = ''
    opt_search = input("\nSpecify a value to search for, it should be the same as the display type: \n")

    if opt_type == 'x':
        ## Saves the current line to print
        to_print = ''

        ## Saves a flag saying whether or not the current line should be printed
        flag = False
        for i in range(0, len(chunk)):
            if i % 16 == 0:
                if flag:
                    if narrow and last_text.find(hex(start + i - 15)) == -1:
                        flag = False
                        continue
                    searched_text += to_print + '\n'
                    print(to_print, end='')
                    flag = False
                to_print = '\n{} '.format(hex(start + i))
            elif i % 4 == 0:
                to_print += '     '

            if (opt_search == '%02x'%chunk[i]):
                flag = True

            to_print += '%02x'%chunk[i]

    elif opt_type == 'n':
        ## Saves the current value of the integer until all have been added
        forged_int = 0

        ## Saves the current line to print
        to_print = ''

        ## Converts search term to integer
        opt_search = int(opt_search)

        state = 0

        ## Saves a flag saying whether or not the current line should be printed
        flag = False
        for i in range(0, len(chunk)):
            ## Start new line and print only filtered results
            if i % 16 == 0:
                if flag:
                    if narrow and last_text.find(hex(start + i - 15)) == -1:
                        flag = False
                        continue
                    searched_text += to_print + '\n'
                    print(to_print)
                    flag = False
                to_print = '{} '.format(hex(start + i))

            ## Show numbers as 4 byte integers by putting chunks together
            if state == 0:
                forged_int += chunk[i]
                state = 1
            elif state == 1:
                forged_int += 256 * chunk[i]
                state = 2
            elif state == 2:
                forged_int += (256 * 256) * chunk[i]
                state = 3
            elif state == 3:
                forged_int += (256 * 256 * 256) * chunk[i]
                to_print += '{}     '.format(forged_int)
                if opt_search == forged_int:
                    flag = True
                forged_int = 0
                state = 0

    elif opt_type == 'c':
        ## Saves the current line to print
        to_print = ''

        ## Saves a flag saying whether or not the current line should be printed
        flag = False
        for i in range(0, len(chunk)):

            ## Prints out the line if search result was found
            if i % 16 == 0:
                if flag:
                    if narrow and last_text.find(hex(start + i - 15)) == -1:
                        flag = False
                        continue
                    searched_text += to_print + '\n'
                    print(to_print)
                    flag = False
                to_print = '{} '.format(hex(start + i))
            elif i % 4 == 0:
                to_print += '     '

            char = chr(chunk[i])
            if char == '\n':
                to_print += '\\n'
            else:
                to_print += char

            if chr(chunk[i]) == opt_search:
                flag = True

    print("\n")
    return searched_text