import os

def start():
    print(f'--------------------------Olá, Bem vindo ao ChatQuiz Da Bíblia--------------------------{os.linesep}')

    print(f'A Bíblia é uma coleção de livros sagrados escritos por antigos profetas e historiadores. {os.linesep}Esses autores registraram a relação entre Deus e Seu povo por mais de 4 mil anos.{os.linesep}Suas palavras inspiradas são o que hoje conhecemos como a Bíblia Sagrada.{os.linesep}')
    print(f'Seguir os ensinamentos encontrados na Bíblia nos ajuda a conhecer quem é Deus, a aprender{os.linesep}com pessoas boas que O amavam e a entender melhor como Ele deseja que vivamos.{os.linesep}-----------------------------------------------------------------------------------------')
    
    cont = True
    res = True;
    while cont:
        resposta = input(f'Você deseja participar de um Quiz com perguntas bíblicas?{os.linesep}Digite Sua Resposta: ')

        if resposta == 'Sim' or  resposta == 'sim' or  resposta == 'Si' or  resposta == 'si' or resposta == 'S' or  resposta == 's':
            cont = False;
            nome = input('Digite Seu Nome: ')
            while res:         
                nivel = input(f'{os.linesep}Escolha um Nível de dificuldade:{os.linesep}[1] - Fácil{os.linesep}[2] - Médio{os.linesep}[3] - Difícil{os.linesep}Nível: ')

                print('-----------------------------------')
                if nivel == '1' or nivel == '2' or nivel == '3':
                    ProcessarResposta(nivel,nome)
                    continuar = input(f'Deseja Continuar?{os.linesep}Digite Sua Resposta: ')
                    if continuar == 'Não' or  continuar == 'não' or  continuar == 'Nao' or  continuar == 'nao' or continuar == 'No' or  continuar == 'no' or continuar == 'N' or  continuar == 'n':
                        print(f'{os.linesep}-------------------------------------------------------')
                        print(f'Obrigado ' + nome + f' por participar. Volte Sempre! :)')
                        print(f'-------------------------------------------------------{os.linesep}')
                        res = False;                      
                else:
                    print('Digite apenas 1, 2 ou 3')

        elif resposta == 'Não' or  resposta == 'não' or  resposta == 'Nao' or  resposta == 'nao' or resposta == 'Na' or  resposta == 'na' or resposta == 'N' or  resposta == 'n':
            print("Sem Problemas, volte quando quiser :)")
            cont = False;
        else:
            print(f'-----------------------------------{os.linesep}Desculpa, não consegui entender. Por favor, digite apenas "Sim" ou "Não".{os.linesep}')


def ProcessarResposta(nivel, nome):
    if nivel == '1':

        resultado = 0;

        print(f' Voce selecionou o nível Fácil{os.linesep}-----------------------------------')
        resposta = input(f'1) - Quem era considerado o pai da fé?{os.linesep}{os.linesep}[1] - Abraão{os.linesep}[2] - Jacó{os.linesep}[3] - José{os.linesep}[4] - Isaac{os.linesep}Sua Resposta: ')
        if resposta == '1':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Abraão é considerado o pai da fé{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'2) - Quem Deus enviou para libertar o povo hebreu do Egito?{os.linesep}{os.linesep}[1] - José{os.linesep}[2] - Moisés{os.linesep}[3] - Noé{os.linesep}[4] - Abraão{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Moisés que libertou o povo hebreu do Egito{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'3) - Quem era a mãe de Jesus?{os.linesep}{os.linesep}[1] - Rebeca{os.linesep}[2] - Sarah{os.linesep}[3] - Izabel{os.linesep}[4] - Maria{os.linesep}Sua Resposta: ')
        if resposta == '4':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Maria era a mãe de Jesus{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'4) - "Não amem o mundo e nem o que há no mundo. Se alguém ama o mundo, o amor do Pai não está nele." Onde se encontra essa passagem?{os.linesep}{os.linesep}[1] - Isaías 40, 48{os.linesep}[2] - Isaías 6, 8{os.linesep}[3] - 1 João 2, 15{os.linesep}[4] - 1 João 2, 3{os.linesep}Sua Resposta: ')
        if resposta == '3':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Essa passagem está em 1 João 2, 15{os.linesep}')
       
        print('-----------------------------------')
        resposta = input(f'5) - Quem foi levado ao céu em uma carruagem de fogo?{os.linesep}{os.linesep}[1] - Jonas{os.linesep}[2] - Elias{os.linesep}[3] - Eliseu{os.linesep}[4] - Isaac{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Elias foi levado ao céu em uma carruagem de fogo{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'6) - Quem era perseguidor de cristãos e depois se tornou o maior apóstolo da Bíblia?{os.linesep}{os.linesep}[1] - Pedro{os.linesep}[2] - João{os.linesep}[3] - Paulo{os.linesep}[4] - Estevão{os.linesep}Sua Resposta: ')
        if resposta == '3':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Paulo perseguia o povo de Deus, mas depois se tornou um dos apóstolos de Jesus{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'7) - Quem construiu a arca?{os.linesep}{os.linesep}[1] - Adão{os.linesep}[2] - Isaac{os.linesep}[3] - Noé{os.linesep}[4] - Abraão{os.linesep}Sua Resposta: ')
        if resposta == '3':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Noé construiu a arca{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'8) - Em qual monte a arca encalhou?{os.linesep}{os.linesep}[1] - Monte Nemrut{os.linesep}[2] - Monte Ararat{os.linesep}[3] - Monte Taurus{os.linesep}[4] - Monte Hasan{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}A arca encalhou no Monte Ararat{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'9) - Quem foi engolido por um peixe grande?{os.linesep}{os.linesep}[1] - Jonas{os.linesep}[2] - Daniel{os.linesep}[3] - Jonathas{os.linesep}[4] - Salomão{os.linesep}Sua Resposta: ')
        if resposta == '1':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Jonas foi engolido por um peixe grande{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'10) - Quantos eram os discípulos de Jesus?{os.linesep}{os.linesep}[1] - 11{os.linesep}[2] - 12{os.linesep}[3] - 13{os.linesep}[4] - 10{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Reposta Correta: 12 Discípulos{os.linesep}')

        if resultado >= 8:
            print('Incrível ' + nome + f'! Você Acertou ' + repr(resultado) + f' de 10')
            print(f'Que tal desafiar os seus amigos e ver se eles vão tão bem quanto você?{os.linesep}-----------------------------------')
        elif resultado >= 5:
            print('Parabéns ' + nome + f'! Você Acertou ' + repr(resultado) + f' de 10')
            print(f'Que tal tentar mais uma vez? Quem sabe você consegue acertar todas na próxima!{os.linesep}-----------------------------------')
        else:
            print(f'Você Acertou ' + repr(resultado) + f' de 10')
            print(f'Que tal tentar mais uma vez? Quem sabe você consegue acertar todas na próxima!{os.linesep}-----------------------------------')

    if nivel == '2':
        resultado = 0;

        print(f' Voce selecionou o nível Médio{os.linesep}-----------------------------------')
        resposta = input(f'1) - Qual das opções é a correta?{os.linesep}{os.linesep}[1] - "Ora, a fé é a certeza de coisas que se esperam, a convicção de fatos que não se veem." Hebreus- 11:1"{os.linesep}[2] - NDA ( Nenhuma das alternativas){os.linesep}[3] - "A terra era sem forma e vazia; havia trevas sobre a face do abismo, e o Espírito de Deus se movia as águas." Gênesis- 1:3"{os.linesep}[4] - Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo o que nele crê não pereça mas tenha a vida eterna." João- 6:16{os.linesep}Sua Resposta: ')
        if resposta == '1':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}"Ora, a fé é a certeza de coisas que se esperam, a convicção de fatos que não se veem." Hebreus- 11:1"{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'2) - Qual era o nome da sogra de Rute?{os.linesep}{os.linesep}[1] - Sara{os.linesep}[2] - Noemi{os.linesep}[3] - Eva{os.linesep}[4] - Orfa{os.linesep}[5] - Miriã{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Correta: Noemi{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'3) - Qual foi o monte que o povo de Israel temeu subir?{os.linesep}{os.linesep}[1] - Sião{os.linesep}[2] - Tabor{os.linesep}[3] - Herbom{os.linesep}[4] - Sinai{os.linesep}Sua Resposta: ')
        if resposta == '4':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Correta: Monte Sinai{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'4) - Porque o povo de Israel temeu o Monte?{os.linesep}{os.linesep}[1] - Pois Deus havia descido ao monte e Ele podia ser visto no topo do monte, e sua glória era tanta, que o povo não conseguia olhar.{os.linesep}[2] - Pois Deus havia descido ao monte e a trombeta que soava era tão alta que o povo temeu perder a audição.{os.linesep}[3] - Pois Deus havia descido ao monte e havia animais perigosos demarcando os limites, então o povo recuou.{os.linesep}[4] - Pois Deus havia descido ao monte e houve trovões e relâmpagos, uma grossa nuvem cobriu o monte, e dele saia fumaça.{os.linesep}Sua Resposta: ')
        if resposta == '4':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Pois Deus havia descido ao monte e houve trovões e relâmpagos, uma grossa nuvem cobriu o monte, e dele saia fumaça.{os.linesep}')
       
        print('-----------------------------------')
        resposta = input(f'5) - Quantos animais entraram na arca de Noé?{os.linesep}{os.linesep}[1] - 25.000.000.000{os.linesep}[2] - Um de cada espécie{os.linesep}[3] - Um par de cada espécie{os.linesep}[4] - Dois pares de cada espécie{os.linesep}Sua Resposta: ')
        if resposta == '3':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Um par de cada espécie{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'6) - Quem entrou na arca de Noé?{os.linesep}{os.linesep}[1] - Noé e seus filhos, sua mulher{os.linesep}[2] - Noé, seus filhos, sua mulher, as mulheres de seus filhos e seus netos{os.linesep}[3] - Noé e sua mulher{os.linesep}[4] - Noé apenas{os.linesep}[5] - Noé, seus filhos, sua mulher e as mulheres de seus filhos{os.linesep}Sua Resposta: ')
        if resposta == '5':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Noé, seus filhos, sua mulher e as mulheres de seus filhos{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'7) - Qual dessas frases não foi dita por Jesus?{os.linesep}{os.linesep}[1] - Quem quiser ser líder deve ser primeiro servo. Se você quiser liderar, deve servir.{os.linesep}[2] - Eu sou a ressurreição e a vida. Quem crê em mim, ainda que morra, viverá; e quem vive e crê em mim nunca morrerá.{os.linesep}[3] - E conhecereis a verdade e a verdade vos libertará{os.linesep}[4] - Não se regozija com a injustiça, mas se regozija com a verdade; Tudo sofre, tudo crê, tudo espera, tudo suporta. O amor jamais acaba.{os.linesep}Sua Resposta: ')
        if resposta == '4':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Não se regozija com a injustiça, mas se regozija com a verdade; Tudo sofre, tudo crê, tudo espera, tudo suporta. O amor jamais acaba.{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'8) - Quantos livros essas pessoas escreveram na Bíblia respectivamente?João/Marcos/Paulo/Pedro{os.linesep}{os.linesep}[1] - 6/1/13/4{os.linesep}[2] - 6/2/14/4{os.linesep}[3] - 3/8/12/1{os.linesep}[4] - 5/1/14/2{os.linesep}[5] - 5/1/13/2{os.linesep}Sua Resposta: ')
        if resposta == '5':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: 5/1/13/2{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'9) - Jesus continuou na terra depois de ressuscitar.{os.linesep}{os.linesep}[1] - Falso{os.linesep}[2] - Verdadeiro{os.linesep}Sua Resposta: ')
        if resposta == '1':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Verdadeira{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'10) - Quanto tempo Jesus passou na terra depois de ressuscitar e antes de assubir aos céus?{os.linesep}{os.linesep}[1] - 1 ano{os.linesep}[2] - 40 dias{os.linesep}[3] - uma semana{os.linesep}[4] - 20 dias{os.linesep}[5] - 30 dias{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: 40 dias{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'11) - Ao invés de ir para Nínive, Jonas embarcou rumo a qual cidade?{os.linesep}{os.linesep}[1] - Galiléia{os.linesep}[2] - Creta{os.linesep}[3] - Tarsis{os.linesep}[4] - Roma{os.linesep}[5] - Egito{os.linesep}Sua Resposta: ')
        if resposta == '3':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Tarsis{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'12) - O que Jonas fez para sair da barriga do grande peixe?{os.linesep}{os.linesep}[1] - Pregou{os.linesep}[2] - Orou{os.linesep}[3] - Dormiu{os.linesep}[4] - Gritou{os.linesep}[5] - Chorou{os.linesep}Sua Resposta: ')
        if resposta == '2':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Orou{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'13) - Qual pessoa tratou de sepultar o corpo de Jesus?{os.linesep}{os.linesep}[1] - Simão Cirineu{os.linesep}[2] - Gamaliel{os.linesep}[3] - José de Arimateia{os.linesep}[4] - Maria Madalena{os.linesep}[5] - Pedro{os.linesep}Sua Resposta: ')
        if resposta == '3':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: JJosé de Arimateia{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'14) - Qual a idade de Calebe ao entrar na Terra Prometida?{os.linesep}{os.linesep}[1] - 85 anos{os.linesep}[2] - 90 anos{os.linesep}[3] - 100 anos{os.linesep}[4] - 120 anos{os.linesep}[5] - 95 anos{os.linesep}Sua Resposta: ')
        if resposta == '1':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: 85 anos{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'15) - Quais personagens eram gêmeos?{os.linesep}{os.linesep}[1] - João e Tiago{os.linesep}[2] - José e Benjamim{os.linesep}[3] - Pedro e Thiago{os.linesep}[4] - Jacó e Esaú{os.linesep}[5] - João e Judas{os.linesep}Sua Resposta: ')
        if resposta == '4':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Jacó e Esaú{os.linesep}')


        if resultado >= 13:
            print('Incrível ' + nome + f'! Você Acertou ' + repr(resultado) + f' de 15')
            print(f'Que tal desafiar os seus amigos e ver se eles vão tão bem quanto você?{os.linesep}-----------------------------------')
        elif resultado >= 8:
            print('Parabéns ' + nome + f'! Você Acertou ' + repr(resultado) + f' de 15')
            print(f'Que tal tentar mais uma vez? Quem sabe você consegue acertar todas na próxima!{os.linesep}-----------------------------------')
        else:
            print(f'Você Acertou ' + repr(resultado) + f' de 15')
            print(f'Que tal tentar mais uma vez? Quem sabe você consegue acertar todas na próxima!{os.linesep}-----------------------------------')
    
    if nivel == '3':

        resultado = 0;

        print(f' Voce selecionou o nível Difícil{os.linesep}-----------------------------------')
        resposta = input(f'1) - Quem foi o personagem que foi tímido e medroso, que se tornou um grande estadista e escritor?{os.linesep}{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Moisés' or resposta == 'moises' or resposta == 'Moises' or resposta == 'moisés':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Moisés{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'2) - Quem foi o personagem da Bíblia que era perseguidor dos cristãos e se tornou um grande evangelista?{os.linesep}{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Paulo' or resposta == 'paulo':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Paulo{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'3) - Quem foi o personagem da Bíblia que era um pescador de peixes e se tornou um ´´pescador`` de pessoas?{os.linesep}{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Pedro' or resposta == 'pedro':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Pedro{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'4) - Quem foi o personagem da Bíblia que era um garoto mimado e se tornou o vice-governador do Egito?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'José' or resposta == 'josé' or resposta == 'Jose' or resposta == 'jose':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: José{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'5) - Quem foi o personagem da Bíblia que era um agropecuarista que se transformou em um profeta de Deus?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Amós' or resposta == 'amós' or resposta == 'Amos' or resposta == 'amos':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Amós{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'6) - Quem foi a personagem da Bíblia que era uma garota desconhecida e se tornou uma destemida defensora de seu povo?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Ester' or resposta == 'ester':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Ester{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'7) - Quem foi o personagem da Bíblia que era um enganador e se tornou um pai da nação israelita?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Jacó' or resposta == 'jacó' or resposta == 'Jaco' or resposta == 'jaco':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Jacó{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'8) - Quem foi o personagem da Bíblia que era um desonesto e se tornou um seguidor fiel de Cristo?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Zaqueu' or resposta == 'zaqueu':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Zaqueu{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'9) - Quem foi o personagem da Bíblia que era um prostituta e se tornou uma ancestral de Jesus?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Raabe' or resposta == 'raabe':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Raabe{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'10) - Qual era o nome da serpente de bronze que Moisés tinha feito?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Neutsã' or resposta == 'neutsâ' or resposta == 'Neutsa' or resposta == 'neustsa':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Neutsã{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'11) - Quando Jesus nasceu, onde Ele foi colocado?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Manjedoura' or resposta == 'manjedoura' or resposta == 'Manjedora' or resposta == 'manjedora':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Manjedoura{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'12) - Quem foi o 'assistente' do profeta Elias?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Eliseu' or resposta == 'eliseu':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Eliseu{os.linesep}')
        
        print('-----------------------------------')
        resposta = input(f'13) - Quem era a mãe de Samuel?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Ana' or resposta == 'ana':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Ana{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'14) - Quem a Bíblia diz que foi pior que todos os reis de Israel?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Acabe' or resposta == 'acabe' or resposta == 'Neutsa' or resposta == 'neustsa':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Acabe{os.linesep}')

        print('-----------------------------------')
        resposta = input(f'15) - Quem era a mãe de Ismael, filho de Abraão?{os.linesep}Digite Sua Resposta: ')
        if resposta == 'Hagar' or resposta == 'hagar':
            print(f'Resposta Certa{os.linesep}')
            resultado += 1
        else:
            print(f'Resposta Errada!{os.linesep}Resposta Certa: Hagar{os.linesep}')

        if resultado >= 12:
            print('Incrível ' + nome + f'! Você Acertou ' + repr(resultado) + f' de 15')
            print(f'Que tal desafiar os seus amigos e ver se eles vão tão bem quanto você?{os.linesep}-----------------------------------')
        elif resultado >= 8:
            print('Parabéns ' + nome + f'! Você Acertou ' + repr(resultado) + f' de 15')
            print(f'Que tal tentar mais uma vez? Quem sabe você consegue acertar todas na próxima!{os.linesep}-----------------------------------')
        else:
            print(f'Você Acertou ' + repr(resultado) + f' de 15')
            print(f'Que tal tentar mais uma vez? Quem sabe você consegue acertar todas na próxima!{os.linesep}-----------------------------------')


if __name__ == '__main__':
    start()

