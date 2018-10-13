import os
import sys
import requests

from flask import jsonify, request, make_response, send_from_directory

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

PUBLIC_PATH = os.path.join(ROOT_PATH, 'public')

from app import app
from logger import logger

PORT = os.environ.get('PORT')

LOG = logger.get_root_logger(os.environ.get('ROOT_LOGGER', 'root'), 
    filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/')
def index():
    """ static files serve """
    return send_from_directory(PUBLIC_PATH, 'index.html')

if __name__ == '__main__':
    LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development' # Debug mode if development env
    app.run(host='0.0.0.0', port=int(PORT)) # Run the app