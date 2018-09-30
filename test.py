from random import randint

v = [0, 0, 0, 0, 0, 0]

for _ in range(500000):
    i = randint(1, 6)
    v[i-1] = v[i-1] + i

sumV = sum(v)
for i, v in enumerate(v):
    print("{} {}, => {:.2f}%".format(i+1, v, v/sumV * 100))