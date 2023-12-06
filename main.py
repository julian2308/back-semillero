from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import openpyxl




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes ajustar esto para permitir solo ciertos orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id+3}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    datos = pd.read_excel(file.file, header=7, skipfooter=4)
    outfile = 'resultados.txt'
    finalFile = open(outfile, 'w')
    finalFile.write(f'Promedio: {datos["Tasa de cambio representativa del mercado (TRM)"].mean()}\n')
    finalFile.write(f'Máximo: {datos["Tasa de cambio representativa del mercado (TRM)"].max()}\n')
    finalFile.write(f'Mínimo: {datos["Tasa de cambio representativa del mercado (TRM)"].min()}\n')
    finalFile.close()
    

    return {"Promedio": datos["Tasa de cambio representativa del mercado (TRM)"].mean(),
            "Máximo" : datos["Tasa de cambio representativa del mercado (TRM)"].max(),
            "Mínimo" : datos["Tasa de cambio representativa del mercado (TRM)"].min()}