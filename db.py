import mysql.connector
import os
os.system('cls' if os.name == 'nt' else 'clear')
mediaTransporteFinal = 0
transporteCount = 0
#Conexão BD
connect = mysql.connector.connect(
    host = "127.0.0.1",
    user = "sparkle",
    password = "Bheee2",
    database = "sustentabilidade"
)
cursor = connect.cursor()

#Parámetros
cursor.execute("use sustentabilidade")
cursor.execute("select * from dados")
for dados in cursor.fetchall():
    print(f'Data: {dados[1]}')
    print(f'Consumo de Água: {dados[2]}L')
    print(f'Consumo de Energia: {dados[3]}KWh')
    print(f'Produção de Resíduos: {dados[4]}kg')
    print(f'Produção de Resíduos Recicláveis: {dados[5]}%')
    print('**0 = não usou, 1 = usou (baixa sust), 3 = usou (alta sust)**')
    print(f'Uso de Transporte Público: {dados[6]}')
    print(f'Uso de Bicicleta: {dados[7]}')
    print(f'Uso de Caminhada: {dados[8]}')
    print(f'Uso de Carro: {dados[9]}')
    print(f'Uso de Carro Elétrico: {dados[10]}')
    print(f'Uso de Carona Compartilhada: {dados[11]}')
    print('************')
for count in range (6, 12):
    if int(dados[count]) > 0:
        mediaTransporteFinal += int(dados[count])
        transporteCount += 1

#Níveis
cursor.execute("use sustentabilidade")
cursor.execute("select * from saídas")
for saidas in cursor.fetchall():
    print(f'************')
    print(f'Consumo de Água: {saidas[1]}')
    print(f'Consumo de Energia: {saidas[2]}')
    print(f'Produção de Resíduos: {saidas[3]}')
    print(f'Uso de Transportes: {saidas[4]}')

#Médias
cursor.execute("select avg(Quantidade_de_Água_Consumida), avg(Quantidade_de_Energia), avg(Porcentagem_de_Recicláveis) from dados")
mediaAgua, mediaEnergia, mediaReciclaveis = cursor.fetchone()
print(f'\n************')
print(f'Média de Consumo de Água: {mediaAgua:.2f}L')
print(f'Média de Consumo de Energia: {mediaEnergia:.2f}KWh')
print(f'Média de Resíduos Recicláveis: {mediaReciclaveis:.2f}%')

if mediaAgua < 150:
    sustAgua = "ALTA"
elif mediaAgua <= 200:
    sustAgua = "MÉDIA"
else:
    sustAgua = "BAIXA"

if mediaEnergia < 5:
    sustEnergia = "ALTA"
elif mediaEnergia <= 10:
    sustEnergia = "MÉDIA"
else:
    sustEnergia = "BAIXA"

if mediaReciclaveis > 50:
    sustReciclaveis = "ALTA"
elif mediaReciclaveis >= 20:
    sustReciclaveis = "MÉDIA"
else:
    sustReciclaveis = "BAIXA"

if transporteCount == 0:
    sustTransporte = 0
sustTransporte = round(mediaTransporteFinal/transporteCount)
if sustTransporte == 3:
    sustTransporte = "ALTA"
elif sustTransporte == 1:
    sustTransporte = "BAIXA"
elif sustTransporte == 2:
    sustTransporte = "MÉDIA"
else:
    sustTransporte = "NÃO HÁ DADOS"

cursor.execute("select count(*) from dados")
total = cursor.fetchone()[0]

print(f'\n************')
print(f'Classificação média de Água: {sustAgua}')
print(f'Classificação média de Energia: {sustEnergia}')
print(f'Classificação média de Resíduos: {sustReciclaveis}')
print(f'Classificação média de Transporte: {sustTransporte}')