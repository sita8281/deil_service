from flask import request, render_template
from app import app


@app.route('/cfg/')
def configs():
    return render_template('cfg_storage/index.html')
