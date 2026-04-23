import os #import sys para manejo de argumentos de línea de comandos, os para manejo de archivos
from PIL import Image #importamos la librería Pillow para manipulación de imágenes

# Dimensiones objetivo para móvil y tablet
DIMENSIONES = {
    "mobile": (400, 400),   # ejemplo: cuadrada para móvil
    "tablet": (800, 800)    # ejemplo: más grande para tablet
}

def generar_versiones(input_path):
    try:
        # Abrimos la imagen original
        with Image.open(input_path) as img:
            # Convertimos a RGB si es necesario (para compatibilidad)
            img = img.convert("RGB")

            # Carpeta de salida (misma que la original)
            base_dir = os.path.dirname(input_path)
            base_name = os.path.splitext(os.path.basename(input_path))[0]

            for tipo, size in DIMENSIONES.items():
                # Redimensionamos manteniendo proporción
                img_resized = img.resize(size, Image.LANCZOS)

                # Nombre de salida
                output_path = os.path.join(base_dir, f"{base_name}-{tipo}.webp")

                # Guardamos en formato WebP
                img_resized.save(output_path, "WEBP", quality=85)

                print(f"✅ Imagen {tipo} creada en: {output_path}")

    except Exception as e:
        print(f"❌ Error al generar versiones: {e}")

#metodo principal para convertir imágenes a diferentes formatos
def  main():
    while True:
        print("------------------------")
        print("|    MENÚ PRINCIPAL.    |")
        print("| 1. Convertir imagen.  |")
        print("| 2. Salir.             |")
        print("------------------------")
        opcion = input("Selecciona una opción: ")

        if opcion == "1": #convertir imagen a formato webp para móvil y tablet  
            # Ruta de la imagen original
            input_path = input("Ingresa el nombre o la ruta de la imagen de entrada: ")
            generar_versiones(input_path)
        elif opcion == "2":
            print(" Gracias por usar el convertidor....")
            break
        else:
            print(" Opción inválida, intenta de nuevo.")
    

# llamada al método principal
if __name__ == "__main__":
    main()

# Nota: Asegúrate de que la imagen de entrada esté en el mismo directorio que el script o proporciona la ruta completa. 
# Las imágenes convertidas se guardarán con un sufijo indicando el tipo (mobile o tablet) y en formato WebP, 
# lo que es ideal para su uso en dispositivos móviles y tablets debido a su eficiencia en compresión sin pérdida significativa de calidad.

## Para ejecutar el programa, asegúrate de tener la librería Pillow instalada:
# pip install Pillow
# O si estás usando un entorno virtual, activa tu entorno y luego instala las dependencias:
# python3 -m pip install -r requirements.txt

# Luego, puedes ejecutar el script y seguir las instrucciones para convertir tus imágenes a formato WebP para móvil
# y tablet. Asegúrate de proporcionar la ruta correcta de la imagen de entrada. Las imágenes convertidas se guardarán en el mismo 
# directorio que la original con un sufijo indicando el tipo (mobile o tablet).




