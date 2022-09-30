T = int(input())

for test_case in range(1, T + 1):
    I = input()
    P = input()

    lst = list(I) + ['##'] # If I = 'Hello', lst = ['H', 'e', 'l', 'l', 'o', '##']
    
    for char in P:
        if char == lst[0]:
            lst.pop(0)

    if lst == ['##']:
        print(f'Case #{test_case}: {len(P) - len(I)}')
    else:
        print(f'Case #{test_case}: IMPOSSIBLE')


