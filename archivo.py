# Define una variable de cada tipo de primitivo
num = 4
flotante = 3.14
mayor_de_edad = True
cadena = "si es mayor de edad: "

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concatenar = cadena + " " + str(num) + " " + str(mayor_de_edad) + " " + str(flotante)
print(concatenar)

# Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
# Límite de enteros
# 9223372036854775807

# Límite de flotantes
# 1.7976931348623157e+308

#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = 20
resultado = 0
for i in range(2,n+1,2):
    resultado += i
print(resultado)



