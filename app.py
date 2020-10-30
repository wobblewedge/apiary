from flask import Flask, render_template
from PIL import Image

app=Flask(__name__)


@app.route('/home')
def giveInsect():
    randomInsect=Image.open(r'beez\kaggle_bee_vs_wasp\bee1\2984293_b650d46745_n.jpg')
    return render_template('home.html', randomInsect=randomInsect)

if __name__=='__main__':
    app.run(debug=True)
