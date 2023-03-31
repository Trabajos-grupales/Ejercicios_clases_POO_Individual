
''''''''''''''''
Enunciado: en esta misma clase Palindromo, añada un atributo que se inicializará en el constructor. Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia, muestre el atributo en mayúsculas.

Comportamiento esperado:

p = Palindromo("radar")
print(p.test())
>>> True
p = Palindromo("sonar")
>>> RADAR
print(p.test())
>>> False
SONAR
Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")?
'''''''''

class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena
        