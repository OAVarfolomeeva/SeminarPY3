N = int(input('Введи кол-во кустов: '))
spisok = list(map(int, input(f'Введи {N} цифр через пробел: ').split()))

N = len(spisok)
spisok = spisok + spisok[:2]
m = 0
for i in range(N):
     m = max( m, spisok[i] + spisok[i+1] + spisok[i+2] )
print(m)
