from telnetlib import PRAGMA_HEARTBEAT


cadena_alfanumerica = "lk45ih3E84ku34zs923dfgf72";
cantidad = len(cadena_alfanumerica);
cadena = "";
mitad1 = "";
mitad2 = "";

for i in range (cantidad):
    if cadena_alfanumerica[i].isalpha():
        cadena += cadena_alfanumerica[i];

    elif cadena_alfanumerica[i].isdigit() and i < 13:
        mitad1 += cadena_alfanumerica[i];


    elif cadena_alfanumerica[i].isdigit() and i > 12:
        mitad2 += cadena_alfanumerica[i];

print(
    sorted(
        cadena.split()
    )
);

resultado = int(mitad1) + int(mitad2);
print(f"El resultado esperado: suma de numero = {resultado}");