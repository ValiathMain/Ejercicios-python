"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 """

def anagrama_sin_input(anagrama1,anagrama2):
    return sorted(anagrama1.lower()) == sorted(anagrama2.lower())

print(anagrama_sin_input("Roma","Amor"))
print(anagrama_sin_input("Amiga","Magia"))
print(anagrama_sin_input("Caza","Casa"))

# version con un input y finalisa con un string en lugar de un true o false

def anagrama_con_input(anagrama3,anagrama4):
    if sorted(anagrama3.lower()) == sorted(anagrama4.lower()):
        print(f"{anagrama3} y {anagrama4} son anagramas")
        return True
    else:
        print(f"{anagrama3} y {anagrama4} no son anagramas")
        return False

anagrama3 = str(input("inserte el primer anagrama:"))
anagrama4 = str(input("inserte el segundo anagrama:"))

anagrama_con_input(anagrama3, anagrama4)
