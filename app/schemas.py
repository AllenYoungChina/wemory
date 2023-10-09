from pydantic import BaseModel, EmailStr


class ItemBase(BaseModel):
    content: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        from_attributes = True
