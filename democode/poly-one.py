from collections import Counter

with open("input.txt", 'r') as f:
    contents = f.read().splitlines()
    polymer = contents[0]
    rules = dict(row.split(' -> ') for row in contents[2:])

    for i in range(10):
        next_polymer = ""
        for j in range(len(polymer) - 1):
            next_polymer += polymer[j]
            next_polymer += rules.get(polymer[j:j+2], "")
        next_polymer += polymer[-1]
        #print(f'{i + 1}: {len(polymer):,}')
        polymer = next_polymer

    #c = list(Counter(polymer).values())
    c = Counter(polymer).values()
    print(f'Result: { max(c) - min(c) }')

