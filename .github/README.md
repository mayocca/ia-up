# IA-UP

Un proyecto desarrollado con Python 3.13 para la asignatura Inteligencia Artificial de la Universidad de Palermo.

## Requisitos

- Python 3.13
- pip (viene incluido con Python 3.13)
- módulo venv (viene incluido con Python 3.13)

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/mayocca/ia-up.git
cd ia-up
```

2. Crear un entorno virtual

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3.13 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Problemas Comunes

### Versión de Python

Asegúrate de tener Python 3.13 instalado:

```bash
python --version  # Debería mostrar Python 3.13.x
```

### Entorno Virtual

Si aparece el error "venv not found" (entorno virtual no encontrado):

```bash
# Windows
py -3.13 -m venv venv

# macOS/Linux
python3.13 -m venv venv
```

## Solución de Problemas Comunes

### Si pip no funciona:

```bash
# Actualizar pip
python -m pip install --upgrade pip
```

### Si hay problemas con las dependencias:

```bash
# Instalar dependencias una por una
pip install numpy
pip install pandas
pip install torch
```

### Si Jupyter no inicia:

```bash
# Reinstalar Jupyter
pip uninstall jupyter
pip install jupyter
```
