import enum, sys

class Lexico:
    def __init__(self, fuente):
        #Se pasa el código fuente como cadena. Se le agrega newline para simplificar el análisis para el último token/sentencia.
        self.fuente = fuente + '\n'
        self.carActual = ''     #Caracter actual en la cadena.
        self.posActual = -1     #Posición actual en la cadena.
        self.siguiente()

    #Leer el siguiente caracter.
    def siguiente(self):
        pass

    #Regresar el caracter adelante (lookahead).
    def asomar(self): #NO guarda los cambios
        pass
    
    #Token inválido, imprimir error y salir.
    def abortar(self, mensaje):
        sys.exit("Error léxico: " + mensaje)

    #Saltar espacios, \t y \r, pero no \n, estas se utilizarán para indicar el final de una sentencia.
    def saltarEspacios(self):
        pass

    #Saltar comentarios en el código.	
    def saltarComentarios(self):
        pass
    
    #Regresar el siguiente token.
    def getToken(self):
        self.saltarEspacios()
        self.saltarComentarios()
        token = None #Var auxiliar

        if self.carActual == '+':
            pass
        
        elif self.carActual == '-':
            pass
        
        elif self.carActual == '*':
            pass
        
        elif self.carActual == '/':
            pass
        
        elif self.carActual == '\0':
            pass
        
        elif self.carActual == '\n':
            pass
        
        elif self.carActual == '=':
            pass
        
        elif self.carActual == '<':
            pass
        
        elif self.carActual == '>':
            pass
        
        elif self.carActual == '!':
            pass
        
        elif self.carActual.isdigit(): #Numeros
            pass
        
        elif self.carActual == '\"': #Strings
            pass
        
        #Los ID empiezan SIEMPRE con letra, luego pueden ser seguidos de numeros y letras
        elif self.carActual.isalpha(): #Keywords e identificadores
            pass
        
        #--------------Token desconocido--------------
        else:
            self.abortar("El lexema '" + self.carActual + "' es desconocido :(")
        
        #Si ya se identificó el token, debemos leer el siguiente car[acter]
        self.siguiente() 
        return token

class Token:
    def __init__(self, lexema, token):
        self.lexema = lexema #text
        self.token = token #TipoToken ENUM tipo
    
    @staticmethod
    def revisarSiEsKeyword(lexema):
        #Usar la enum: TipoToken.name (nombre); TipoToken.value (numeros)
        for tipo in TipoToken:
            if tipo.name == lexema and tipo.value > 100 and tipo.value < 200:
                return tipo
        return None


class TipoToken(enum.Enum):
    EOF = -1 #End of file \0
    NEWLINE = 0 #\n
    NUMERO = 1
    ID = 2
    STRING = 3
    
    #Keywords 100>, pero <200
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    
    #Operadores
    EQ = 201 #=
    PLUS = 202 #+
    MINUS = 203 #-
    ASTERISK = 204 #*
    SLASH = 205 #/
    EQEQ = 206 #==
    NOTEQ = 207 #!=
    LT = 208 #<
    LTEQ = 209 #<=
    GT = 210 #>
    GTEQ = 211 #>=  