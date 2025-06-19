import pymysql
import os

connect = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sustentabilidade"
)

cursor = connect.cursor()


alfabeto = [' ', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
chave = [[1, 2],[3, 5]]
continuar = True

#Funções
def ajuste_transporte(valor):
        if valor == "0":
            return "Não"
        if valor == "1" or valor == "3":
            return "Sim"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cript(texto):
    texto = texto.upper()
    if len(texto) % 2 != 0:
        texto += ' '
    resultado = ""

    for i in range(0, len(texto), 2):
        a = alfabeto.index(texto[i])
        b = alfabeto.index(texto[i + 1])
        x = (chave[0][0]*a + chave[0][1]*b) % 27
        y = (chave[1][0]*a + chave[1][1]*b) % 27
        resultado += alfabeto[x] + alfabeto[y]
        
    return resultado

def decript(texto_cifrado):
    # Inverso da matriz mod 27
    a, b = chave[0]
    c, d = chave[1]
    det = (a*d - b*c) % 27

    for i in range(1, 27):
        if (det * i) % 27 == 1:
            inv_det = i
            break

    chave_inv = [
        [(d * inv_det) % 27, (-b * inv_det) % 27],
        [(-c * inv_det) % 27, (a * inv_det) % 27]
    ]

    resultado = ''
    i = 0
    while i < len(texto_cifrado):
        a = texto_cifrado[i]
        b = texto_cifrado[i+1]
        va = alfabeto.index(a)
        vb = alfabeto.index(b)
        x = (chave_inv[0][0]*va + chave_inv[0][1]*vb) % 27
        y = (chave_inv[1][0]*va + chave_inv[1][1]*vb) % 27
        resultado += alfabeto[x] + alfabeto[y]
        i += 2
    return resultado


def menu():
    clear()
    print("**********MENU**********")
    print("1. Cadastrar parâmetros")
    print("2. Alterar parâmetros")
    print("3. Excluir parâmetros")
    print("4. Classificar sustentabilidade")
    print("0. Sair")
    print("************************")
    opcao = int(input("Escolha uma opção: "))
    if opcao <0 or opcao > 4:
        menu()
    else:
        return opcao
def perguntas():
    clear()
    dia = int(input("Dia de hoje (DD): "))
    mes = int(input("Mês de hoje (MM): "))
    ano = int(input("Ano de hoje (AAAA): "))
    date = f"{ano}-{mes:02d}-{dia:02d}"
    clear()
    water = float(input("Quantidade de água consumida hoje (aprx. em l): "))
    energy = float(input("Quantidade de energia consumida hoje (aprx.em kWh): "))
    waste = float(input("Quantidade de resíduos não recicláveis produzidos hoje (aprx. em kg): "))
    transport = 0
    transportCount = 0
    goodWaste = float(input("Porcentagem de resíduos recicláveis produzidos hoje (aprox. em %): "))
    clear()
    print("Meio(s) de transporte utilizados hoje (S (sim) ou N (não))")
    transportPublic = input("Transporte Público (ônibus, metrô, trem): ").upper()
    if transportPublic == "N" or transportPublic == "S":
        if transportPublic == "S":
            transportPublic = 3
            transport += 3
            transportCount += 1
        else:
            transportPublic = 0
    else:
        while not (transportPublic == 0 or transportPublic == 3):
            print("Valor inválido. Use somente S para sim, e N para não.")
            transportPublic = input("Transporte Público (ônibus, metrô, trem): ").upper()
            if transportPublic == "N" or transportPublic == "S":
                if transportPublic == "S":
                    transportPublic = 3
                    transport += 3
                    transportCount += 1
                else:
                    transportPublic = 0
    transportBike = input("Bicicleta: ").upper()
    if transportBike == "N" or transportBike == "S":
        if transportBike == "S":
            transportBike = 3
            transport += 3
            transportCount += 1
        else:
            transportBike = 0
    else:
        while not (transportBike == 0 or transportBike == 3):
            print("Valor inválido. Use somente S para sim, e N para não.")
            transportBike = input("Bicicleta: ").upper()
            if transportBike == "N" or transportBike == "S":
                if transportBike == "S":
                    transportBike = 3
                    transport += 3
                    transportCount += 1
                else:
                    transportBike = 0
    moonWalk = input("Caminhada: ").upper()
    if moonWalk == "N" or moonWalk == "S":
        if moonWalk == "S":
            moonWalk = 3
            transport += 3
            transportCount += 1
        else:
            moonWalk = 0
    else:
        while not (moonWalk == 0 or moonWalk == 3):
            print("Valor inválido. Use somente S para sim, e N para não.")
            moonWalk = input("Caminhada: ").upper()
            if moonWalk == "N" or moonWalk == "S":
                if moonWalk == "S":
                    moonWalk = 3
                    transport += 3
                    transportCount += 1
                else:
                    moonWalk = 0
    car = input("Carro: ").upper()
    if car == "N" or car == "S":
        if car == "S":
            car = 1
            transport += 1
            transportCount += 1
        else:
            car = 0
    else:
        while not (car == 0 or car == 1):
            print("Valor inválido. Use somente S para sim, e N para não.")
            car = input("Carro: ").upper()
            if car == "N" or car == "S":
                if car == "S":
                    car = 1
                    transport += 1
                    transportCount += 1
                else:
                    car = 0
    tesla = input("Carro elétrico: ").upper()
    if tesla == "N" or tesla == "S":   
        if tesla == "S":
            tesla = 3
            transport += 3
            transportCount += 1
        else:
            tesla = 0
    else:
        while not (tesla == 0 or tesla == 3):
            print("Valor inválido. Use somente S para sim, e N para não.")
            tesla = input("Carro elétrico: ").upper()
            if tesla == "N" or tesla == "S":
                if tesla == "S":
                    tesla = 3
                    transport += 3
                    transportCount += 1
                else:
                    tesla = 0
    uber = input("Carona compartilhada: ").upper()
    if uber == "N" or uber == "S":
        if uber == "S":
            uber = 1
            transport += 1
            transportCount += 1
        else:
            uber = 0
    else:
        while not (uber == 0 or uber == 1):
            print("Valor inválido. Use somente S para sim, e N para não.")
            uber = input("Carona compartilhada: ").upper()
            if uber == "N" or uber == "S":
                if uber == "S":
                    uber = 1
                    transport += 1
                    transportCount += 1
                else:
                    uber = 0
    clear()
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
        sustTransport = "Sem dados referentes ao uso de meios de transporte"
    else:
        avgSustTransport = round(transport/transportCount)
        if avgSustTransport == 3:
            sustTransport = "Alta Sustentabilidade"
        elif avgSustTransport == 1:
            sustTransport = "Baixa Sustentabilidade"
        else:
            sustTransport = "Moderada Sustentabilidade"
    #Criptografar
    sustWater = cript(sustWater)
    sustEnergy = cript(sustEnergy)
    sustWaste = cript(sustWaste)
    sustTransport = cript(sustTransport)
    #Inserir DB
    values = f"('{date}', {water}, {energy}, {waste}, {goodWaste}, {transportPublic}, {transportBike}, {moonWalk}, {car}, {tesla}, {uber})"
    cursor.execute(f"INSERT INTO dados (dia, Quantidade_de_Água_Consumida, Quantidade_de_Energia, Quantidade_de_Resíduo_Não_Reciclável, Porcentagem_de_Recicláveis, Meio_de_Transporte_Público, Meio_de_Transporte_Bicicleta, Meio_de_Transporte_Caminhada, Meio_de_Transporte_Carro, Meio_de_Transporte_Carro_Elétrico, Meio_de_Transporte_Carona_Compartilhada) values {values}")
    cursor.execute(f"insert into saídas (Sustentabilidade_Água, Sustentabilidade_Energia, Sustentabilidade_Lixo, Sustentabilidade_Transporte) values ('{sustWater}', '{sustEnergy}', '{sustWaste}', '{sustTransport}')")
    connect.commit()
    print("Parâmetros cadastrados com sucesso.")
def alterar(id):
    clear()
    transport = 0
    transportCount = 0
    print("Qual parâmetro você deseja alterar?")
    print("1. Consumo de Água")
    print("2. Consumo de Energia")
    print("3. Produção de Resíduos")
    print("4. Produção de Resíduos Recicláveis")
    print("5. Uso de Transportes")
    print("0. Voltar")
    opcao = int(input("Escolha uma opção: "))
    if opcao < 0 or opcao > 5:
        print("Opção inválida. Tente novamente.")
        alterar(id)
    if opcao == 0:
        return
    if opcao == 1:
        clear()
        water = float(input("Digite o novo valor de consumo de água (em L): "))
        if water < 150:
            sustWater = "Alta Sustentabilidade"
        elif water > 200:
            sustWater = "Baixa Sustentabilidade"
        else:
            sustWater = "Moderada Sustentabilidade"
        cursor.execute(f"UPDATE dados SET Quantidade_de_Água_Consumida = {water} WHERE id = {id}")
        cursor.execute(f"UPDATE saídas SET Sustentabilidade_Água = '{cript(sustWater)}' WHERE id = {id}")
        connect.commit()
        print("Consumo de água atualizado com sucesso.")
    if opcao == 2:
        clear()
        energy = float(input("Digite o novo valor de consumo de energia (em kWh): "))
        if energy < 5:
            sustEnergy = "Alta Sustentabilidade"
        elif energy > 10:
            sustEnergy = "Baixa Sustentabilidade"
        else:
            sustEnergy = "Moderada Sustentabilidade"
        cursor.execute(f"UPDATE dados SET Quantidade_de_Energia = {energy} WHERE id = {id}")
        cursor.execute(f"UPDATE saídas SET Sustentabilidade_Energia = '{cript(sustEnergy)}' WHERE id = {id}")
        connect.commit()
        print("Consumo de energia atualizado com sucesso.")
    if opcao == 3:
        clear()
        waste = float(input("Digite o novo valor de produção de resíduos (em kg): "))
        cursor.execute(f"UPDATE dados SET Quantidade_de_Resíduo_Não_Reciclável = {waste} WHERE id = {id}")
        connect.commit()
        print("Produção de resíduos atualizada com sucesso.")
    if opcao == 4:
        clear()
        goodWaste = float(input("Digite o novo valor de produção de resíduos recicláveis (em %): "))
        if goodWaste > 50:
            sustWaste = "Alta Sustentabilidade"
        elif goodWaste < 20:
            sustWaste = "Baixa Sustentabilidade"
        else:
            sustWaste = "Moderada Sustentabilidade"
        cursor.execute(f"UPDATE dados SET Porcentagem_de_Recicláveis = {goodWaste} WHERE id = {id}")
        cursor.execute(f"UPDATE saídas SET Sustentabilidade_Lixo = '{cript(sustWaste)}' WHERE id = {id}")
        connect.commit()
        print("Produção de resíduos recicláveis atualizada com sucesso.")
    if opcao == 5:
        clear()
        print("Meio(s) de transporte utilizados (S (sim) ou N (não))")
        transportPublic = input("Transporte Público (ônibus, metrô, trem): ").upper()
        if transportPublic == "N" or transportPublic == "S":
            if transportPublic == "S":
                transportPublic = 3
                transport += 3
                transportCount += 1
            else:
                transportPublic = 0
        else:
            while not (transportPublic == "N" or transportPublic == "S"):
                print("Valor inválido. Use somente S para sim, e N para não.")
                transportPublic = input("Transporte Público (ônibus, metrô, trem): ").upper()
        transportBike = input("Bicicleta: ").upper()
        if transportBike == "N" or transportBike == "S":
            if transportBike == "S":
                transportBike = 3
                transport += 3
                transportCount += 1
            else:
                transportBike = 0
        else:
            while not (transportBike == "N" or transportBike == "S"):
                print("Valor inválido. Use somente S para sim, e N para não.")
                transportBike = input("Bicicleta: ").upper()
        moonWalk = input("Caminhada: ").upper()
        if moonWalk == "N" or moonWalk == "S":
            if moonWalk == "S":
                moonWalk = 3
                transport += 3
                transportCount += 1
            else:
                moonWalk = 0
        else:
            while not (moonWalk == "N" or moonWalk == "S"):
                print("Valor inválido. Use somente S para sim, e N para não.")
                moonWalk = input("Caminhada: ").upper()
        car = input("Carro: ").upper()
        if car == "N" or car == "S":
            if car == "S":
                car = 1
                transport += 1
                transportCount += 1
            else:
                car = 0
        else:
            while not (car == "N" or car == "S"):
                print("Valor inválido. Use somente S para sim, e N para não.")
                car = input("Carro: ").upper()
        tesla = input("Carro elétrico: ").upper()
        if tesla == "N" or tesla == "S":   
            if tesla == "S":
                tesla = 3
                transport += 3
                transportCount += 1
            else:
                tesla = 0
        else:
            while not (tesla == "N" or tesla == "S"):
                print("Valor inválido. Use somente S para sim, e N para não.")
                tesla = input("Carro elétrico: ").upper()
        uber = input("Carona compartilhada: ").upper()
        if uber == "N" or uber == "S":
            if uber == "S":
                uber = 1
                transport += 1
                transportCount += 1
            else:
                uber = 0
        else:
            while not (uber == "N" or uber == "S"):
                print("Valor inválido. Use somente S para sim, e N para não.")
                uber = input("Carona compartilhada: ").upper
        if transportCount == 0:
            sustTransport = "Sem dados referentes ao uso de meios de transporte"
        else:
            avgSustTransport = round(transport/transportCount)
            if avgSustTransport == 3:
                sustTransport = "Alta Sustentabilidade"
            elif avgSustTransport == 1:
                sustTransport = "Baixa Sustentabilidade"
            else:
                sustTransport = "Moderada Sustentabilidade"
        cursor.execute(f"UPDATE dados SET Meio_de_Transporte_Público = {transportPublic}, Meio_de_Transporte_Bicicleta = {transportBike}, Meio_de_Transporte_Caminhada = {moonWalk}, Meio_de_Transporte_Carro = {car}, Meio_de_Transporte_Carro_Elétrico = {tesla}, Meio_de_Transporte_Carona_Compartilhada = {uber} WHERE id = {id}")
        cursor.execute(f"UPDATE saídas SET Sustentabilidade_Transporte = '{cript(sustTransport)}' WHERE id = {id}")
        connect.commit()
        print("Meios de transporte atualizados com sucesso.")
def mostrar_dados(date):
    clear()
    cursor.execute("use sustentabilidade")
    cursor.execute("select * from dados")
    for dados in cursor.fetchall():
        if str(dados[1]) == date:
            print('####################')
            print(f'ID: {dados[0]}')
            print(f'Data: {dados[1]}')
            print(f'Consumo de Água: {dados[2]}L')
            print(f'Consumo de Energia: {dados[3]}KWh')
            print(f'Produção de Resíduos: {dados[4]}kg')
            print(f'Produção de Resíduos Recicláveis: {dados[5]}%')
            print(f'Uso de Transporte Público: {ajuste_transporte(dados[6])}')
            print(f'Uso de Bicicleta: {ajuste_transporte(dados[7])}')
            print(f'Uso de Caminhada: {ajuste_transporte(dados[8])}')
            print(f'Uso de Carro: {ajuste_transporte(dados[9])}')
            print(f'Uso de Carro Elétrico: {ajuste_transporte(dados[10])}')
            print(f'Uso de Carona Compartilhada: {ajuste_transporte(dados[11])}')
            return True
def mostrar_dados_id(id):
    cursor.execute("use sustentabilidade")
    cursor.execute("select * from dados")
    for dados in cursor.fetchall():
        if dados[0] == id:
            print(f'ID: {dados[0]}')
            print(f'Data: {dados[1]}')
            print(f'Consumo de Água: {dados[2]}L')
            print(f'Consumo de Energia: {dados[3]}KWh')
            print(f'Produção de Resíduos: {dados[4]}kg')
            print(f'Produção de Resíduos Recicláveis: {dados[5]}%')
            print(f'Uso de Transporte Público: {ajuste_transporte(dados[6])}')
            print(f'Uso de Bicicleta: {ajuste_transporte(dados[7])}')
            print(f'Uso de Caminhada: {ajuste_transporte(dados[8])}')
            print(f'Uso de Carro: {ajuste_transporte(dados[9])}')
            print(f'Uso de Carro Elétrico: {ajuste_transporte(dados[10])}')
            print(f'Uso de Carona Compartilhada: {ajuste_transporte(dados[11])}')
def classificar():
    clear()
    mediaTransporteFinal = 0
    transporteCount = 0
    cursor.execute("use sustentabilidade")
    cursor.execute("select * from saídas")
    for dados in cursor.fetchall():
        print('####################')
        mostrar_dados_id(dados[0])
        print('--------')
        print(f'Sustentabilidade da Água: {decript(dados[1])}')
        print(f'Sustentabilidade da Energia: {decript(dados[2])}')
        print(f'Sustentabilidade do Lixo: {decript(dados[3])}')
        print(f'Sustentabilidade do Transporte: {decript(dados[4])}')
    cursor.execute("select * from dados")
    for dados in cursor.fetchall():
        for count in range (6, 12):
            if int(dados[count]) > 0:
                mediaTransporteFinal += int(dados[count])
                transporteCount += 1
        #Médias
    cursor.execute("select avg(Quantidade_de_Água_Consumida), avg(Quantidade_de_Energia), avg(Porcentagem_de_Recicláveis) from dados")
    mediaAgua, mediaEnergia, mediaReciclaveis = cursor.fetchone()
    print('####################')
    print('####################')
    print(f'Média de Consumo de Água: {mediaAgua:.2f}L')
    print(f'Média de Consumo de Energia: {mediaEnergia:.2f}KWh')
    print(f'Média de Resíduos Recicláveis: {mediaReciclaveis:.2f}%')
    if mediaAgua < 150:
        sustAgua = "ALTA SUSTENTABILIDAD"
    elif mediaAgua <= 200:
        sustAgua = "MÉDIA SUSTENTABILIDADE"
    else:
        sustAgua = "BAIXA SUSTENTABILIDADE"

    if mediaEnergia < 5:
        sustEnergia = "ALTA SUSTENTABILIDADE"
    elif mediaEnergia <= 10:
        sustEnergia = "MÉDIA SUSTENTABILIDADE"
    else:
        sustEnergia = "BAIXA SUSTENTABILIDADE"

    if mediaReciclaveis > 50:
        sustReciclaveis = "ALTA SUSTENTABILIDADE"
    elif mediaReciclaveis >= 20:
        sustReciclaveis = "MÉDIA SUSTENTABILIDADE"
    else:
        sustReciclaveis = "BAIXA SUSTENTABILIDADE"

    if transporteCount == 0:
        sustTransporte = 0
    else:
        sustTransporte = round(mediaTransporteFinal/transporteCount)
    if sustTransporte == 3:
        sustTransporte = "ALTA SUSTENTABILIDADE"
    elif sustTransporte == 1:
        sustTransporte = "BAIXA SUSTENTABILIDADE"
    elif sustTransporte == 2:
        sustTransporte = "MÉDIA SUSTENTABILIDADE"
    else:
        sustTransporte = "SEM DADOS REFERENTES AO USO DE MEIOS DE TRANSPORTE"
    cursor.execute("select count(*) from dados")
    total = cursor.fetchone()[0]

    print('####################')
    print(f'Classificação média de Água: {sustAgua}')
    print(f'Classificação média de Energia: {sustEnergia}')
    print(f'Classificação média de Resíduos: {sustReciclaveis}')
    print(f'Classificação média de Transporte: {sustTransporte}')

#Código
while continuar:
    opcao = menu()
    if opcao == 0:
        continuar = False
        clear()
        print("Sistema encerrado. Obrigado por usar.")
    if opcao == 1:
        perguntas()
        input("Pressione Enter para continuar...")
    if opcao == 2:
        clear()
        print("Digite a data do parâmetro que deseja alterar: ")
        dia = int(input("Dia (DD): "))
        mes = int(input("Mês (MM): "))
        ano = int(input("Ano (AAAA): "))
        date = f"{ano}-{mes:02d}-{dia:02d}"
        if mostrar_dados(date) is True:
            mostrar_dados(date)
            print('####################')
            id = input("Digite o ID do parâmetro que deseja alterar: ")
            alterar(id)
        else:
            print("Nenhum dado encontrado para a data informada.")
        input("Pressione Enter para continuar...")
    if opcao == 3:
        clear()
        excluir = True
        print("Digite a data do parâmetro que deseja excluir: ")
        dia = int(input("Dia (DD): "))
        mes = int(input("Mês (MM): "))
        ano = int(input("Ano (AAAA): "))
        date = f"{ano}-{mes:02d}-{dia:02d}"
        if mostrar_dados(date) is True:
            mostrar_dados(date)
            print('####################')
            id = input("Digite o ID do parâmetro que deseja excluir: ")
            while excluir:
                escolha = input("Tem certeza que deseja excluir? (S/N): ").upper()
                if escolha == "S":
                    cursor.execute(f"DELETE FROM dados WHERE id = {id}")
                    cursor.execute(f"DELETE FROM saídas WHERE id = {id}")
                    connect.commit()
                    print("Parâmetro excluído com sucesso.")
                    excluir = False
                elif escolha == "N":
                    print("Parâmetro não excluído.")
                    excluir = False
                else:
                    print("Escolha inválida. Tente novamente.")
        else:
            print("Nenhum dado encontrado para a data informada.")
        input("Pressione Enter para continuar...")
    if opcao == 4:
        classificar()
        input("Pressione Enter para continuar...")