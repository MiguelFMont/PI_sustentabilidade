import os
import mysql.connector
os.system('cls' if os.name == 'nt' else 'clear')

#Conexão BD
connect = mysql.connector.connect(
    host = "127.0.0.1",
    user = "sparkle",
    password = "Bheee2",
    database = "sustentabilidade"
)
cursor = connect.cursor()

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
transportPublic = input("Transporte Público (ônibus, metrô, trem): ")
if transportPublic == "N" or transportPublic == "S":
    if transportPublic == "S":
        transport += 3
        transportCount += 1
else:
    while not (transportPublic == "N" or transportPublic == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        transportPublic = input("Transporte Público (ônibus, metrô, trem): ")
transportBike = input("Bicicleta: ")
if transportBike == "N" or transportBike == "S":
    if transportBike == "S":
        transport += 3
        transportCount += 1
else:
    while not (transportBike == "N" or transportBike == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        transportBike = input("Bicicleta: ")
moonWalk = input("Caminhada: ")
if moonWalk == "N" or moonWalk == "S":
    if moonWalk == "S":
        transport += 3
        transportCount += 1
else:
    while not (moonWalk == "N" or moonWalk == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        moonWalk = input("Caminhada: ")
car = input("Carro: ")
if car == "N" or car == "S":
    if car == "S":
        transport += 1
        transportCount += 1
else:
    while not (car == "N" or car == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        car = input("Carro: ")
tesla = input("Carro elétrico: ")
if tesla == "N" or tesla == "S":
    if tesla == "S":
        transport += 3
        transportCount += 1
else:
    while not (tesla == "N" or tesla == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        tesla = input("Carro elétrico: ")
uber = input("Carona compartilhada: ")
if uber == "N" or uber == "S":
    if uber == "S":
        transport += 1
        transportCount += 1
else:
    while not (uber == "N" or uber == "S"):
        print("Valor inválido. Use somente S para sim, e N para não.")
        uber = input("Carona compartilhada: ")
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