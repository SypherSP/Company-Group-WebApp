from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='3b7087e6018f2c48bf23a41c'

from CG import routes