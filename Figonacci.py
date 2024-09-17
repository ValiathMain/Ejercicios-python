"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
 """

def figonacci():
    num1,num2 = 0,1
    numeros = 0

    while numeros < 50:
        num1, num2 = num2, num1 + num2
        print(num1)
        numeros += 1

print(figonacci())
