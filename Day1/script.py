file = open("input.txt", "r")
output = open("output.txt", "w")
for line in file.readlines():
    print(line)
    output.write(line + "\n")
file.close()
output.close()
