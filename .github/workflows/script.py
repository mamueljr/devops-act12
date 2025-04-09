import datetime

print("🚀 Iniciando ejecución del script...")
try:
    with open("resultados.txt", "w") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Resultado generado el: {fecha}\n")
        f.write("Estado: ÉXITO\n")
    print("✅ Archivo de resultados creado correctamente!")
except Exception as e:
    print(f"❌ Error al generar archivo: {e}")
    raise