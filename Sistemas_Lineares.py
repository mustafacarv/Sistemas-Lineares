# introdução ao conceito
print('\n Um sistema linear 3x3 possui o seguinte formato:')
print('\n |Ax + Ay + Az = A| \n |Bx + By + Bz = B| \n |Cx + Cy + Cz = C| \n')

# solicitando as varíaveis para o usuário
print('para calcular este sistema, insira os valores correspondente a cada variável a seguir:')

print('olhando para a 1ª linha do nosso exercício:\n')
ax = int(input('A em AX: '))
ay = int(input('A em AY: '))
az = int(input('A em AZ: '))
a  = int(input('A em A: '))

print('olhando para a 2ª linha do nosso exercício:')
bx = int(input('B em BX: '))
by = int(input('B em BY: '))
bz = int(input('B em BZ: '))
b  = int(input('B em B: '))

print('olhando para a 3ª linha do nosso exercício:')
cx = int(input('C em CX: '))
cy = int(input('C em CY: '))
cz = int(input('C em CZ: '))
c  = int(input('C em C: '))

# início do cálculo

d1 = (ax*by)-(bx*ay)
d2 = (ax*bz)-(az*bx)
d3 = (ax*b)-(a*bx)

d4 = (ax*cy)-(ay*cx)
d5 = (ax*cz)-(az*cx)
d6 = (ax*c)-(a*cx)

d7 = (d1*d5)-(d2*d4)
d8 = (d1*d6)-(d3*d4)

# Respostas do exercício

if d7 == d8 :
    print('este é um sistema indeterminado')
if d8 == 0:
    print('Este sistema possui infinitas soluções, logo é um sistema possível e indeterminado')
else:
    print('Este sistema possui uma solução, logo é um sistema possível e determinado. E estes são os valores para X, Y e Z:')
    z = d8/d7
    y = (d3-d2*z)/d1
    x = (a-ay*y-az*z)/ax

    print('o valor de x é: ',x)
    print('o valor de y é: ',y)
    print('o valor de z é: ',z)