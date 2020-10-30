from flask import Flask, render_template
from PIL import Image

app=Flask(__name__)


@app.route('/home')
def giveInsect():
    randomInsect=Image.open('beez\kaggle_bee_vs_wasp\bee1\10823834_7f6ddb5bce_n.jpg')
    return render_template('home.html', randomInsect=randomInsect)

if __name__=='__main__':
    app.run(debug=True)
