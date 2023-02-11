c = s = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    c += 1
    s += num
print(f'Foram digitados {c} números e a soma entre eles resulta em {s}.')
