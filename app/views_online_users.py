from app import app, forms, db, models, views_permission
from flask import render_template, request, redirect, url_for, flash, session, send_file, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from .modules import sessions_online


@app.route('/connected', methods=['POST'])
@login_required
def is_online():
    host = request.headers.get('X-Real-Ip')
    if not host:
        host = request.remote_addr

    sessions_online.connect(
        session_token=request.cookies.get('session'),
        remote_ip=host,
    )
    return 'Connected', 200


@app.route('/online_users', methods=['GET'])
@login_required
def users_online():
    return jsonify(sessions_online.get_connections), 200


@app.route('/disconnect', methods=['POST'])
@login_required
def user_disconnect():
    return jsonify('notify', 'Вы отключили пользователя')

