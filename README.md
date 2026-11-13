# Portal de Servicios

Aplicación web desarrollada con Flask para la Universidad de León. Presenta
información de una empresa ficticia, sus servicios y medios de contacto, además
de calculadoras de compra, salario y conversión de temperatura. La interfaz usa
Bootstrap 4.6.2 y sus archivos CSS, JavaScript e imágenes están dentro de
`static/`.

## Requisitos

- Python 3.9 o posterior.
- `pip`, incluido con Python.
- PowerShell o una terminal compatible con Windows.

Las dependencias de Python están listadas en `requirements.txt`.

## Instalación

Abre la terminal en la carpeta del proyecto y crea el entorno virtual:

```TERMINAL
py -m venv .venv
```

Actívalo:

```terminal
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```terminal
python -m pip install -r requirements.txt
```

## Iniciar la aplicación

Desde la carpeta del proyecto, con el entorno virtual activo, ejecuta:

```terminal
python app.py
```

Abre la dirección local en el navegador:

<http://127.0.0.1:5000>