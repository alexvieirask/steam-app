from schemas.game import Game
from schemas.user import User
from services.encrypt import encrypt_password

'''
Default gamelist

Games: Celeste, Undertale, Rocket League, Deltarune, Doom Eternal, Cities: Skyline,
       The Stanley Parable Ultra Deluxe, Roblox, Euro Truck Simulator 2, EA SPORTS™ FIFA 23, The Sims 4,
       Slime Rancher 2 e Genshin Impact.
'''

game01 = Game(
    title='''Celeste''',
    description=''' Ajude Madeline a enfrentar seus demônios internos em sua jornada até o topo da Montanha Celeste, 
    nesse jogo de plataforma super afiado dos criadores de TowerFall. Desbrave centenas de desafios meticulosos, 
    descubra segredos complicados e desvende o mistério da montanha.''',
    categorie='''Ação, Aventura, Indie''', 
    price=36.99,
    required_age=10,
    launch_date='''25/jan./2018''',
    developer=''' Extremely OK Games, Ltd. '''
) 

game02 = Game(
    title='''UNDERTALE''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros. 
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=19.99,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox'''
)

game03 = Game(
    title='''Rocket League''',
    description=''' Futebol e pilotagem se encontram mais uma vez na aguardada sequência do jogo clássico de arena baseado 
    em física tão amado pelos fãs, o Supersonic Acrobatic Rocket-Powered Battle-Cars! ''',
    categorie='''Esportes, Corrida''',
    price=0,
    required_age=0,
    launch_date='''7/jul./2015''',
    developer='''Psyonix LLC'''
)

game04 = Game(
    title='''Deltarune''',
    description=''' Deltarune, assim como Undertale, é um RPG eletrônico que utiliza 
    uma perspectiva de cima para baixo. O jogador controla um humano chamado 
    Kris e tem que concluir objetivos para completar o jogo. Durante algumas 
    partes do jogo, o jogador pode escolher ataques de outros personagens. ''',
    categorie='''Indie, RPG''', 
    price=0,
    required_age=14,
    launch_date='''31/out./2018''',
    developer='''tobyfox'''
) 

game05 = Game(
    title='''Doom Eternal''',
    description=''' Os exércitos do Inferno invadiram a Terra. Torne-se o 
    Slayer em uma campanha épica para um jogador e derrote demônios 
    entre dimensões para impedir a derradeira destruição da humanidade. 
    A única coisa que eles temem... é você. ''',
    categorie='''Ação''', 
    price=79,
    required_age=18,
    launch_date='''20/mar./2020''',
    developer=''' id Software '''
) 

game06 = Game(
    title='''Cities: Skyline''',
    description=''' Cities: Skylines é uma versão moderna dos simuladores 
    de cidade clássicos. O jogo introduz novos elementos de jogabilidade 
    para que você sinta a emoção e a dificuldade de criar e manter uma cidade 
    de verdade, além de aprimorar os elementos clássicos da construção de cidades. ''',
    categorie='''Simulação, Estratégia''', 
    price=74.99,
    required_age=0,
    launch_date='''10/mar./2015''',
    developer='''Colossal Order Ltd.'''
) 

game07 = Game(
    title='''The Stanley Parable Ultra Deluxe''',
    description=''' O game conta a história de Stanley, um homem que trabalha em um prédio comercial 
    como digitador. Narrado por Kevan Brighting, o título é baseado em ações e respostas através 
    de instruções dadas pelo próprio narrador. ''',
    categorie='''Aventura, Casual, Indie''', 
    price=47.49,
    required_age=0,
    launch_date='''27/abr./2022''',
    developer='''Crows Crows Crows'''
) 

game08 = Game(
    title='''Age of Mythology: Extended Edition''',
    description=''' Age of Mythology está de volta! Escolha o seu deus e vá para o campo de batalha neste clássico, 
    atualizado com integração total com o Strayworks e recursos aprimorados.''',
    categorie='''Simulação, Estratégia''', 
    price=55.99,
    required_age=0,
    launch_date='''08/mai./2014''',
    developer='''SkyBox Labs, Ensemble Studios'''
) 

game09 = Game(
    title='''Euro Truck Simulator 2''',
    description=''' Viaje pela Europa como o rei da estrada, um caminhoneiro que entrega cargas importantes em 
    distâncias impressionantes! Com dezenas de cidades para explorar, sua resistência, habilidade e 
    velocidade serão levadas ao limite. ''',
    categorie='''Indie, Simulação''', 
    price=44.99,
    required_age=0,
    launch_date='''18/out./2012''',
    developer='''SCS Software'''
) 

game10 = Game(
    title='''EA SPORTS™ FIFA 23''',
    description=''' FIFA 23 traz o Jogo de Todo Mundo aos gramados com a tecnologia HyperMotion2, proporcionando 
    ainda mais realismo às partidas, a FIFA World Cup™ masculina e feminina (lançamento durante a temporada), times 
    femininos, recursos de crossplay e muito mais. ''',
    categorie='''Simulação, Esportes''', 
    price=299,
    required_age=0,
    launch_date='''30/set./2022''',
    developer=''' EA Canada & EA Romania '''
) 

game11 = Game(
    title='''The Sims 4''',
    description=''' Curta o poder de criar e controlar pessoas num mundo virtual onde não há regras. Seja poderoso 
    e livre, divirta-se e jogue com a vida! ''',
    categorie='''Casual, Simulação''', 
    price=4773.90,
    required_age=12,
    launch_date='''02/set./2014''',
    developer='''Maxis'''
) 

game12 = Game(
    title='''Slime Rancher 2''',
    description=''' Continue as aventuras de Beatrix LeBeau enquanto ela viaja pelo Mar de Slime até a Ilha Arco-Íris, 
    uma terra repleta de mistérios antigos e cheia de novos slimes bons de remelexo para criar, na sequência do 
    grande sucesso Slime Rancher ''',
    categorie='''Ação, Aventura, Casual, Indie, Simulação''', 
    price='''36,99''',
    required_age=10,
    launch_date='''22/set./2022''',
    developer='''Monomi Park'''
) 

game13 = Game(
    title='''Genshin Impact''',
    description=''' O jogo apresenta um ambiente de mundo aberto de fantasia e sistema de batalha baseado em ação usando 
    Pontos de energia elemental e troca de personagem, e usa a monetização de jogo gacha para os jogadores obterem 
    novos personagens, armas e outros recursos.''',
    categorie='''Ação, Aventura, RPG''', 
    price=0,
    required_age=0,
    launch_date='''28/set./2020''',
    developer='''HoYoverse'''
) 

default_games = [ game01, game02, game03, game04, game05, game06, game07, game08, game09, game10, game11, game12, game13 ]


'''
Default userlist

users: Alex Vieira Dias, Emanoela Rodrigues Erthal, Igor Gramkow, Gabriel Molon Zanella, Yara Rahn, Alana Cristina Andreazza,
Amadeus Vitor Poletti, Lucas Gabriel Sievert, Beatriz Miranda, Larissa Reiter Branco, Liriel Pisetta, Lemuel Kauê Manske e Eduardo Caitano.
'''

user01 = User(
    name = '''Alex Vieira Dias''',
    username = '''alex.vieira''',
    email = '''alexvieiradias2019@gmail.com''',
    password = encrypt_password('''my-password'''),
    description = '''This profile...''',
    profile_picture = '''alex.png'''
)

user02 = User(
    name = '''Emanoela Rodrigues Erthal''',
    username = '''emanoela.erthal''',
    email = '''emanoelaerthal@gmail.com''',
    password = encrypt_password('''my-password2'''),
    description = '''This profile...''',
    profile_picture = '''emanoela.png'''
)

user03 = User(
    name = '''Igor Gramkow''',
    username = '''igor.gramkow''',
    email = '''igorgramkow@gmail.com''',
    password = encrypt_password('''my-password3'''),
    description = '''This profile...''',
    profile_picture = '''igor.png'''
)

user04 = User(
    name = '''Gabriel Molon Zanella''',
    username = '''gabriel.zanella''',
    email = '''grabrielzanella@gmail.com''',
    password = encrypt_password('''my-password4'''),
    description = '''This profile...''',
    profile_picture = '''zanella.png'''
)

user05 = User(
    name = '''Yara Rahn''',
    username = '''yara.rahn''',
    email = '''yarahn@gmail.com''',
    password = encrypt_password('''my-password5'''),
    description = '''This profile...''',
    profile_picture = '''yara.png'''
)

user06 = User(
    name = '''Alana Cristina Andreazza''',
    username = '''alana.andreazza''',
    email = '''alanaandreazza@gmail.com''',
    password = encrypt_password('''my-password6'''),
    description = '''This profile...''',
    profile_picture = '''alana.png'''
)

user07 = User(
    name = '''Amadeus Vitor Poletti''',
    username = '''amadeus.poletti''',
    email = '''amadeusvp@gmail.com''',
    password = encrypt_password('''my-password7'''),
    description = '''This profile...''',
    profile_picture = '''amadeus.png'''
)

user08 = User(
    name = '''Lucas Gabriel Sievert''',
    username = '''lucas.gabriel''',
    email = '''lucasgabriel@gmail.com''',
    password = encrypt_password('''my-password8'''),
    description = '''This profile...''',
    profile_picture = '''lucas.png'''
)

user09 = User(
    name = '''Beatriz Miranda''',
    username = '''beatriz.miranda''',
    email = '''beatrizmiranda@gmail.com''',
    password = encrypt_password('''my-password9'''),
    description = '''This profile...''',
    profile_picture = '''beatriz.png'''
)

user10 = User(
    name = '''Larissa Reiter Branco''',
    username = '''larissa.branco''',
    email = '''larissabranco@gmail.com''',
    password = encrypt_password('''my-password10'''),
    description = '''This profile...''',
    profile_picture = '''larissa.png'''
)

user11 = User(
    name = '''Liriel Pisetta''',
    username = '''liriel.pisetta''',
    email = '''lirielpisetta@gmail.com''',
    password = encrypt_password('''my-password11'''),
    description = '''This profile...''',
    profile_picture = '''liriel.png'''
)

user12 = User(
    name = '''Lemuel Kauê Manske''',
    username = '''lemuel.manske''',
    email = '''lemuelmanske@gmail.com''',
    password = encrypt_password('''my-password112'''),
    description = '''This profile...''',
    profile_picture = '''lemuel.png'''
)

user13 = User(
    name = '''Eduardo Caitano''',
    username = '''eduardo.caitano''',
    email = '''eduardocaitanop@gmail.com''',
    password = encrypt_password('''my-password13'''),
    description = '''This profile...''',
    profile_picture = '''eduardo.png'''
)


default_users = [ user01, user02, user03, user04, user05, user06, user07, user08, user09, user10, user11, user12, user13 ]