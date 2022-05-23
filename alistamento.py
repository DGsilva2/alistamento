from datetime import date
atual = date.today().year
nasc = int(input('em qual ano voce nasceu? '))
idade = atual - nasc
print('Quem nasceu no ano de {}, tem {} ano em {}'.format(nasc, idade, atual))
if idade == 18:
    print('devera se alistar ')
elif idade > 18:
    passou = idade - 18
    print('Voce é um refratario, ja tem {} ano que era pra ter se alistado '. format(passou))
    ano = atual - passou
    print('Era pra voce ter se alistado em {}'.format(ano))
elif idade < 18:
    falta = 18 - idade
    print('ainda falta {} ano para se alistar '.format(falta))
    tempo = atual + falta
    print('voce ira se alistar daqui {} ano'.format(falta))
print('Brasil acima de tudo e Deus acima de todos!!')