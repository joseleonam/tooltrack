# from fastapi import APIRouter, HTTPException
# from typing import List
# from modelos import Ferramenta
# from db import get_connection

# router = APIRouter()

# def get_ferramentas_db():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_ferramenta, nome, descricao, categoria, status FROM Ferramenta")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [Ferramenta(id_ferramenta=r[0], nome=r[1], descricao=r[2], categoria=r[3], status=r[4]) for r in rows]

# def get_ferramenta_db(id_ferramenta: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_ferramenta, nome, descricao, categoria, status FROM Ferramenta WHERE id_ferramenta = %s", (id_ferramenta,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return Ferramenta(id_ferramenta=row[0], nome=row[1], descricao=row[2], categoria=row[3], status=row[4])
#     return None

# def create_ferramenta_db(ferramenta: Ferramenta):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO Ferramenta (id_ferramenta, nome, descricao, categoria, status) VALUES (%s, %s, %s, %s, %s)",
#         (ferramenta.id_ferramenta, ferramenta.nome, ferramenta.descricao, ferramenta.categoria, ferramenta.status)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return ferramenta

# @router.get("/", response_model=List[Ferramenta])
# def listar_ferramentas():
#     return get_ferramentas_db()

# @router.get("/{id_ferramenta}", response_model=Ferramenta)
# def obter_ferramenta(id_ferramenta: int):
#     ferramenta = get_ferramenta_db(id_ferramenta)
#     if ferramenta:
#         return ferramenta
#     raise HTTPException(status_code=404, detail="Ferramenta não encontrada")

# @router.post("/", response_model=Ferramenta)
# def criar_ferramenta(ferramenta: Ferramenta):
#     return create_ferramenta_db(ferramenta)
