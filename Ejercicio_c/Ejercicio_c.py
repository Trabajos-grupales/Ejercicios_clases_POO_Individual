class A:
    def z(self):
        return self

    def y(self, t):
        return len(t) # y siempre hará referencia a la longitud, en este ejercicio serán el número de elementos

a = A
y = a.z
print(y(a)) # devuelve <class '__main__.A'>, que es el tipo de la clase A
aa = a()
print(aa is a()) # a pesar de que iguala un elemento a otro, no son el mismo, porque son dos instancias distintas, por lo que devuelve False
z = aa.y
print(z(())) # el método z no tiene elementos, más que el self, y tampoco añade nada, así que lo que printa es 0
print(a().y((a,))) # el método y hace referencia a un elemento, que es una tupla, y devuelve 1
print(A.y(aa, (a,z))) # en este caso el método y hace referencia primero a la tupla, otra vez, y después al método z, por tanto hace referencia a dos elementos, y devuelve 2
print(aa.y((z,1,'z'))) # en este caso el método y cuenta el método z, el número 1 y la letra z, por tanto devuelve 3