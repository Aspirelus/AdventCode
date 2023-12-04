file = open("input.txt", "r")
final = []

for line in file.readlines():
    data = (
    line.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
    )
    res = [int(i) for i in data if i.isdigit()]
    print(res)
    first = [res[0]]
    last = [res[-1]]
    res1 = first + last
    out = int("".join(map(str, res1)))
    final.append(out)
print(sum(final))
file.close()
