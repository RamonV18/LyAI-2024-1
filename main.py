from lexico import *
import sys

def main():
    print("---CompiladorCITO---")

    if len(sys.argv) != 2:
        sys.exit("Error: Se necesita un archivo fuente para compilar.")
    with open(sys.argv[1], 'r') as archivo:
        fuente = archivo.read()

    print("\nLista de tokens identificados:")
    lexico = Lexico(fuente) #Análisis léxico
    token = lexico.getToken()

    #Siempre y cuando no sea EOF, continuar leyendo tokens
    while token.token != TipoToken.EOF:
        print(token.token)
        token = lexico.getToken()

main()