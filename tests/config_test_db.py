# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# from config_db import Base
# # Creamos una instacia de Engine
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":
# False})
# # este argumento: connect_args={"check_same_thread": False} es usado sólo en base dedatos SQLite
# # se crea una SessionLocal, que es una sesión de la base de datos:
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # Creamos una instancia de DeclarativeMeta
# Base.metadata.create_all(bind=engine)
