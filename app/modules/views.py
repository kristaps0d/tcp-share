from flask import Flask, render_template, request
import datetime

from app import app

from app.modules.manager.files import AvailableFiles

URL, URN = '/static/public/', AvailableFiles()
URLS = [[f, URL + f] for f in URN]

@app.route('/')
def index():
    ip = request.access_route[-1]
    ua = request.headers.get('User-Agent')
    return render_template('index.html', urls=URLS, ipaddr=ip, useragent=ua, title=f'- {datetime.date.today()} -')

@app.errorhandler(404)
def error(e):
    ip = request.remote_addr
    return render_template('error.html', ipaddr=ip, title=f'- {datetime.date.today()} -')
