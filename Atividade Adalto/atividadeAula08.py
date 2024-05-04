from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Categoria: {self.categoria.nome}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Categoria: {self.categoria.nome}, Potência da Fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        pass
    
class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def cadastrar(self):
        pass

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Categoria: {self.categoria.nome}, Tempo de Bateria: {self.__tempoDeBateria}"

    # Getter e Setter para tempoDeBateria
    def get_tempoDeBateria(self):
        return self.__tempoDeBateria

    def set_tempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

# Testando o código
if __name__ == "__main__":
    # Criando uma categoria
    categoria1 = Categoria(1, "Eletrônicos")

    # Criando um desktop
    desktop1 = Desktop("Desktop Modelo X", "Preto", 1500, categoria1, "500W")

    # Criando um notebook
    notebook1 = Notebook("Notebook Modelo Y", "Prata", 2000, categoria1, "8 horas")

    # Testando os métodos getInformacoes()
    print(desktop1.getInformacoes())
    print(notebook1.getInformacoes())

    # Testando o setter de Notebook
    notebook1.set_tempoDeBateria("10 horas")
    print(notebook1.getInformacoes())
