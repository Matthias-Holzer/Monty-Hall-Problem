import random

cg1 = 0
cg2 = 0
a = 2000000

for i in range(a):
    t = random.randint(1, 3)
    pool = [1, 2, 3]
    g1 = random.choice(pool)
    if pool[0] == t:
        pool.remove(pool[0])
    elif pool[1] == t:
        pool.remove(pool[1])
    elif pool[2] == t:
        pool.remove(pool[2])

    if pool[0] == g1:
        g2 = pool[1]
    else:
        g2 = pool[0]
    if g1 == t:
        cg1 += 1
    else:
        cg2 += 1

print(f"Right guesses without switch: {cg1}")
print(f"Right guesses switch: {cg2}")
print(f"Percentage without switch: {cg1/a}")
print(f"Percentage  switch: {cg2/a}")