from fastapi import APIRouter, HTTPException
from typing import List
from modelos import Usuario  # seu modelo Pydantic
from db import get_connection  # função que retorna uma conexão psycopg2

router = APIRouter()

# Função: obter todos os usuários

@router.get("/", response_model=List[Usuario])
def get_usuarios_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_usuario, nome, email, tipo FROM usuario")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Usuario(id_usuario=row[0], nome=row[1], email=row[2], tipo=row[3]) for row in rows]

# # Função: obter usuário por ID
# def get_usuario_by_id(id_usuario: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id_usuario, nome, email, tipo FROM Usuario WHERE id_usuario = %s", (id_usuario,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return Usuario(id_usuario=row[0], nome=row[1], email=row[2], tipo=row[3])
#     else:
#         return None

# # Função: criar usuário
# def create_usuario_db(usuario: Usuario):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO Usuario (id_usuario, nome, email, tipo) VALUES (%s, %s, %s, %s)",
#         (usuario.id_usuario, usuario.nome, usuario.email, usuario.tipo)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return usuario

# # ========================
# # ROTAS DA API FASTAPI
# # ========================

# @router.get("/", response_model=List[Usuario])
# def listar_usuarios():
#     return get_usuarios_db()

# @router.get("/{id_usuario}", response_model=Usuario)
# def obter_usuario(id_usuario: int):
#     usuario = get_usuario_by_id(id_usuario)
#     if usuario:
#         return usuario
#     raise HTTPException(status_code=404, detail="Usuário não encontrado")

# @router.post("/", response_model=Usuario)
# def criar_usuario(usuario: Usuario):
#     return create_usuario_db(usuario)
