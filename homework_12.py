def test(*args):
    print(*args)

test(2, "string", [2, 4])


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

print(factorial(5))