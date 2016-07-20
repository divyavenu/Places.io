from flask import Flask, render_template, request
from application import db
from application.models import Data

# Elastic Beanstalk initalization
app = Flask(__name__)
app.debug=True
# change this to your own value
app.secret_key = 'cC1YCIWOj9GgWspgNEo2'  
urls = ("/favicon.ico", "dummy")

@app.route('/')
def index():
	return render_template('login.html')



if __name__ == '__main__':
    app.run()
    # Uncomment when running on EBS
    #app.run(host='0.0.0.0')