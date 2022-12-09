import numpy as np

print("         Starting battleship map\n")
starting_matrix = np.array([['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
                            ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
                            ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
                            ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
                            ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
                            ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
                            ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
                            ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']])
print(starting_matrix)
print()
print("Your first ship is 2 units long, your second ship is 3 units long, your third ship is 3 units long, your fourth ship is 4 units long, and your fifth ship is 5 units long.")
print("You must place ships vertically or horizontally.")
ship_number = input("Which ship would you like to place first? Your first, second, third, fourth, or fifth?")

first_ship_start = str(input("What is the starting location of your first ship?"))
first_ship_end = str(input("What is the ending location of your first ship?"))

row = first_ship_start[1:]
col = first_ship_start[:1]

match row:
    case "1":
        start_row_pos = 0
    case "2":
        start_row_pos = 1
    case "3":
        start_row_pos = 2
    case "4":
        start_row_pos = 3
    case "5":
        start_row_pos = 4
    case "6":
        start_row_pos = 5
    case "7":
        start_row_pos = 6
    case "8":
        start_row_pos = 7
    case _:
        print("Valid input not detected.")

match col:
    case "A":
        start_col_pos = 0
    case "B":
        start_col_pos = 1
    case "C":
        start_col_pos = 2
    case "D":
        start_col_pos = 3
    case "E":
        start_col_pos = 4
    case "F":
        start_col_pos = 5
    case "G":
        start_col_pos = 6
    case "H":
        start_col_pos = 7
    case _:
        print("Valid input not detected.")

row = first_ship_end[1:]
col = first_ship_end[:1]

match row:
    case "1":
        end_row_pos = 0
    case "2":
        end_row_pos = 1
    case "3":
        end_row_pos = 2
    case "4":
        end_row_pos = 3
    case "5":
        end_row_pos = 4
    case "6":
        end_row_pos = 5
    case "7":
        end_row_pos = 6
    case "8":
        end_row_pos = 7
    case _:
        print("Valid input not detected.")

match col:
    case "A":
        end_col_pos = 0
    case "B":
        end_col_pos = 1
    case "C":
        end_col_pos = 2
    case "D":
        end_col_pos = 3
    case "E":
        end_col_pos = 4
    case "F":
        end_col_pos = 5
    case "G":
        end_col_pos = 6
    case "H":
        end_col_pos = 7
    case _:
        print("Valid input not detected.")

starting_matrix[start_row_pos, start_col_pos] = "O "
starting_matrix[end_row_pos, end_col_pos] = "O "

if start_row_pos == end_row_pos:
    row_diff = 0
    col_diff = abs(end_col_pos - start_col_pos)
else:
    col_diff = 0
    row_diff = abs(end_row_pos - start_row_pos)

print(starting_matrix)
