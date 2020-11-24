from flask import Flask
from flask import request
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/add', methods=['GET'])
def test_api():
    temp = request.args.get('str', 'default')
    custom_logger.info("request :"+temp)
    return temp


if __name__ == '__main__':
    custom_logger = logging.getLogger('Groobee')
    custom_logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler("logs/test.log", maxBytes=1000, mode='a', backupCount=5)
    fileFormatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    handler.setFormatter(fileFormatter)
    custom_logger.addHandler(handler)
    custom_logger.info("Logging Start")
    app.run()
