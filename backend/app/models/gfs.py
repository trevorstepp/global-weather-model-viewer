from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime

from db.database import Base

class GFSRun(Base):
    __tablename__ = "gfs_runs"

class GFSImage(Base):
    __tablename__ = "gfs_images"