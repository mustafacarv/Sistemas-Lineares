x=y=0
escolha = int(input('escolha a opção: '))

while escolha not in (2,3):
	escolha = int(input('A opção inserida é inválida!\nEscolha novamente: '))

if escolha == 2:
	# introdução ao conceito
	print('\n Um sistema linear 2x2 possui o seguinte formato:')
	print('\n |Ax + Ay = A| \n |Bx + By = B| \n')

	# solicitando as varíaveis para o usuário
	print('para calcular este sistema, insira os valores correspondente a cada variável a seguir:')
	print('olhando para a 1ª linha do nosso exercício:\n')
	ax = int(input('A em AX: '))
	ay = int(input('A em AY: '))
	a  = int(input('A em A: '))
	print('olhando para a 2ª linha do nosso exercício:')
	bx = int(input('B em BX: '))
	by = int(input('B em BY: '))
	b  = int(input('B em B: '))

	# início do cálculo
	d1 = (ax*by)-(bx*ay)
	d2 = (ax*b)-(a*bx)

	# Respostas do exercício
	if d1 == d2 == 0 :
		print('Este sistema possui infinitas soluções, logo é um sistema possível e indeterminado')
	if d1 == 0 and d2 != 0:
		print('Este sistema não possui solução, logo é um sistema impossível')
	else:
		print('Este sistema possui uma solução, logo é um sistema possível e determinado. E estes são os valores para X e Y:')
		y = d2/d1
		x = (a-ay*y)/ax
		print('o valor de x é: ',x)
		print('o valor de y é: ',y)
else:
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
	if d7 == d8 == 0 :
		print('Este sistema possui infinitas soluções, logo é um sistema possível e indeterminado')
	if d7 == 0 and d8 != 0:
		print('Este é sistema impossível')
	else:
		print('Este sistema possui uma solução, logo é um sistema possível e determinado. E estes são os valores para X, Y e Z:')
		z = d8/d7
		y = (d3-d2*z)/d1
		x = (a-ay*y-az*z)/ax
		print('o valor de x é: ',x)
		print('o valor de y é: ',y)
		print('o valor de z é: ',z)