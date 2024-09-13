from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Создаем соединение с базой данных
engine = create_engine('sqlite:///weather.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
