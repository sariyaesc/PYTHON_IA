import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

conn= sqlite3.connect("billboard100.db")
cursor= conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               posicion INTEGER,
               artista TEXT NOT NULL
               )''')

conn.commit()
conn.close()

class Datos(BaseModel):
    id:int
    titulo:str
    artista:str
    posicion:int

app=FastAPI()

@app.post("/agregar/")
async def agregar_datos(datos: Datos):
    conn=sqlite3.connect("billboard100.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO datos (titulo,artista,posicion) VALUES (?, ?, ?)",(datos.titulo,datos.artista,datos.posicion))
    conn.commit()
    conn.close()    
    return {"mensaje":"Datos agregados exitosamente"}

@app.get("/datos/")
async def obtener_todos_datos():
    conn=sqlite3.connect("billboard100.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM datos")
    resultados=cursor.fetchall()
    conn.closea
    if resultados:
        return [{"id":resultado[0],"titulo": resultado[1], "artista": resultado[2], "posicion": resultado[3]}for resultado in resultados]
    else:
        return{"mensaje":"No hay datos en la base de datos"}

@app.put("/actualizar/{id}/")
async def actualizar_datos(id: int,datos:Datos):
    conn=sqlite3.connect("billboard100.db")
    cursor=conn.execute()
    cursor.execute("UPDATE datos SET titulo=?,artista=?,posicion=? WHERE id=?",{datos.titulo, datos.artista, datos.posicion, id})

@app.delete ("/eliminar/{id}/")
async def eliminar_datos(id:int):
    conn=sqlite3.connect("billboard100.db") 
    cursor=conn.execute()
    cursor.execute("DELETE FROM datos WHERE id-?",(id,))
    conn.commit()
    conn.close()
    return {"mensaje":"Datos eliminados exitosamente"}  
