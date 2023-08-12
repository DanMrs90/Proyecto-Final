# %%
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# %%
class Item(BaseModel):
    dia: int
    temp_maxima: int
    temp_min: int
    temp_promedio: int

app = FastAPI()

# %%
@app.post("/agregar_temperatura/")
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temperaturas(dia,temp_maxima,temp_min,temp_promedio) VALUES (?,?,?,?)", (item.dia, item.temp_maxima, item.temp_min,item.temp_promedio))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

# %%
@app.get("/leer_elementos/")
async def leer_elementos():
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id,dia,temp_maxima,temp_min,temp_promedio FROM temperaturas")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"id": resultado[0], "dia": resultado[1], "temp_maxima": resultado[2],"temp_min": resultado[3],"temp_promedio": resultado[4]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

# %%
@app.get("/leer_elemento/{id}/")
async def leer_elemento(id: int):
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id,dia,temp_maxima,temp_min,temp_promedio FROM temperaturas WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"id": resultado[0], "dia": resultado[1], "temp_maxima": resultado[2],"temp_min": resultado[3],"temp_promedio": resultado[4]}
    else:
        return {"mensaje": "Datos no encontrados"}

# %%
@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE temperaturas SET dia=?,temp_maxima=?,temp_min=?,temp_promedio=? WHERE id=?", (item.dia, item.temp_maxima, item.temp_min,item.temp_promedio,id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

# %%
@app.delete("/eliminar_elemento/{id}/")
async def eliminar_elemento(id: int):
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temperaturas WHERE id=?", (id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}

# %%

#http://127.0.0.1:8000/docs