rows = int(input("Number of lines: "))

# Rows iteration.
for i in range (0, rows):
  # Columns iteration.
  for j in range (0, i + 1):
    print("*", end = ' ')
  # Prints a line break after printing all character in the current row.
  print("\r")