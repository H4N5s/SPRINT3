def generar_contrasena():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    contrasena = ""
    for _ in range(8):
        contrasena += random.choice(caracteres)
    return contrasena

generar_contrasena()