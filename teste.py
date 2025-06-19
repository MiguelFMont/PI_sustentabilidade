
alfabeto = ['Z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
chave = [[4, 3],[1, 2]]


def cript(texto):
    texto = texto.upper()

    if texto.find(' ') != -1:
        texto = texto.replace(' ', '')
    
        
    if len(texto) % 2 != 0:
        texto += ' '
    resultado = ""

    for i in range(0, len(texto), 2):
        a = alfabeto.index(texto[i])
        b = alfabeto.index(texto[i + 1])
        x = (chave[0][0]*a + chave[0][1]*b) % 26
        y = (chave[1][0]*a + chave[1][1]*b) % 26
        resultado += alfabeto[x] + alfabeto[y]
        
    return resultado

def decript(texto_cifrado):
    # Inverso da matriz mod 26
    a, b = chave[0]
    c, d = chave[1]
    det = (a*d - b*c) % 26

    for i in range(1, 26):
        if (det * i) % 26 == 1:
            inv_det = i
            break

    chave_inv = [
        [(d * inv_det) % 26, (-b * inv_det) % 26],
        [(-c * inv_det) % 26, (a * inv_det) % 26]
    ]

    resultado = ''
    i = 0
    while i < len(texto_cifrado):
        a = texto_cifrado[i]
        b = texto_cifrado[i+1]
        va = alfabeto.index(a)
        vb = alfabeto.index(b)
        x = (chave_inv[0][0]*va + chave_inv[0][1]*vb) % 26
        y = (chave_inv[1][0]*va + chave_inv[1][1]*vb) % 26
        resultado += alfabeto[x] + alfabeto[y]
        i += 2
    return resultado
print(f'Deseja criptografar ou decriptografar um texto?')
print(f'1 - Criptografar')
print(f'2 - Decriptografar')
opcao = input("Digite 1 ou 2: ")
if opcao == '1':
    print("Você escolheu criptografar.")
    texto = input("Digite o texto a ser criptografado: ")
    texto_criptografado = cript(texto)
    print("Texto criptografado:", texto_criptografado)
    texto_decriptografado = decript(texto_criptografado)
    print("Texto decriptografado:", texto_decriptografado)
else:
    print("Você escolheu decriptografar.")
    texto = input("Digite o texto a ser decriptografado: ")
    texto_decriptografado = decript(texto)
    print("Texto decriptografado:", texto_decriptografado)
    texto_criptografado = cript(texto_decriptografado)
    print("Texto criptografado:", texto_criptografado)

