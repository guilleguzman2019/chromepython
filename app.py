from flask import Flask

app = Flask(__name__)


@app.route('/info')
def hello():
    
    data = {
        'summary': 'prueba',
        'raw': 'Successful',
    }

    return data
   
