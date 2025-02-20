from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict

# Create FastAPI app instance
app = FastAPI()  # This line is crucial - 'app' must be defined at module level

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input model
class TextInput(BaseModel):
    text: str
    parameters: Optional[Dict] = None

@app.post("/api/generate")
async def generate_model(input_data: TextInput):
    try:
        return {
            "status": "success",
            "message": f"Received text: {input_data.text}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}