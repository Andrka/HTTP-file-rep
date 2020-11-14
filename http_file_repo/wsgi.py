# -*- coding:utf-8 -*-

"""WSGI entry point."""

from http_file_repo.app import app

if __name__ == '__main__':
    app.run()
