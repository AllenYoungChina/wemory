from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter_by(id=user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter_by(email=email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter_by(username=username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = models.User(username=user.username, email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item_by_user_id(db: Session, user_id: int):
    return db.query(models.Item).filter_by(user_id=user_id).all()


def create_user_item(db: Session, user_id: int, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
