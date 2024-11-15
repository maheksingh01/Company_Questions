def print_star_pattern():
    pattern = ''
    for row in range (9):
        for col in range (15):
            if(row == 0 and col == 14) or (row == 1 and col == 14) or (row == 2 and col == 14) or (row == 3 and col == 14) or (row == 5 and col == 0) or (row == 6 and col == 0) or (row == 7 and col == 0) or (row == 8 and col == 0) or (row ==4 and col <= 4) or (row == 4 and col >= 10):
                pattern += 'e '
            elif((row >= 2 and col >= 5) and (row <= 6 and col <= 9)):
                pattern += '* '
            else:
                pattern += '  '
        pattern += '\n'
    print(pattern)
    
    
print_star_pattern()