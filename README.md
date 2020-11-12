## HTTP-file-rep

HTTP-file-rep is a written in Python (using Flask) HTTP API for upload, download and delete files. This app serving with Gunicorn using daemon mode.

### Built With

- Python
- Flask
- Gunicorn

### Prerequisites

Before you continue, ensure you have met the following requirements:

- You are using a Linux or Mac OS machine. Windows is not supported;
- You have installed the latest versions of Python and pip on your computer;

This project uses Poetry for dependency and virtual environment management. 

### Installation

1) Clone the repo:

`git clone https://github.com/Andrka/HTTP-file-rep.git`

2) To install the required dependencies and set up a virtual environment run in the cloned directory (poetry command):

`poetry install`

or install requirements using requirements.txt by yourself:

`pip install --user --upgrade -r requirements.txt`

### Usage

By default, HTTP API Daemon will be on ____ port. This can be changed in ____.
To start HTTP API Daemon run in the cloned directory:

`make run`

To stop:

`make stop`

(commands from Makefile)

1) Uploading:

2) Downloading:

3) Deleting:


### Development

To run tests you can run Makefile command (poetry is needed):

`make check`