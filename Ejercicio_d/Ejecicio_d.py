class Logger:
    def __init__(self, archivo):
        self.contador = 0
        self.archivo = archivo
        with open(self.archivo, "w") as log:
            log.write("--Start log--\n")
    def log(self, mensaje):
        with open(self.archivo, "a") as log:
            self.contador += 1
            log.write(f"{self.contador}: {mensaje}\n")
    def __del__(self):
        with open(self.archivo, "a") as log:
            log.write("--End log--\n")

class Test(Logger):
    def __init__(self, archivo):
        super().__init__('log.txt')
    def test(self, mensaje):
        self.log(mensaje)