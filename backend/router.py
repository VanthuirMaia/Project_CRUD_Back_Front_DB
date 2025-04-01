from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()

# Criar a rota de buscar todos os itens
@router.get("/products", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    """
    Essa é minha rota de ler todos os produtos do banco de dados
    """
    products = get_product(db)
    return products

# Criar a rota de buscar 1 item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    """
    Essa é minha rota de apenas 01 produto do banco de dados
    """
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Esse produto não existe")
    return db_product

# Criar a rota de adicionar um item
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Essa é minha rota de criar um produto do banco de dados
    """
    return create_product(product=product, db=db)

# Criar a rota de deletar um item
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Essa é minha rota de apagar um produto do banco de dados
    """
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Esse produto não existe")
    return delete_product(product_id=product_id, db=db)

# Criar a rota de Editar um item
@router.put("/products/{product_id}", response_model=ProductResponse)
def atualizar_product(product_id: int, product: ProductResponse, db: Session=Depends(get_db)):
    """
    Essa é minha rota de editar um produto do banco de dados
    """
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Esse produto não existe")
    product_db
    
    