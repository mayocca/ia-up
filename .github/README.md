# Spend-a-lot

Un proyecto desarrollado con Python 3.12 para la asignatura Inteligencia Artificial de la Universidad de Palermo. Este proyecto es una API REST que procesa imágenes de facturas y tickets utilizando el modelo de Hugging Face `impira/layoutlm-invoices`.

## Descripción

Este proyecto implementa una API REST utilizando FastAPI que procesa imágenes de facturas y tickets utilizando el modelo de IA `impira/layoutlm-invoices`. La API extrae información relevante como montos, fechas y detalles del vendedor, devolviendo un JSON estandarizado.

## Requisitos

- Python 3.12
- pip (viene incluido con Python 3.12)
- módulo venv (viene incluido con Python 3.12)
- [tesseract](https://github.com/UB-Mannheim/tesseract)

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/mayocca/ia-up.git
cd ia-up
```

2. Copiar el archivo `.env.example` a `.env` y setear las variables de entorno

```bash
cp .env.example .env
```

3. Crear un entorno virtual

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3.12 -m venv venv
source venv/bin/activate
```

4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

Para iniciar el servidor:

```bash
uvicorn src.main:app --reload
```

La API estará disponible en `http://localhost:8000`

### Endpoints

#### POST /scan-invoice/

Endpoint para procesar imágenes de facturas.

**Solicitud:**

- Método: POST
- Content-Type: multipart/form-data
- Cuerpo: archivo (imagen de factura)

**Respuesta:**

```json
{
  "invoice_number": "string",
  "date": "string",
  "total_amount": 0.0,
  "vendor": "string",
  "items": [
    {
      "description": "string",
      "quantity": 0,
      "unit_price": 0.0,
      "total": 0.0
    }
  ],
  "tax": 0.0,
  "currency": "string"
}
```

## Documentación de la API

Una vez que el servidor esté corriendo, puedes acceder a:

- Documentación interactiva: `http://localhost:8000/docs`
- Documentación OpenAPI: `http://localhost:8000/redoc`
