from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    temperature = Column(Float)
    wind_speed = Column(Float)
    wind_direction = Column(String)
    pressure = Column(Float)
    precipitation_type = Column(String)
    precipitation_amount = Column(Float)
