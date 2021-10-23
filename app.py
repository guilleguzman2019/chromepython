from flask import Flask
import requests
import json
from fpdf import FPDF, HTMLMixin

app = Flask(__name__)


@app.route('/info')
def hello():
    
    html = """
            <!DOCTYPE html>
            <html>
                <head>
                    <!-- head definitions go here -->
                </head>
                <body>
                    <h1>Hola mundo!!!</h1>
                </body>
            </html>
          """
    
    class MyFPDF(FPDF, HTMLMixin):
        pass

    pdf = MyFPDF()
    #First page
    pdf.add_page()
    pdf.write_html(html)
    pdf.output('html2pdf.pdf', 'F')
    
    data = {
        'summary': response_dict['emailAddress'],
        'raw': 'Successful',
    }

    return data
   
