# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:55:28 2021

@author: Vignez
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

