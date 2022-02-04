from flask import Flask, render_template, request, redirect, url_for
from mishap import html_mishap

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
   print('Request for index page received')
   if request.method == 'POST':
      if request.form['mishap'] == 'teleporter':
         mishap_text = html_mishap(1,1)
         return render_template('mishap.html', mishap_text=mishap_text)
   elif request.method == 'GET':
      return render_template('index2.html')

if __name__ == '__main__':
   app.run()