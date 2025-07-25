# from fastapi import APIRouter, HTTPException
# from typing import List
# from modelos import Emprestimo
# from db import get_connection

# router = APIRouter()

# def get_emprestimos_db():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_emprestimo, id_usuario, data_emprestimo, data_prevista_devolucao, data_devolucao FROM Emprestimo")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [Emprestimo(id_emprestimo=r[0], id_usuario=r[1], data_emprestimo=r[2], data_prevista_devolucao=r[3], data_devolucao=r[4]) for r in rows]

# def get_emprestimo_db(id_emprestimo: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_emprestimo, id_usuario, data_emprestimo, data_prevista_devolucao, data_devolucao FROM Emprestimo WHERE id_emprestimo = %s", (id_emprestimo,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return Emprestimo(id_emprestimo=row[0], id_usuario=row[1], data_emprestimo=row[2], data_prevista_devolucao=row[3], data_devolucao=row[4])
#     return None

# def create_emprestimo_db(emprestimo: Emprestimo):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO Emprestimo (id_emprestimo, id_usuario, data_emprestimo, data_prevista_devolucao, data_devolucao) VALUES (%s, %s, %s, %s, %s)",
#         (emprestimo.id_emprestimo, emprestimo.id_usuario, emprestimo.data_emprestimo, emprestimo.data_prevista_devolucao, emprestimo.data_devolucao)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return emprestimo

# @router.get("/", response_model=List[Emprestimo])
# def listar_emprestimos():
#     return get_emprestimos_db()

# @router.get("/{id_emprestimo}", response_model=Emprestimo)
# def obter_emprestimo(id_emprestimo: int):
#     emprestimo = get_emprestimo_db(id_emprestimo)
#     if emprestimo:
#         return emprestimo
#     raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

# @router.post("/", response_model=Emprestimo)
# def criar_emprestimo(emprestimo: Emprestimo):
#     return create_emprestimo_db(emprestimo)
