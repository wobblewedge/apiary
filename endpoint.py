from flask import render_template
from PIL import image

app=Flask(__name__)

@app.route('/home')
def giveInsect("/*", method=["GET"])
    randomInsect=Image.open('apiary/beez/kaggle_bee_vs_wasp/bee1/1240800_e5f2b40032_n.jpg')
    return render_template('home.html', randomInsect=randomInsect)
