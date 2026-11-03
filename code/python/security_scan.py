import sys

# Palabras que indican una posible clave API expuesta
PATRONES = ["api_key", "apikey", "secret_key", "token"]

with open("ventas.json") as fichero:
    contenido = fichero.read().lower()

for patron in PATRONES:
    if patron in contenido:
        print(f"Posible clave expuesta encontrada: {patron}")
        sys.exit(1)

print("Escaneo de seguridad OK: no hay claves API expuestas")
