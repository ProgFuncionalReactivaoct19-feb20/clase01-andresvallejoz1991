"""
andresvallejoz1991
"""
valores = [10,2,11,12,15]
for i in valores:
	if i%2 ==0:
		print (i)

resultado = list(filter(lambda x: x%2 ==0, valores))
print (resultado)

