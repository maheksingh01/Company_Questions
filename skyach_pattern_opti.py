def print_star_pattern():
    # Define positions for stars and dashes
    stars = {
        (0, 3), (1, 2), (1, 4), (2, 1), (2, 3), (2, 5),
        (3, 0), (3, 2), (3, 4), (3, 6), (4, 1), (4, 3), (4, 5),
        (5, 2), (5, 4), (6, 3)
    }
    
    dashes = {
        (1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (3, 5),
        (4, 2), (4, 4), (5, 3)
    }
    
    # Iterate over the rows and columns
    for row in range(7):
        for col in range(7):
            if (row, col) in stars:
                print('* ', end='')
            elif (row, col) in dashes:
                print('- ', end='')
            else:
                print('  ', end='')
        print()

print_star_pattern()