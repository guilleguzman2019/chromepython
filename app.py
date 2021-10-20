from flask import Flask
from linkedin_api import Linkedin

app = Flask(__name__)


@app.route('/info')
def hello():
    
    perfil = 'micaela-patricia-jasarevic-10a883140'

    api = Linkedin('guillermoguzman.2016@gmail.com', 'guille16')

    profile = api.get_profile(perfil)
    
    data = {
        'summary': profile['firstName'],
        'raw': 'Successful',
    }

    return data
   
