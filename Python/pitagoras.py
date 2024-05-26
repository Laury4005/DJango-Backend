def print_triangulo(n):
    """
    Imprime un triángulo de altura 'n' centrado en la pantalla.
    """
    for i in range(1, n + 1):
        espacios = " " * (n - i)  # Calcula los espacios en blanco antes de los asteriscos
        asteriscos = "*" * (2 * i - 1)  # Calcula los asteriscos en esta línea
        print(espacios + asteriscos)

# Llama a la función para imprimir un triángulo centrado con una altura de 5
print_triangulo(5)
