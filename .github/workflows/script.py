import datetime

print("🔧 Ejecutando script de prueba...")

try:
    # Generar archivo de resultados
    with open("resultado.txt", "w") as file:
        file.write(f"Fecha de ejecución: {datetime.datetime.now()}\n")
        file.write("Estado: ÉXITO\n")
    print("✅ Archivo 'resultado.txt' creado!")
except Exception as error:
    print(f"❌ Error: {error}")
    raise  # Esto hará fallar el workflow