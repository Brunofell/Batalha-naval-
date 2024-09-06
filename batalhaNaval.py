# Aqui tem algumas variáveis que serão usadas ao decorrer do programa:

nlinhas = 20
ncolunas = 20
vetor = [0] * ncolunas
vetor_mapa = ["?"] * ncolunas
matriz = []
mapa = []
cont = 0
cruzador = 4
fragata = 5
porta_aviao = 3
cont_cruz = 0
cont_fragata = 0
cont_porta = 0

# Função pra vizualização e construção do mapa
def imprime_m(prm1, prm2):
    cont = 0
    while cont < prm2:
        print(prm1[cont])
        cont += 1

def jogo(linha, coluna):
    jog = 0
    if matriz[linha][coluna] == 0:
        print("Você acertou água ):")
        matriz[lin_jog] = '▲'
        mapa[lin_jog][col_jog] = '▲'
    elif matriz[linha][coluna] == 10:
        print("Você acertou uma fragata!")
        jog += 10
        matriz[lin_jog] = '☻'
        mapa[lin_jog][col_jog] = '☻'
    elif matriz[linha][coluna] == 20:
        print("Você acertou um cruzador!")
        jog += 20
        matriz[lin_jog] = '☻'
        mapa[lin_jog][col_jog] = '☻'
    elif matriz[lin_jog][col_jog] == 30:
        print("Você acertou um porta-avião!")
        jog += 30
        matriz[lin_jog] = '☻'
        mapa[lin_jog][col_jog] = '☻'
    else:
        print("Essa posição já foi bombardeada! Tente novamente:")
        jog += 0
    return jog

print("••••••" * 20)
print("• Bem-vindo ao jogo de Batalha Naval PYTHON!")
print("• Como jogar:")
print(" ► O mapa do jogo tem tamanho de uma MATRIZ 20x20, feito inteiramente na linguagem python.\n"
      " Por isso, escolha linhas e colunas entre 0 e 19 !!")
print("• Tabela de pontuação:")
print("  ► Ganhar 10 pontos, ao acertar uma fragata.")
print("  ► Ganhar 20 pontos, ao acertar um cruzador.")
print("  ► Ganhar 30 pontos, ao acertar um porta-avião.")
print("• Você apenas vencerá o jogo, quando destruir todos os navios no mapa!")
print("Trabalho feito por Bruno Feliciano!☺")
print("••••••" * 20)
# forma a matriz
while cont < nlinhas:
    matriz.append(vetor * 1)
    mapa.append(vetor_mapa * 1)
    cont += 1

for cont_cruz in range(cruzador):
    lin = int(input("• Digite a linha que os cruzadores estarão: "))
    col = int(input("• Digite a coluna que os cruzadores estarão: "))
    while lin > 19 or lin < 0 or col > 19 or col < 0 or (matriz[lin][col] == 20):
        print("Posição inválida! Tente novamenete:")
        lin = int(input("• Digite a linha que os cruzadores estarão: "))
        col = int(input("• Digite a coluna que os cruzadores estarão: "))
    matriz[lin][col] = 20
    cont_cruz += 1
for cont_fragata in range (fragata):
    lin = int(input("-> Digite a linha que as fragatas estarão: "))
    col = int(input("-> Digite a coluna que as fragatas estarão: "))
    while lin > 19 or lin < 0 or col > 19 or col < 0 or (matriz[lin][col] == 10) or (matriz[lin][col] == 20):
        print("Posição inválida! Tente novamenete:")
        lin = int(input("-> Digite a linha que as fragatas estarão: "))
        col = int(input("-> Digite a coluna que as fragatas estarão: "))
    matriz[lin][col] = 10
    cont_fragata += 1
for cont_porta in range(porta_aviao):
    lin = int(input("=> Digite a linha que os porta-aviões estarão: "))
    col = int(input("=> Digite a coluna que os porta-aviões estarão: "))
    while lin > 19 or lin < 0 or col > 19 or col < 0 or (matriz[lin][col] == 10) or (matriz[lin][col] == 20) or (matriz[lin][col] == 30):
        print("Posição inválida! Tente novamenete:")
        lin = int(input("=> Digite a linha que os porta-aviões estarão: "))
        col = int(input("=> Digite a coluna que os porta-aviões estarão: "))
    matriz[lin][col] = 30
    cont_porta += 1

# jogabilidade
print("••••••" * 30)
print("QUE SE INICIE A BATALHA NAVAL!")
print("••••••" * 30)

jog = 0

while jog < 220:
    print("")
    print("Jogue!")
    imprime_m(mapa, nlinhas)
    col_jog = int(input("Qual a coluna que você quer jogar?  "))
    lin_jog = int(input("Qual a linha que você quer jogar?  "))
    while col_jog > 19 or col_jog < 0 or lin_jog > 19 or col_jog < 0:
        print("Essa posição não existe!")
        col_jog = int(input("Qual a coluna que você quer jogar?  "))
        lin_jog = int(input("Qual a linha que você quer jogar?  "))
    print("••••••" * 20)
    jogador = int(jogo(lin_jog, col_jog))
    matriz[lin_jog] = '☻'
    jog += jogador
    if jogador == 20:
        cont_cruz -= 1
    elif jogador == 10:
        cont_fragata -= 1
    elif jogador == 30:
        cont_porta -= 1
    print(f"O jogador tem {jog} pontos")
    print("")
    print("••••••" * 20)
else:
    print(f"► Parabéns!!\n► Você destruiu TODAS os navios !!\n► Você venceu a BATALHA NAVAL com {jog} pontos!!!! ")

