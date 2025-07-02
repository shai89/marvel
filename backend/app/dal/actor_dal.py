from sqlalchemy.orm import Session
from app import models

def get_or_create_actor(db: Session, name: str):
    actor = db.query(models.Actor).filter(models.Actor.name == name).first()
    if actor:
        return actor

    actor = models.Actor(name=name)
    db.add(actor)
    db.commit()
    db.refresh(actor)
    return actor


def get_all_actors(db: Session):
    return db.query(models.Actor).all()
