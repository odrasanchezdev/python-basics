rows = int(input("Number of lines: "))

# Rows iteration
for j in range(1, rows + 1):
    print(" " * (rows-j) + "* " * j)
