# Convertidor de imágenes para móvil y tablet

Este proyecto es un script en Python que permite convertir imágenes a formato WebP optimizado para dispositivos móviles y tabletas. Utiliza la librería Pillow para manipular las imágenes y genera versiones redimensionadas para móvil (400x400) y tablet (800x800).

## Requisitos

- Python 3.x instalado en tu sistema.
- Librería Pillow (instalada automáticamente vía requirements.txt).

## Instalación

### 1. Crear un entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto.

En la terminal, navega al directorio del proyecto:

```bash
cd convertidorIMGFormatoTableMovil
```

Crea un entorno virtual:

```bash
python3 -m venv venv
```

### 2. Activar el entorno virtual

Activa el entorno virtual:

- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

- En Windows:
  ```bash
  venv\Scripts\activate
  ```

### 3. Instalar dependencias

Instala las dependencias desde el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

Esto instalará Pillow y cualquier otra dependencia necesaria.

## Uso

1. Ejecuta el script:
   ```bash
   python convertidor.py
   ```

2. Selecciona la opción 1 en el menú para convertir una imagen.

3. Ingresa la ruta completa o relativa de la imagen de entrada (por ejemplo: `imagen.jpg` o `/ruta/a/imagen.png`).

4. El script generará dos versiones:
   - `imagen-mobile.webp` (400x400 píxeles)
   - `imagen-tablet.webp` (800x800 píxeles)

   Las imágenes se guardarán en el mismo directorio que la imagen original.

5. Para salir, selecciona la opción 2.

## Sitio web

Enlace al sitio web:
> [Página](https://12345star.github.io/convertidor-imagen-table-movil-python/)

## Notas

- Asegúrate de que la imagen de entrada sea de un formato compatible con Pillow (JPEG, PNG, etc.).
- Las imágenes de salida están en formato WebP con calidad del 85 % para optimización.
- Si encuentras errores, verifica que Pillow esté instalado correctamente y que la ruta de la imagen sea válida.

## Licencia

Este proyecto es de uso libre. Modifícalo según tus necesidades.