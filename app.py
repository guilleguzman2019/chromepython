from flask import Flask
from datetime import datetime
import pydf

app = Flask(__name__)

@app.route('/')
def homepage():
    pdf = pydf.generate_pdf('<h1>this is html</h1>')
    with open('test_doc.pdf', 'wb') as f:
        f.write(pdf)
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
