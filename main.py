# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:04:01 2021

@author: Vignez
"""
from flask import Flask
  
app = Flask(__name__)
  
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"
