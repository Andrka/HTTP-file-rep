## HTTP-file-repo

HTTP-file-repo is a written in Python (using Flask) HTTP API for upload, download and delete files. This app is serving with Gunicorn in daemon mode.

You can upload, download and delete files.

Upload: app receives file, returns his hash and saves file to 'store/ab/abcdef12345...', where 'ab' is first two letters of file hash and 'abcdef12345...' - new file name from full file hash.

Download: app receives file hash and returns file if it exists.

Delete: app receives file hash and deletes file if it exists.

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

To start HTTP API Daemon run in the cloned directory:

`make run`

(bash command: gunicorn --bind 0.0.0.0:8001 http_file_repo.wsgi:app --daemon)

To stop:

`make stop`

(bash command: kill -9 \`ps aux | grep gunicorn | grep http_file_repo | awk '{ print $2 }'\`)

1) Uploading file:

2) Downloading file:

3) Deleting file:


### Development

To run tests you can run Makefile command (poetry is needed):

`make check`