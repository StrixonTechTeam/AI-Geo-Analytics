from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base

class WeatherRecord(Base):
    __tablename__ = "weather_records"  # the actual table name in PostgreSQL

    id          = Column(Integer, primary_key=True)
    city        = Column(String, index=True)   # index makes searching by city fast
    country     = Column(String)
    latitude    = Column(Float)
    longitude   = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)
    temp_max    = Column(Float)   # degrees Celsius
    temp_min    = Column(Float)
    precipitation = Column(Float) # mm of rain
    wind_speed  = Column(Float)   # km/h
    description = Column(String)  # "Partly Cloudy", "Rain", etc.