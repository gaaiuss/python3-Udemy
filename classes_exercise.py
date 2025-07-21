# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer


class Engine:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Manufacturer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


fusca = Car('Fusca')
motor_V8 = Engine('Motor V8')
wolkswagen = Manufacturer('Wolkswagen')

fusca.engine = motor_V8
fusca.manufacturer = wolkswagen
print(fusca.name, fusca.manufacturer.name, fusca.engine.name)
