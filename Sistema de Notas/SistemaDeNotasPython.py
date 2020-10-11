n1 = float(input('1º Bimestre: '))
n2 = float(input('2º Bimestre: '))
n3 = float(input('3º Bimestre: '))
n4 = float(input('4º Bimestre: '))
n5 = float(input('5º Bimestre: '))
n6 = float(input('6º Bimestre: '))


r = (n1 + n2 + n3 + n4 + n5 + n6) / 6


print('Sua média final é {}'.format(r))

if r>=6:
    print('Parabens você foi APROVADO(a) por média')
elif r<=5:
    print('Infelizmente você esta REPROVADO')  
