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
                <h1>Hola mundo!!</h1>
            </body>
        </html>
        """

    from fpdf import FPDF, HTMLMixin

    class MyFPDF(FPDF, HTMLMixin):
	    pass

    pdf = MyFPDF()
    pdf.add_page()
    pdf.write_html(html)

    pdf.output('example.pdf', 'F')
    
    data = {
        'summary': response_dict['emailAddress'],
        'raw': 'Successful',
    }

    return data
   
