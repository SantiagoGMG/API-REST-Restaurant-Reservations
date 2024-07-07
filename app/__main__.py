"""
Esta es una forma alternativa de iniciar la aplicación, para ello usar:
    python -m app

Estando en la carpeta de .env
"""

from . import app

if __name__ == "__main__":
    app.run(debug=True, port=4000)  # No añadir parámetros, modificar directamente en Config