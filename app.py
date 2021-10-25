from flask import Flask
import requests
import json
from fpdf import FPDF, HTMLMixin

app = Flask(__name__)


@app.route('/info')
def hello():
    pdf = pydf.generate_pdf('<h1>this is html</h1>')
    with open('test_doc.pdf', 'wb') as f:
        f.write(pdf)
    
    data = {
        'summary': response_dict['emailAddress'],
        'raw': 'Successful',
    }

    return data
   
