# from fastapi import APIRouter, HTTPException
# from typing import List
# from modelos import ItemEmprestado
# from db import get_connection

# router = APIRouter()

# def get_itens_emprestados_db():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_emprestimo, id_ferramenta, quantidade FROM ItemEmprestado")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [ItemEmprestado(id_emprestimo=r[0], id_ferramenta=r[1], quantidade=r[2]) for r in rows]

# def get_item_emprestado_db(id_emprestimo: int, id_ferramenta: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_emprestimo, id_ferramenta, quantidade FROM ItemEmprestado WHERE id_emprestimo = %s AND id_ferramenta = %s", (id_emprestimo, id_ferramenta))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return ItemEmprestado(id_emprestimo=row[0], id_ferramenta=row[1], quantidade=row[2])
#     return None

# def create_item_emprestado_db(item: ItemEmprestado):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO ItemEmprestado (id_emprestimo, id_ferramenta, quantidade) VALUES (%s, %s, %s)",
#         (item.id_emprestimo, item.id_ferramenta, item.quantidade)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return item

# @router.get("/", response_model=List[ItemEmprestado])
# def listar_itens_emprestados():
#     return get_itens_emprestados_db()

# @router.get("/{id_emprestimo}/{id_ferramenta}", response_model=ItemEmprestado)
# def obter_item_emprestado(id_emprestimo: int, id_ferramenta: int):
#     item = get_item_emprestado_db(id_emprestimo, id_ferramenta)
#     if item:
#         return item
#     raise HTTPException(status_code=404, detail="Item não encontrado")

# @router.post("/", response_model=ItemEmprestado)
# def criar_item_emprestado(item: ItemEmprestado):
#     return create_item_emprestado_db(item)
