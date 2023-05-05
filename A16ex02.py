tabela_brasileirao = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminense',
                      'Cruzeiro', 'Grêmio', 'São Paulo', 'Vasco da gama', 'Atlético-MG',
                      'Santos', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Bahia',
                      'Goiás', 'Corinthians', 'Cuiabá', 'Coritiba', 'América-MG')
for t in tabela_brasileirao:
    print(t, end=', ')
print('\n -----------------')
print(f'Os 5 primeiros times na tabela são: {tabela_brasileirao[0:5]}')
print('----' *10)
print(f' Os 4 últimos são:{tabela_brasileirao[-4:]}')
print('----' *10)
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('----' *10)
print(f'O Bahia está na {tabela_brasileirao.index("Bahia")+1} posição') #como a contagem de posições começa no 0, o Bahia está na posição 7 e é necessario adicionar o +1
