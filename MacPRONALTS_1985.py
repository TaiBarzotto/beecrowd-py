'''
O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC. Só que teve um problema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge você para fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do produto e seu respectivo valor.

1001 | R$ 1.50
1002 | R$ 2.50
1003 | R$ 3.50
1004 | R$ 4.50
1005 | R$ 5.50

Entrada
A primeira entrada informada é a quantidade de produtos comprados (1 <= p <= 5). Para cada produto segue a quantidade (1 <= q <= 500) que o consumidor comprou.

Obs.: não poderão ser informados números de produtos repetidos.

Saída
Você deve imprimir o valor da compra com duas casas decimais.
'''
#RESPOSTA

codigo_valores={'1':1.50,'2':2.50,'3':3.50,'4':4.50,'5':5.50}
p=int(input())
valor_final=0
for i in range(p):
    codigo,qntd=input().split()
    qntd=int(qntd)
    key=codigo[3]
    valor=codigo_valores[key]
    valor_final+=(valor*qntd)
    
print(f"{valor_final:.2f}")