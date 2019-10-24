# encoding:utf-8
import os

from flask import Flask, redirect, url_for
from soutu.views import gallery

import settings


app = Flask(__name__)
app.register_blueprint(gallery, url_prefix='/gallery')
app.config['GALLERY_ROOT_DIR'] = settings.GALLERY_ROOT_DIR

@app.route('/')
def index():
    return redirect(url_for('gallery.show_gallery'))

if __name__ == '__main__':
    app.logger.info('Listening on http://localhost:8001')
    app.run(port=8001, debug=True)
