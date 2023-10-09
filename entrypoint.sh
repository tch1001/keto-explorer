#!/bin/bash
export $(cat .env | xargs)
gunicorn -b 0.0.0.0:5001 "app:create_app()"
