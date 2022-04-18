from collections import Counter

with open("input.txt", 'r') as f:
    contents = f.read().splitlines()
    polymer = '.' + contents[0] + '.'
    pc = Counter(polymer[i:i+2] for i in range(len(polymer) - 1))
    rules = dict(row.split(' -> ') for row in contents[2:])

    for i in range(40):
        new_pc = Counter()
        for pair, count in pc.items():
            if pair in rules:
                ins = rules[pair]
                new_pc[pair[0] + ins] += count
                new_pc[ins + pair[1]] += count
            else:
                new_pc[pair] += count
        pc = new_pc
    lc = Counter()
    for pair, count in pc.items():
        lc[pair[0]] += count
        lc[pair[1]] += count
    lc.pop(".")
    print(f'Result: {(max(lc.values()) - min(lc.values())) // 2:,}')
