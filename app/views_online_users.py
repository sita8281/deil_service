from app import app, forms, db, models, views_permission
from flask import render_template, request, redirect, url_for, flash, session, send_file, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from .modules import sessions_online


@app.route('/is_online', methods=['POST'])
@login_required
def is_online():
    sessions_online.connect(
        session_token=request.cookies.get('session'),
        #remote_ip=str(request.headers.get('X-Real-Ip'))
        remote_ip=request.remote_addr
    )
    return 'Connected', 200


@app.route('/online', methods=['GET'])
@login_required
def users_online():
    print(sessions_online.get_connections)
    return jsonify(sessions_online.get_connections), 200

