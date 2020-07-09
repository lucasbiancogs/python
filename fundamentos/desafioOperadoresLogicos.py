# Os trabalhos
trabalho_terca = True
trabalho_quinta = True

'''
- Confirmando os 2: Tv de 50 + sorvete
- Confirmando apenas 1: Tv de 32 + sorvete
- Não confirmando nenhum: Sem sorvete +  saúde
'''
televisao_50 = trabalho_terca and trabalho_quinta
televisao_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
saude = not sorvete

'''
print('Eles irão comprar a TV de 50"? ', televisao_50)
print('Eles irão comprar a TV de 32"? ', televisao_32)
print('Eles irão comer sorvete? ', sorvete)
print('Eles serão saudáveis? ', saude)
'''
print('Tv de 50" = {}, Tv de 32" = {}, Sorvete = {}, Saúde = {}'.format(
    televisao_50, televisao_32, sorvete, saude))
