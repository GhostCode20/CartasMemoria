from tabulate import tabulate

# Crear una lista de listas con datos
data = [['Juan', 25, 'Madrid'],
        ['María', 30, 'Barcelona'],
        ['Pedro', 35, 'Sevilla']]

# Imprimir la tabla
print(tabulate(data, headers=['Nombre', 'Edad', 'Ciudad']))
