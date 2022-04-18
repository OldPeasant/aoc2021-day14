from collections import Counter

def apply(polymer, rules):
    result = ""
    for i in range(len(polymer) - 1):
        key = polymer[i:i + 2]
        result += polymer[i]
        if key in rules:
            result += rules[key]
    result += polymer[-1]
    return result

with open("data-lrg.txt", 'r') as f:
    contents = f.read().splitlines()
    polymer = contents[0]
    rules = dict(row.split(' -> ') for row in contents[2:])

    for i in range(30):
        polymer = apply(polymer, rules)
        print(i + 1, len(polymer))

    c = list(Counter(polymer).values())
    print( max(c) - min(c) )

