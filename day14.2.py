from collections import Counter

def apply(old_pc, rules):
    new_pc = Counter()
    for pair, count in old_pc.items():
        if pair in rules:
            ins = rules[pair]
            new_pc[pair[0] + ins] += count
            new_pc[ins + pair[1]] += count
        else:
            new_pc[pair] += count
    return new_pc

with open("data-lrg.txt", 'r') as f:
    contents = f.read().splitlines()

    polymer = '.' + contents[0] + '.'
    pc = Counter(polymer[i:i+2] for i in range(len(polymer) - 1))
    rules = dict(row.split(' -> ') for row in contents[2:])

    for i in range(40):
        pc = apply(pc, rules)

    lc = Counter()
    for pair, count in pc.items():
        lc[pair[0]] += count
        lc[pair[1]] += count
    lc.pop(".")
    print((max(lc.values()) - min(lc.values())) // 2)
