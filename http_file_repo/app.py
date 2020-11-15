# -*- coding:utf-8 -*-

"""App routing."""

import hashlib
import logging
import os

from flask import Flask, request, send_file

from http_file_repo import values

STORE_DIR = 'store'
LOCAL_PORT = 5000
logging.basicConfig(
    format='%(levelname)s - %(asctime)s - %(message)s',  # noqa: WPS323
    level=logging.DEBUG,
    datefmt='%d-%b-%y %H:%M:%S',  # noqa: WPS323
)
app = Flask(__name__)

if __name__ != '__main__':
    # Update the Gunicorn logging level
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.route('/upload', methods=['POST'])  # noqa: WPS210, WPS212, WPS213, WPS231
def upload():  # noqa: WPS210, WPS212, WPS213, WPS231
    """Upload file to the store and return file's md5 hash."""
    if 'file' not in request.files:
        app.logger.error('A file is missing')
        return 'A file is missing', 400
    upload_file = request.files['file']
    if not upload_file.filename:
        app.logger.error('No selected file')
        return 'No selected file', 400
    file_hash = hashlib.md5(upload_file.read()).hexdigest()  # noqa: S303
    file_path = os.path.join(STORE_DIR, file_hash[:2], file_hash)
    file_dir = os.path.dirname(file_path)
    if os.path.exists(STORE_DIR):
        if os.path.exists(file_dir):
            if os.path.exists(file_path):
                app.logger.error(
                    'This file already exists: {0}'.format(file_hash),
                )
                return 'This file already exists', 409
        else:
            try:
                os.mkdir(file_hash[:2])
            except (IOError, OSError) as exc:
                app.logger.debug(exc, exc_info=True)
                app.logger.error("Can't create the dir: {0}".format(exc))
                return "Can't save the file", 500
    else:
        directories = [STORE_DIR, file_dir]
        for directory in directories:
            try:
                os.mkdir(directory)
            except (IOError, OSError) as exc:  # noqa: WPS440
                app.logger.debug(exc, exc_info=True)
                app.logger.error("Can't create the dir: {0}".format(exc))
                return "Can't save the file", 500
    try:
        upload_file.save(file_path)
    except (IOError, OSError) as exc:  # noqa: WPS440
        app.logger.debug(exc, exc_info=True)
        app.logger.error("Can't save the file: {0}".format(exc))
        return "Can't save the file", 500
    return {'hash': file_hash}


@app.route('/download/<file_hash>', methods=['GET'])
def download(file_hash):
    """Return file by received hash."""
    if not values.is_correct_hash(file_hash):
        app.logger.error('Bad hash format: {0}'.format(file_hash))
        return 'Bad hash format', 400
    file_path = os.path.join(STORE_DIR, file_hash[:2], file_hash)
    if not os.path.exists(file_path):
        app.logger.error("This file doesn't exist: {0}".format(file_path))
        return "This file doesn't exist", 404
    try:
        return send_file(file_path, as_attachment=True)
    except (IOError, OSError) as exc:
        app.logger.debug(exc, exc_info=True)
        app.logger.error("Can't download the file: {0}".format(exc))
        return "Can't download the file", 500


@app.route('/delete/<file_hash>', methods=['DETELE'])
def delete(file_hash):
    """Delete file from the store by received hash."""
    if not values.is_correct_hash(file_hash):
        app.logger.error('Bad hash format: {0}'.format(file_hash))
        return 'Bad hash format', 400
    file_path = os.path.join(STORE_DIR, file_hash[:2], file_hash)
    if not os.path.exists(file_path):
        app.logger.error("This file doesn't exist: {0}".format(file_path))
        return "This file doesn't exist", 404
    try:
        os.remove(file_path)
    except (IOError, OSError) as exc:
        app.logger.debug(exc, exc_info=True)
        app.logger.error("Can't delete the file: {0}".format(exc))
        return "Can't delete the file", 500
    file_dir = os.path.dirname(file_path)
    directories = [file_dir, STORE_DIR]
    for directory in directories:
        if not os.listdir(directory):
            try:
                os.rmdir(directory)
            except (IOError, OSError) as exc:  # noqa: WPS440
                app.logger.debug(exc, exc_info=True)
                app.logger.error("Can't delete the dir: {0}".format(exc))
    return 'File was deleted'


if __name__ == '__main__':
    app.run(debug=True, port=LOCAL_PORT)  # noqa: S201
