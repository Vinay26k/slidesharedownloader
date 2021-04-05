from flask import Flask, render_template, request, send_file
from . import SlideShareDownloader as ssd

app = Flask(__name__)

# code by github.com/Vinay26k

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        BASE_URL= request.form['q-url']
        fileName = "/"+ ssd.downloadSlides(BASE_URL)
        return send_file(fileName, as_attachment=True)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()