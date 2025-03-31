from pydantic import BaseModel, PositiveFloat, EmailStr, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional

class ProdutoBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProdutoBase):
    pass

class ProductUpdate(ProdutoBase):
    pass