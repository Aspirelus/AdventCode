file = open("input.txt", "r")
final = []
for line in file.readlines():
    res = [int(i) for i in [*line] if i.isdigit()]
    first = [res[0]]
    last = [res[-1]]
    res1 = first + last
    out = int("".join(map(str, res1)))
    final.append(out)
print(sum(final))
file.close()
