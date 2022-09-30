T = int(input())

for test_case in range(1, T + 1):
    N = input()

    total = 0
    for digit in N:
        total += int(digit) # a number is divisible by 9 if the sum of its digits is divisible by 9

    new_digit = 9 - (total % 9)

    if new_digit in (0, 9): 
        print(f'Case #{test_case}: {N[0]}{0}{N[1:]}') # if 9|N we can either add 9 or 0, add 0 cos 0 < 9, place 0 after 1st digit
        continue

    solved = False
    for index, digit in enumerate(N):
        if int(digit) > new_digit:
            print(f'Case #{test_case}: {N[:index]}{new_digit}{N[index:]}')
            solved = True
            break

    if not(solved):
        print(f'Case #{test_case}: {N}{new_digit}')

