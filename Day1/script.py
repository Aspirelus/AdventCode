# open input.txt file
file = open("input.txt", "r")
# define list for final sum
final = []

for line in file.readlines():
    # word replacing methode for 2nd part
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
    # iterate through each element and identify digits
    res = [int(i) for i in data if i.isdigit()]
    # pick first and last digit from list
    first = [res[0]]
    last = [res[-1]]
    res1 = first + last
    # combine first and last digit into a string
    out = int("".join(map(str, res1)))
    # add each string to final list
    final.append(out)
# final print with solution
print(sum(final))
file.close()
