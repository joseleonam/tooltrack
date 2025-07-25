# from fastapi import APIRouter, HTTPException
# from typing import List
# from modelos import Localizacao
# from db import get_connection

# router = APIRouter()

# def get_localizacoes_db():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_ferramenta, sala, armario, prateleira FROM Localizacao")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [Localizacao(id_ferramenta=r[0], sala=r[1], armario=r[2], prateleira=r[3]) for r in rows]

# def get_localizacao_db(id_ferramenta: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_ferramenta, sala, armario, prateleira FROM Localizacao WHERE id_ferramenta = %s", (id_ferramenta,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return Localizacao(id_ferramenta=row[0], sala=row[1], armario=row[2], prateleira=row[3])
#     return None

# def create_localizacao_db(localizacao: Localizacao):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO Localizacao (id_ferramenta, sala, armario, prateleira) VALUES (%s, %s, %s, %s)",
#         (localizacao.id_ferramenta, localizacao.sala, localizacao.armario, localizacao.prateleira)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return localizacao

# @router.get("/", response_model=List[Localizacao])
# def listar_localizacoes():
#     return get_localizacoes_db()

# @router.get("/{id_ferramenta}", response_model=Localizacao)
# def obter_localizacao(id_ferramenta: int):
#     localizacao = get_localizacao_db(id_ferramenta)
#     if localizacao:
#         return localizacao
#     raise HTTPException(status_code=404, detail="Localização não encontrada")

# @router.post("/", response_model=Localizacao)
# def criar_localizacao(localizacao: Localizacao):
#     return create_localizacao_db(localizacao)
