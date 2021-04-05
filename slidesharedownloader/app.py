from flask import Flask, render_template, request
from . import SlideShareDownloader as ssd

app = Flask(__name__)

# code by github.com/Vinay26k

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        BASE_URL= request.form['q-url']
        ssd.downloadSlides(BASE_URL)
        return "Downloaded File!"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()