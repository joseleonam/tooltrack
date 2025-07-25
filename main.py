from fastapi import FastAPI
from crud import crud_usuario, ferramenta, emprestimo, manutencao, localizacao, itemEmprestado

from crud.crud_usuario import router as usuario_router

app = FastAPI(
    title="projeto ToolTrack API",
    version="1.0"
)

# Incluindo rotas
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuarios"])
# app.include_router(ferramenta.router, prefix="/ferramentas", tags=["Ferramentas"])
# app.include_router(emprestimo.router, prefix="/emprestimos", tags=["Empréstimos"])
# app.include_router(manutencao.router, prefix="/manutencoes", tags=["Manutenções"])
# app.include_router(localizacao.router, prefix="/localizacoes", tags=["Localizações"])
# app.include_router(itemEmprestado.router, prefix="/itens-emprestados", tags=["Itens Emprestados"])
