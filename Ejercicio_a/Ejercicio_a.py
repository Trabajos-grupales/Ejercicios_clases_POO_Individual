''''''''''''''''
a. Palíndromo - método de clase
Enunciado: crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

Comportamiento esperado:

print(Palindromo.esPalindromo('radar'))
>>> True
print(Palindromo.esPalindromo('sonar'))
>>> False
print(Palindromo.esPalindromo('Arde ya la yedra'))
>>> False
print(Palindromo.esPalindromo('Ardeyalayedra'))
>>> True
print(Palindromo.esPalindromo('!@#$% %$#@!'))
>>> True
print(Palindromo.esPalindromo('L O L'))
>>> True
'''''''''''''''''

class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena

    @classmethod
    def esPalindromo(cls, cadena):
        principio = 0 # posición inicial que irá avanzando mientras sean iguales los caracteres
        final = len(cadena) # longitud de la cadena de caracetres
        cadena = cadena.lower() # convierte a minúsculas

        while cadena == cadena[::-1]:
            if principio >= final:
                return True
            principio += 1
            final -= 1
        return False

print(Palindromo.esPalindromo('radar'))
print(Palindromo.esPalindromo('sonar'))
print(Palindromo.esPalindromo('Arde ya la yedra'))
print(Palindromo.esPalindromo('Ardeyalayedra'))
print(Palindromo.esPalindromo('!@#$% %$#@!'))
print(Palindromo.esPalindromo('L O L'))
