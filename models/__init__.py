#!/usr/bin/python3
"""
    __init__ models
"""
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from models.user import User

storage = FileStorage()
storage.reload()