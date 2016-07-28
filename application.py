from flask import Flask, render_template, request
from application import db
from application.models import Photo

import sys, os
includepath = os.path.abspath(os.path.join('./','backend'))
sys.path.append(includepath)
import picasa_photo_import
import photo_filterer

# Elastic Beanstalk initalization
app = Flask(__name__)
app.debug=True
# change this to your own value
app.secret_key = 'cC1YCIWOj9GgWspgNEo2'  
urls = ("/favicon.ico", "dummy")

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/map')
def index():

    useremail = request.args.get('useremail')
    earliestDate = request.args.get('earliestDate')
    latestDate = request.args.get('latestDate')  
    photolist = picasa_photo_import.get_photo_url_and_geo(useremail)

    return render_template('index.html',
    					   useremail=useremail,
    					   photolist=photolist,
                           earliestDate=earliestDate)


if __name__ == '__main__':
    # Change to below version when running on localhost
    app.run()
    # Change to below version when running on EBS
    #app.run(host='0.0.0.0')
