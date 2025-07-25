# from fastapi import APIRouter, HTTPException
# from typing import List
# from modelos import Manutencao
# from db import get_connection

# router = APIRouter()

# def get_manutencoes_db():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_manutencao, id_ferramenta, tipo, data_manutencao, descricao FROM Manutencao")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [Manutencao(id_manutencao=r[0], id_ferramenta=r[1], tipo=r[2], data_manutencao=r[3], descricao=r[4]) for r in rows]

# def get_manutencao_db(id_manutencao: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_manutencao, id_ferramenta, tipo, data_manutencao, descricao FROM Manutencao WHERE id_manutencao = %s", (id_manutencao,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return Manutencao(id_manutencao=row[0], id_ferramenta=row[1], tipo=row[2], data_manutencao=row[3], descricao=row[4])
#     return None

# def create_manutencao_db(manutencao: Manutencao):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO Manutencao (id_manutencao, id_ferramenta, tipo, data_manutencao, descricao) VALUES (%s, %s, %s, %s, %s)",
#         (manutencao.id_manutencao, manutencao.id_ferramenta, manutencao.tipo, manutencao.data_manutencao, manutencao.descricao)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return manutencao

# @router.get("/", response_model=List[Manutencao])
# def listar_manutencoes():
#     return get_manutencoes_db()

# @router.get("/{id_manutencao}", response_model=Manutencao)
# def obter_manutencao(id_manutencao: int):
#     manutencao = get_manutencao_db(id_manutencao)
#     if manutencao:
#         return manutencao
#     raise HTTPException(status_code=404, detail="Manutenção não encontrada")

# @router.post("/", response_model=Manutencao)
# def criar_manutencao(manutencao: Manutencao):
#     return create_manutencao_db(manutencao)
