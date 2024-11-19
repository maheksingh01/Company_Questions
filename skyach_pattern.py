def print_star_pattern():
    pattern = ''
    for row in range (7):
        for col in range (7):
            if(row == 0 and col == 3) or (row == 1 and (col == 2 or col == 4)) or (row == 2 and (col == 1 or col == 3 or col == 5)) or (row == 3 and (col == 0 or col == 2 or col == 4 or col == 6)) or (row == 4 and (col == 1 or col == 3 or col == 5)) or (row == 5 and (col == 2 or col == 4)) or (row == 6 and col == 3):
                pattern += '* '
            elif(row == 1 and col == 3) or (row == 2  and (col == 2 or col == 4)) or (row == 3 and (col == 1 or col == 3 or col == 5)) or (row == 4 and (col == 2 or col == 4)) or (row == 5 and col == 3):
                pattern += '- '
            else:
                pattern += '  '
        pattern += '\n'
    print(pattern)
    
    
print_star_pattern()