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

    def esPalindromo(cadena):
        principio = 0
        final = len(cadena)

        while cadena[principio] == cadena[final]:
            if principio >= final:
                return True
            principio += 1
            final -= 1
        return False

