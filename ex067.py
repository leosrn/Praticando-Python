while True:
    tab = int(input('De qual número deseja a tabuada? '))
    print('--==--'*10)
    if tab < 0:
        break
    for c in range(0,11):
        print(f'{tab} X {c} = {tab * c}')
    print('--==--'*10)
print('Programa finalizado!')