"""
Segue abaixo programa de criptografia e descriptografia desenvolvido pelo grupo. A estrutura do programa foi desenvolvida em funções,
sendo cada uma responsável por uma determinada parte do algoritimo. As funçõs foram dividas na seguinte ordem:

Função de Opção do Usuário = def determinaOpcao()

Função de Checagem dos parametros de mensagem = def verifica_mensagem()

Função de checagem dos parametros de segurança da chave = def verifica_chave()

Função responsável pela criptografia de mensagens = def criptografia()

Função responsável pela descriptografia de mensagens = def descriptografia()

Função respnsável pela verificação da vontade do usuário de seguir na utilização do programa ou terminá-la = def encerrar()

Função responsável por toda a execução do algoritimo = def execucao()
"""

import random as rd
import datetime as dt
import time as tm

def determinadaOpcao():
    # Função defeinida, afim de facilitar a escolha do usuário para criptografia ou descriptografia, tendo em visita que um usuário pode abrir o programa apenas para descriptografar uma mensagem.

    while True:
        opcao = input("Deseja criptografar ou descriptogragar a mensagem ?: (C / D): ").upper()
        if opcao in "CRIPTOGRAFAR C DESCRIPTOGRAFAR D".split():
            return opcao
        else:
            print('Digite "C" ou "D".')

def verifica_mensagem():

    """"Função desenvolvida com o objetivo de realizar todas a checagens da mensgem inserida pelo usuário, afim de
        orientá-lo no envio correto da mensagem, conforme padrão definido abaixo, fazendo com que não prossiga até que
        insira a mensagem corretamente."""

    while True:
        mensagem1 = input("Digite sua mensagem: ")

        if len(mensagem1) <= 128:
            return mensagem1
        else:
            print("A mensagem a ser criptografada deve conter no máximo 128 caracteres!")

def verifica_chave():

    """ Função desenvolvida com o objetivo de guiar o usuário a definir uma chave forte, afim de evitar que o mesmo
        continue com uma senha fraca para sua própria segurança e segurança do sistema.

        Essa função também é responsável por garantir um certo respaldo ao usuário em não definir chaves fracas, com
        baixa segurança na criptografia"""

    while True:
        chave = input("*OBS:(Para maiores seguranças digite ao menos 4 letras e 6 números)*\n \nDigite a chave: ")
        lista_verificadora = []
        defina_zero = len(chave)
        numeros = ''
        letras = ''
        calculo_letras = 0
        calculo_numeros = 0
        contador_letra = 0
        contador_numero = 0
        for caracter in chave:
            lista_verificadora.append(caracter)
        for numero in lista_verificadora:
            if numero.isalpha() == True and numero != '0':
                passo1 = ord(numero)
                passo2 = str(passo1)
                letras += passo2
            elif numero.isnumeric() == True and numero != '0':
                numeros += numero
            else:
                if numero == '0':
                    numero_zero = str(defina_zero)
                    numeros += numero_zero

        for numero in numeros:
            if contador_numero == 0:
                passo1 = int(numero)
                calculo_numeros += passo1
                contador_numero += 1
            else:
                passo1 = int(numero)
                calculo_numeros *= passo1

        for letra in letras:
            if contador_letra == 0:
                passo1 = int(letra)
                calculo_letras += passo1
                contador_letra += 1
            else:
                passo1 = int(letra)
                calculo_letras += passo1
        if calculo_letras == 0:
            print('Digite no mínimo 1 *LETRAS*')
        elif calculo_numeros == 0:
            print('Digite no mínimo 1 *NÚMEROS*')
        else:
            calculo_de_chave = (calculo_letras) * (calculo_numeros) * (defina_zero)
            return calculo_de_chave

def simbolos():

    separador = ['@', '&', '-', '_', '!', '$', '¨','a','A','z','Z','g','G','u','U']
    aleatorio = rd.randint(0, 13)
    simbolo = separador[aleatorio]
    return simbolo

def criptografia():

    mensagem = verifica_mensagem()
    chave = verifica_chave()
    msg_criptografada = ""
    # Variável responsavel por concatenar os números e formar o código criptografado

    for letra in mensagem:
    # Para cada letra que contem na mensagem, faça:
        if letra == " ":
            # Se o caracter for igual a espaço, então:
            msg_criptografada += '(@'
            # Adicionar o símbolo ( mais o símbolo de vírgula.

        else:
        # Se a variável não for espaço, então:
            passo1 = ord(letra)
            # Variável responsavel por receber a letra trasformada em número OBS(Ela ainda está em string)
            passo2 = int(passo1)
            # Trasformando a variável passo1 em Inteiro
            passo3 = passo2 * chave
            # Variável recebendo o valor da multiplicação das variáveis DIG e Passo2
            passo4 = str(passo3)
            # Trasformando a variável passo3 em string novamente
            msg_criptografada += passo4
            # Concatenando o valor da variável passo4 com valores anteriores.
            # Após concatenar o numero
            msg_criptografada += simbolos()
    print("Criptografando sua mensagem...\n")
    tm.sleep(2)
    print(f"Sua mensagem criptografada é: {msg_criptografada}")
    tm.sleep(0.5)
    # Mostrando mensagem criptografada

def descriptografia():

    """Neste ponto não foi utilizado a checagem de mensagem, pois quando a mensagem é criptografada, seu tamanho pode ser superior aos 128 caracteres.
        Ação realizada intencionalmente, pois assim torna a mensagem criptografada ainda mais dificil de decodificar por um invasor ou pessoa indesejável """
    #Primeira Etapa:

    mensagem = input("Digite a mensagem que deseja descriptografar: ")
    concat_numeros = ""
    # Variável responsavel por concatenar os números, espaços e vírgulas.
    for numero in mensagem:
    # Para cada número que contem na mensagem, faça:
        if numero in "@ & - _ ! $ ¨ a A z Z g G u U":
        # Se numero for igual a estes símbolos, então:
            concat_numeros += ","
            # Concatenar ","
        elif numero == '(':
            # Se numero for igual a ( então:
            concat_numeros += ' ,'
            # Concatenar espaço, ou seja " ,"

        else:
        # Se a variável não for nenhum destes símbolos, então:
            concat_numeros += numero
            # Concatenar numero

    #Segunda Etapa:

    lista = concat_numeros.split(',')
    # Transformando a variável de concatenação em lista OBS(Separando por vírgula) lista = [97, ,97]
    chave = verifica_chave()
    msg_final = ""
    # Variável responsavel por concatenar as letras e os espaços e assim formando as frases.
    for numero in lista:
    # Para cada numero ou espaço que estiver em lista, faça:
        if numero == ' ' or numero == '':
        # Se numero for igual a espaço ou vazio, então:
            if numero == '':
            # Se numero for igual vazio, então:
                msg_final += ''
                # Concatenar nada
            if numero == ' ':
            # Se numero for igual espaço, então:
                msg_final += ' '
                # Concatenar espaço

        else:
        # Se a variável não estiver dentro deste dois parâmetros, então:
            passo1 = int(numero)
            # Variável responsavel por receber o número e trasformado em inteiro.
            passo2 = int(passo1 / chave)
            # Variável responsavel por receber valor da divisão das variáveis Chave e passo1 e transformado em inteiro.
            passo3 = chr(passo2)
            # Variável responsavel por receber o valor de passo2 e trasformar em letra.
            msg_final += passo3
            # Concatenando as letras

    print('Decifrando sua mensagem...')
    tm.sleep(2)
    msg_descripto = print(f"Sua mensagem descriptografada é: '{msg_final}' ")
    # mostrando mensagem descriptografada

def encerrar():

    """Função desenvolvida para permitir que o usuário possa encerrar o programa, sem a necessidade de forçar sua parada."""

    while True:
        parar = input("Deseja encerrar a sessão? (SIM/NÃO): ").upper()
        if parar in "SIM S NÃO N".split():
            return parar
        else:
            print("ERRO! Você deve digitar SIM ou NÃO")

def execucao():

    """ Função responsável por toda a execução do progarama em ordem.
        Criado para manter um loop, permitindo que o usuário constantemente possa criptografar e descriptografar
        mensagens, sem a necessidade de reinicializar o sistema a cada uso."""

    Controlador = 0
    opcao = determinadaOpcao()
    if opcao[0] == "C":
        criptografia()
    elif opcao[0] == "D":
        descriptografia()
    while Controlador < 1:
        parar = encerrar()
        if parar[0] == "N":
            execucao()
        else:
            print("sessão encerrada. Obrigado por utilizar nosso programa :)")
            Controlador += 1
try:
    execucao()
except KeyboardInterrupt:
    print("\n\nERRO! O USUARIO INTERROMPEU A EXECUÇÃO")
except ValueError:
    print("ERRO! HÁ ALGO DE ERRADO NA CHAVE")