#!/usr/bin/python3
""" Initiate Review Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Create Review """
    place_id = ""
    user_id = ""
    text = ""
