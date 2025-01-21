rows = int(input("Number of lines: "))

# Rows iteration
for j in range(rows, 0, -1):
    print(" " * (rows-j) + "* " * j)
# Prints a line break after printing all character in the current row.
print("\r")