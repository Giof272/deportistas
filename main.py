# Activando pipeline CI

from fastapi import FastAPI

app = FastAPI()

deportistas = [
    {"id": 1, "nombre": "Juan", "disciplina": "Fútbol"},
    {"id": 2, "nombre": "Ana", "disciplina": "Natación"}
]

@app.get("/")
def inicio():
    return {"mensaje": "API FastAPI funcionando"}

@app.get("/deportistas")
def obtener_deportistas():
    return deportistas

@app.get("/buscar/{id}")
def buscar(id: int):
    for d in deportistas:
        if d["id"] == id:
            return d
    return {"error": "No encontrado"}
