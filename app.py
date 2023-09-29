from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from models import User, Role


app = FastAPI()

db: List[User] = [
     User(id=UUID("dad37481-3294-4b00-9d1a-8cf2347491b3") ,
         first_name="Ana", last_name="Maria", email="ana@gmail.com",
         role=[Role.role_1]),

     User(id=UUID("38ab30ad-e593-4104-afab-dde258ae605d") ,
         first_name="Maria", last_name="Miliana", email="mili@gmail.com",
         role=[Role.role_2]),
     User(
          id=UUID("766d2a84-b820-43d0-98ad-b8c124a1a8b5") , #ID COPIADO DO NAVEGADOR EM JSON
         first_name="Camila", last_name="Melo", email="cami@gmail.com",
         role=[Role.role_3])
]

@app.get("/")
async def root():
    return{"message": "Olá"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id:UUID):
    for user in db:
        if user.id == id:
            return user
        return {"message": " Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    '''
     Adiciona um usuário na base de dados:
   - id:UUID
   - first_name: str
   - last_name: str
   - email: str
   -role:Role
    '''
    db.append(user)
    return{"id": user.id}

@app.put("/api/users/{id}")
async def update_user(id: UUID, updated_user: User):
    for index, user in enumerate(db):
        if user.id == id:
            # Update the user's information
            db[index] = updated_user
            return {"message": f"Usuário com id {id} foi atualizado com sucesso!"}


@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code =404,
        detail= f"Usuário com o id {id} não encontrado!"
    )
