from flask import Flask
from linkedin_api import Linkedin

app = Flask(__name__)


@app.route('/info')
def hello():
    
    perfil = 'micaela-patricia-jasarevic-10a883140'

    headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
           }

    company_link = 'https://www.linkedin.com//voyager/api/identity/profiles/guillermo-alejandro-guzman/profileContactInfo'

    with requests.session() as s:
        s.cookies['li_at'] = "AQEDARxXg0cDGCM-AAABfJ5Lih8AAAF8wlgOH04AAVrtbs3uVlAsVQyqqvupNFjQeC4S8B-rcP_tB8kru2_ErtLkLIjjSq6aw8I_5Ecv9kNO60OIf2ZgfD1CX8cTihYRbXje6xwcDQ1y8vlv-KJqmWrW"
        s.cookies["JSESSIONID"] = "ajax:4512023706200924032"
        s.headers = headers
        s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
        response = s.get(company_link)
        response_dict = response.json()
        result = json.dumps(response_dict)
        #print(result)
    
    data = {
        'summary': result['firstName'],
        'raw': 'Successful',
    }

    return data
   
