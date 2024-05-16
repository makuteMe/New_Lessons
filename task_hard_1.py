n = 3
used_pairs = set()
result = ""

a = 1
while a <= 20:
    b = 1
    while b <= 20:
        if a != b and a != n and b != n and (a + b) % n == 0 and (a + b) == n:
            pair = tuple(sorted((a, b)))
            if pair not in used_pairs:
                used_pairs.add(pair)
                result += f"{a}{b}"
        b += 1
    a += 1

print(f"Для числа {n} сгенерирован пароль: {result}")
