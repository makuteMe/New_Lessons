n = 20

used_pairs = set()
result = ""

for a in range(1, 21):
    for b in range(1, 21):
        if a != b and a != n and b != n and (a + b) % n == 0 and (a + b) == n:

            pair = tuple(sorted((a, b)))
            if pair not in used_pairs:
                used_pairs.add(pair)
                result += f"{a}{b}"

print(f"Для числа {n} сгенерирован пароль: {result}")
