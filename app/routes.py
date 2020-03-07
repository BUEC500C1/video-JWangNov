from flask import render_template
from flask import send_file
from flask import send_from_directory
from app import app
from videoGenerator import VideoGen
import os
import request


myDict = {
    'lagav' : '@LagavulinWhisky',
    'laphr' : '@Laphroaig',
    'klcho' : '@Kilchomanwhisky',
    'bnrmc' : '@Benromach',
    'cdsde' : '@clydesidewhisky'
}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route("/<abbr>", methods=['GET'])
def genLaga(abbr):
    user = myDict[abbr]
    filename = 'TV_{}.mp4'.format(user)
    obj = VideoGen(user, 10)
    obj.run()
    return send_from_directory(os.getcwd(), filename, as_attachment=True)
