## HTTP-file-repo

[![Build Status](https://travis-ci.org/Andrka/HTTP-file-repo.svg?branch=main)](https://travis-ci.org/Andrka/HTTP-file-repo) [![Github Actions Status](https://github.com/Andrka/HTTP-file-repo/workflows/Python%20CI/badge.svg)](https://github.com/Andrka/HTTP-file-repo/actions)

HTTP-file-repo is a written in Python (using Flask) HTTP API for upload, download and delete files. This app is serving by Gunicorn in daemon mode.

You can upload, download and delete files.

Upload: app receives file (with POST method), returns his hash and saves file to 'store/ab/abcdef12345...', where 'ab' is first two letters of file hash and 'abcdef12345...' - new file name from full file hash.

Download: app receives file hash (with GET method) and returns file if it exists.

Delete: app receives file hash (with DELETE method) and deletes file if it exists.

### Prerequisites

Before you continue, ensure you have met the following requirements:

- You are using a Linux machine;
- You have installed the latest versions of Python and pip on your computer.

This project uses [Poetry](https://python-poetry.org/) for dependency and virtual environment management. 

### Installation

1) Clone the repo:

`git clone https://github.com/Andrka/HTTP-file-repo.git`

2) To install the required dependencies and set up a virtual environment run in the cloned directory (using poetry):

`poetry install`

or install requirements using requirements.txt by yourself:

`pip install --user --upgrade -r requirements.txt`

### Usage

By default, HTTP API Daemon will be on 8001 port.

To start HTTP API Daemon run in the cloned directory (poetry is needed):

`make run`

Or use bash command (without poetry):

`gunicorn --bind 0.0.0.0:8001 HTTP-file-repo.wsgi:app --daemon`

To stop:

`make stop`

(kill -9 \`ps aux | grep gunicorn | grep http_file_repo | awk '{ print $2 }'\`)

1) Uploading file:

After attempting to POST file to the `server_domain_name_or_IP_address/upload` you can receive next HTTP codes:
- 200 - if file was uploaded
- 400 - if request did not contain file
- 409 - if file already exists
- 500 - if server had IO errors

2) Downloading file:

After attempting to GET file from the `server_domain_name_or_IP_address/download/file_hash` you can receive next HTTP codes:
- 200 - if file was downloaded
- 400 - if given file hash was incorrect
- 404 - if file does not exist
- 500 - if server had IO errors

3) Deleting file:

After attempting to DELETE file from the `server_domain_name_or_IP_address/delete/file_hash` you can receive next HTTP codes:
- 200 - if file was deleted
- 400 - if given file hash was incorrect
- 404 - if file does not exist
- 500 - if server had IO errors

### Development

To run tests you can run Makefile command (poetry is needed):

`make check`