import os
import mysql.connector
os.system('cls' if os.name == 'nt' else 'clear')

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def criptografia(mensagem):

    chave = [[3, 3], [2, 5]]

    mensagem = mensagem.upper().replace(" ", "")
    
    if len(mensagem) % 2 != 0:
        mensagem += 'X'
    
    resultado = ""
    
    for i in range(0, len(mensagem), 2):
        a = alfabeto.index(mensagem[i])
        b = alfabeto.index(mensagem[i+1])
        
        x = (chave[0][0]*a + chave[0][1]*b) % 26
        y = (chave[1][0]*a + chave[1][1]*b) % 26
        
        resultado += alfabeto[x] + alfabeto[y]

    print(f'{mensagem} -> {resultado}')

def descriptografia(mensagemCriptografada):
    
    inversa = [[15, 17],
               [20, 9]]
    
    resultado = ""
    for i in range(0, len(mensagemCriptografada), 2):
        a = alfabeto.index(mensagemCriptografada[i])
        b = alfabeto.index(mensagemCriptografada[i+1])
        
        x = (inversa[0][0]*a + inversa[0][1]*b) % 26
        y = (inversa[1][0]*a + inversa[1][1]*b) % 26
        
        resultado += alfabeto[x] + alfabeto[y]
    
    return resultado

# #Conexão BD
# connect = mysql.connector.connect(
#     host = "127.0.0.1",
#     user = "sparkle",
#     password = "Bheee2",
#     database = "sustentabilidade"
# )
# cursor = connect.cursor()

#Perguntas
date = input("Data de hoje (DD/MM/AAAA): ")
os.system('cls' if os.name == 'nt' else 'clear')
water = float(input("Quantidade de água consumida hoje (aprx. em l): "))
energy = float(input("Quantidade de energia consumida hoje (aprx.em kWh): "))
waste = float(input("Quantidade de resíduos não recicláveis produzidos hoje (aprx. em kg): "))
transport = 0
transportCount = 0
goodWaste = float(input("Porcentagem de resíduos recicláveis produzidos hoje (aprox. em %): "))
os.system('cls' if os.name == 'nt' else 'clear')
print("Meio(s) de transporte utilizados hoje (S (sim) ou N (não))")
transportPublic = input("Transporte Público (ônibus, metrô, trem): ").upper()
if transportPublic == "N" or transportPublic == "S":
    if transportPublic == "S":
        transport += 3
        transportCount += 1
else:
    while not (transportPublic == "N" or transportPublic == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        transportPublic = input("Transporte Público (ônibus, metrô, trem): ").upper()
transportBike = input("Bicicleta: ").upper()
if transportBike == "N" or transportBike == "S":
    if transportBike == "S":
        transport += 3
        transportCount += 1
else:
    while not (transportBike == "N" or transportBike == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        transportBike = input("Bicicleta: ").upper()
moonWalk = input("Caminhada: ").upper()
if moonWalk == "N" or moonWalk == "S":
    if moonWalk == "S":
        transport += 3
        transportCount += 1
else:
    while not (moonWalk == "N" or moonWalk == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        moonWalk = input("Caminhada: ").upper()
car = input("Carro: ").upper()
if car == "N" or car == "S":
    if car == "S":
        transport += 1
        transportCount += 1
else:
    while not (car == "N" or car == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        car = input("Carro: ").upper()
tesla = input("Carro elétrico: ").upper()
if tesla == "N" or tesla == "S":
    if tesla == "S":
        transport += 3
        transportCount += 1
else:
    while not (tesla == "N" or tesla == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        tesla = input("Carro elétrico: ").upper()
uber = input("Carona compartilhada: ").upper()
if uber == "N" or uber == "S":
    if uber == "S":
        transport += 1
        transportCount += 1
else:
    while not (uber == "N" or uber == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        uber = input("Carona compartilhada: ").upper()
os.system('cls' if os.name == 'nt' else 'clear')
#Cálculo
if water < 150:
    sustWater = "Alta Sustentabilidade"
elif water > 200:
    sustWater = "Baixa Sustentabilidade"
else:
    sustWater = "Moderada Sustentabilidade"

if energy < 5:
    sustEnergy = "Alta Sustentabilidade"
elif energy > 10:
    sustEnergy = "Baixa Sustentabilidade"
else:
    sustEnergy= "Moderada Sustentabilidade"

if goodWaste > 50:
    sustWaste = "Alta Sustentabilidade"
elif goodWaste < 20:
    sustWaste = "Baixa Sustentabilidade"
else:
    sustWaste = "Moderada Sustentabilidade"

if transportCount == 0:
    sustTransport = "Não há dados referentes ao uso de meios de transporte"
else:
    avgSustTransport = round(transport/transportCount)
    if avgSustTransport == 3:
        sustTransport = "Alta Sustentabilidade"
    elif avgSustTransport == 1:
        sustTransport = "Baixa Sustentabilidade"
    else:
        sustTransport = "Moderada Sustentabilidade"

#Prints
print(f"Água: {sustWater}")
print(f"Energia: {sustEnergy}")
print(f"Lixo: {sustWaste}")
print(f"Transporte: {sustTransport}")

criptografia(sustWater)
