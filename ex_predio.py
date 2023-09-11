andar = 20
while andar >= 1:
  if andar != 13:
    print (Andar)
    andar -= 1

for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)

numeros = [andar for andar in range(20, 0, -1) if andar != 13]
for andar in numeros:
    print(andar)

#CORREÇÃO

#No primeiro exemplo definimos o valor inicial do contador (primeiro argumento da função range) como 1, para não imprimir o valor 0. Isto não é uma questão de programação, senão apenas para começar a contagem a partir do 1ro andar, e não do "andar 0"
for i in range(1, 21):
  if (i == 13):
    continue
  else:
    print(i)

#No segundo exemplo (laço 'while') é importante lembrar do incremento do contador dentro do bloco 'if' e antes da palavra chave 'continue'. Caso esqueçamos de incrementar o contador, ou se colocarmos ele depois do 'continue', o laço de repetição continuará sendo executado de forma infinita, pois ele continuará verificando se o valor é menor que 20, mas o contador nunca mudará do valor '13'. Isto é conhecido também como um 'loop infinito' e deve ser evitado.
contador = 1
while (contador <= 20):
  if (contador == 13):
    contador = contador + 1
    continue
  else:
    print(contador)
    contador = contador + 1
#Finalmente, no terceiro exemplo, definimos o valor inicial da função range como 20 (último andar do hotel), a condição de parada como '0', e o terceiro argumento é agora um decremento de '-1', ao invés de um incremento. Perceba que, ao usar um valor inicial maior do que a condição de parada, a função 'range' sabe que a comparação a ser feita entre ambos é agora 'maior que', e não mais 'menor que' (ex. '20 > 0' e não '20 < 0').
for i in range (20, 0, -1):
  if(i == 13):
    continue
  else:
    print (1)
