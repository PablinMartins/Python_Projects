
#//////////////////////////////////// 

nome = input('Qual o seu nome? ')
print(f'Olá {nome}, seja bem vindo a calculadora de Juros Compostos!\
    Aqui nós cuidamos da sua aposentadoria!'
    )

print('_______________________________________________')

investimento_inicial = float(input('Digite o valor que pretende investir inicialmente: '))
taxa = float(input('Qual a taxa mensal, em decimal, de rendimento do investimento? '))
tempo_desejado = int(input('Quantos meses você pretende deixar o investimento? '))
aporte = float(input('Quanto dinheiro você consegue aportar ao mês? '))
salario_pretendido = float(input('Qual sua pretensão salarial? '))

if taxa >= 1: 
    taxa = taxa / 100 
else:
    taxa = taxa

tempo_decorrido = 0

while tempo_decorrido < tempo_desejado:
    
    if tempo_decorrido == 0:
        
        montante_final = investimento_inicial * (1 + taxa) ** 1
        montante_final = round(montante_final, 2)
        tempo_decorrido = tempo_decorrido + 1
    else:
        montante_final = (montante_final + aporte) * (1 + taxa) ** 1
        montante_final = round(montante_final, 2)
        tempo_decorrido = tempo_decorrido + 1


if taxa > 1: 
    taxa = taxa / 100 
else:
    taxa = taxa

print('__________________________')

print(f'Parabéns {nome}! Ao final do período você terá R${montante_final}')

salario_mensal = (montante_final * taxa)
salario_mensal = round(salario_mensal, 2)

if salario_mensal >= salario_pretendido:
    print(f'Parabéns, você conseguiu sua meta salarial, atingindo {salario_mensal}.')
elif salario_mensal < salario_pretendido:
    print(f'Infelizmente seu salario pretendido não foi alcançado, ficando R${salario_mensal}')

