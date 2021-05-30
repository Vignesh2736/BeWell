# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:04:01 2021

@author: Vignez
"""
from flask import Flask
  
main = Flask(__name__)
  
@main.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"
