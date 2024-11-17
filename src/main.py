from fastapi import FastAPI, UploadFile, HTTPException
from transformers import pipeline
from PIL import Image
import io
import re
from typing import Dict, List, Tuple, Optional
from datetime import datetime

app = FastAPI(title="Invoice Scanner API")

# Initialize the pipeline
pipe = pipeline("document-question-answering", model="impira/layoutlm-invoices")

INVOICE_QUESTIONS = [
    "What is the ticket number?",
    "What is the invoice date?",
    "What is the total amount?",
    "Who is the vendor? This is the name of the company that provided the service.",
]

def parse_currency(amount_str: str) -> float:
    """Convert currency string to float."""
    try:
        return float(re.sub(r'[^\d.]', '', amount_str))
    except (ValueError, AttributeError):
        return 0.0

def extract_field(results: List, index: int, default: str = '...') -> str:
    """Safely extract field from results."""
    return results[index][0]['answer'] if results[index] else default

def process_image(image: Image.Image) -> Dict:
    """Process image and extract invoice information."""
    # Get answers using the pipeline
    results = [pipe(image=image, question=q) for q in INVOICE_QUESTIONS]
    
    # Parse the date string into a datetime object
    try:
        date_str = extract_field(results, 1)
        # Try multiple date formats
        for date_format in ['%m/%d/%Y', '%d %B, %Y', '%d %b, %Y', '%Y-%m-%d', '%d %b %Y']:
            try:
                date = datetime.strptime(date_str, date_format)
                break
            except ValueError:
                continue
        else:  # If no format worked
            date = None
    except (ValueError, AttributeError):
        date = None
    
    try:
        total_amount = results[2][0]['answer'] if results[2] else '0.0'
        total_amount = float(total_amount.replace('$', '').replace(',', ''))
    except (ValueError, AttributeError):
        total_amount = 0.0
    
    extracted_data = {
        "date": date.isoformat() if date else None,
        "total_amount": total_amount,
        "vendor": extract_field(results, 3),
    }
    
    return extracted_data

@app.post("/scan-invoice/")
async def scan_invoice(file: UploadFile):
    # Verify file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        # Read the image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Process the image
        result = process_image(image)
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)