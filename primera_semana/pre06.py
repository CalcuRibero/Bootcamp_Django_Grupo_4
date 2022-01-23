# pregunta06
# De este arquitecto de persona,  crear por lo menos 3 personas
# Pedir los datos por consola(añadir cada persona a un alista , para evitar
# que al sobreescribir los datos se pierdan)

persona = {
    "nombre": None,
    "apellido": None,
    "ciudad": None,
    "lenguajes_programacion": []
}

persona["nombre"] = ["Luis", "Juan", "Gonzalo"]
persona["apellido"] = "aaa", "bbb", "ccc"
persona["ciudad"] = "Bogotá", "Buenos Aires", "Lima"
persona["lenguajes_programacion"] = "Python", "Java", "Go"

print(persona["nombre"])
print(persona["nombre"][0])
print(persona["nombre"][1])
print(persona["nombre"][2])
