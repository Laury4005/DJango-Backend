import numpy as np

# Definir número de medidores y días
num_medidores = 15
num_dias = 15

# Crear matriz de datos
datos = np.random.randint(0, 10, size=(num_medidores, num_dias))

# Imprimir tabla
print("012024\t" + "\t".join([f"Día {i+1}" for i in range(num_dias)]))
for i in range(num_medidores):
    fila = [str(valor) if valor != 0 else "-" for valor in datos[i]]
    print(f"Med{i+1}\t" + "\t".join(fila))

