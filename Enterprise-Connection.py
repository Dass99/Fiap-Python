# Lista contendo as empresas, os tipos de dados vazados pelas empresas e a data de vazamento.
# Site utilizado para a criação da lista: https://haveibeenpwned.com/PwnedWebsites
companylist = [
    [2015, '000webhost', 'passwords', 'names', 'emails'],
    [2020, '123RF', 'passwords', 'phone numbers', 'names', 'emails'],
    [2012, '126', 'passwords', 'emails'], [2017, '2fast4u', 'passwords', 'emails'],
    [2016, 'AbuseWith.Us', 'passwords', 'email'],
    [2021, 'Aditya Birla Fashion and Retail', 'password help', 'phone numbers', 'emails'],
    [2013, 'Adobe', 'password help', 'emails'],
    [2015, 'Adult FriendFinder', 'password help', 'phone numbers', 'emails'],
    [2018, 'AerServ', 'password help', 'names', 'phone numbers', 'emails'],
    [2019, 'AgusiQ-Torrents.pl', 'passwords', 'email'],
    [2013, 'AhaShare.com', 'password help', 'email'], [2017, 'ai.type', 'password help', 'names', 'emails'],
    [2019, 'Aimware', 'password help', 'passwords', 'names', 'emails'], [2016, 'Aipai.com', 'passwords', 'emails'],
    [2018, 'Ajarn', 'passwords', 'password help', 'emails', 'names', 'phone numbers'],
    [2012, 'Netlog', 'passwords', 'emails'],
    [2017, 'NetProspex', 'emails', 'names', 'phone numbers'], [2022, 'NVIDIA', 'passwords', 'emails'],
    [2020, 'OGUsers', 'passwords', 'emails', 'names'], [2015, 'Patreon', 'passwords', 'emails'],
    [2016, 'PayAsUGym', 'password', 'password help', 'emails', 'names'],
    [2019, 'Quidd', 'passwords', 'names', 'emails'],
    [2016, 'Real Estate Mogul', 'emails', 'names', 'phone numbers'],
    [2020, 'RedDoorz', 'passwords', 'names', 'emails', 'password help', 'passwords'],
    [2017, 'Russian America', 'emails', 'names', 'phone numbers', 'password'], [2018, 'SaverSpy', 'names', 'emails'],
    [2011, 'Tianya', 'emails', 'names'], [2013, 'tumblr', 'emails', 'passwords'],
    [2013, 'Vodafone', 'emails', 'names', 'passwords', 'phone numbers'],
    [2019, 'Zynga', 'emails', 'passwords', 'phone numbers'],
    [2014, 'Dominos Pizza', 'emails', 'names', 'passwords', 'phone numbers'], [2012, 'Dropbox', 'emails', 'passwords'],
    [2013, 'Dominos Pizza', 'emails', 'names', 'passwords'], [2017, 'LiveJournal', 'emails', 'passwords'],

]

# Utilizei o ano do vazamento como primeiro elemento para facilitar a ordenação e colocar os vazamentos mais atuais antes dos mais antigos
companylist.sort()  # primeiro utilizei o sort para organizar a lista de forma crescente, fazendo as listas com anos menores aparecerem primeiro
companylist.reverse()  # Depois utilizei o reverse para colocar a lista de forma decrescente, fazendo a lista ser organizada da maior data pra menor

# Lista vaziada onde ao final do programa serão colocados os dados pedidos pelo exercicio seguindo os critérios de gravidades especificados no enunciado
ranking = []
for company in range(
        len(companylist)):  # Loop para percorrer a lista companylist e acessar seus índices que contém as listas com os dados que precisamos
    score = 0  # Como cada tipo de vazamento e mais grave que o outro e atribui pontos para eles, quanto mais grave o tipo de vazamento, mais pontos ele vale
    # Abaixo utilizei condicionais para verificar quais tipos de dados há em cada empresa dentro da lista "pai"
    if 'passwords' in companylist[company]:
        score += 5
    if 'password help' in companylist[company]:
        score += 4
    if 'phone numbers' in companylist[company]:
        score += 3

    if 'names' in companylist[company]:
        score += 2
    if 'emails' in companylist[company]:
        score += 1
    # Abaixo transformo as duas variaveis em sublistas, concateno o score com a companylist[i] de forma que o compilador leia o score antes da data
    ranking.append([score] + [companylist[company]])
# mMis uma vez utilizo sort e reverse, mas agora para ordenar por pontos, a empresa com mais pontos virá primeiro no ranking
ranking.sort()
ranking.reverse()
# OBS: Após fazer a verificação por pontos, se houver empates no número de pontos entre algumas empresas o ranking ira priorizar os vazamentos mais recentes
print('\nThe ranking below follows the breach criteria and considers the severity of each leak for sorting.\n')
for company in ranking:  # Por fim utilizo um loop para percorrer o ranking para que ele possa retornar na tela o ranking ja ordenado da forma correta.
    print(company[1])  # Utilizo o 1 como índice para que não seja mostrada a pontuação de cada empresa(score) no ranking
