from sqlalchemy import Integer, String, Boolean, Float, ForeignKey, Column
from backend.app.models.db import Base



class User(Base):

    __tablename__ = "users"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False)
    password = Column("password", String, nullable=False)
    admin = Column("admin", Boolean, nullable=False, default=False)

    def __init__(this, name, email, password, admin=False):
        this.name = name
        this.email = email
        this.password = password
        this.admin = admin