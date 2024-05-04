from atividadeAula08 import Categoria, Desktop, Notebook

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
