from pydantic import BaseModel
from typing import Optional
from datetime import date

class Usuario(BaseModel):
    id_usuario: int
    nome: str
    email: Optional[str] = None
    tipo: Optional[str] = None

class Ferramenta(BaseModel):
    id_ferramenta: int
    nome: str
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    status: Optional[str] = None

class Emprestimo(BaseModel):
    id_emprestimo: int
    id_usuario: int
    data_emprestimo: date
    data_prevista_devolucao: date
    data_devolucao: Optional[date] = None

class ItemEmprestado(BaseModel):
    id_emprestimo: int
    id_ferramenta: int
    quantidade: int

class Manutencao(BaseModel):
    id_manutencao: int
    id_ferramenta: int
    tipo: str
    data_manutencao: date
    descricao: Optional[str] = None

class Localizacao(BaseModel):
    id_ferramenta: int
    sala: str
    armario: str
    prateleira: str
