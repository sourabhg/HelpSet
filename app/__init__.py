import os,sys
from urlparse import urlparse
from flask import Flask,render_template,url_for,json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
app.debug = True
 
from routes import *