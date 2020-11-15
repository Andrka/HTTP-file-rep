#!/usr/bin/env bash
set -o errexit -o pipefail
kill -9 `ps aux | grep gunicorn | grep HTTP-file-repo | awk '{ print $2 }'`