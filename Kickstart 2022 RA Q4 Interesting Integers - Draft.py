T = int(input())

for test_case in range(1, T + 1):
    A, B = tuple(map(int, input().split()))

    output = 0
    for num in range(A, B + 1):
        num = str(num)

        product = 1
        for digit in num:
            product *= int(digit)

        total = 0
        for digit in num:
            total += int(digit)

        if product % total == 0:
            output += 1

    print(f'Case #{test_case}: {output}')


























