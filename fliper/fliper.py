
def verifica_fliper(a, b):
    if a == 0:
        return 'C'
    elif b == 0:
        return 'B'
    else:
        return 'A'

P, R = map(int, input().split())

print(verifica_fliper(P, R))


