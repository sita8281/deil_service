from app import app, db, models
from flask import render_template, jsonify, request, abort
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import pickle
import logging


log = logging.getLogger('connect_statements')


@app.route('/connect_statements', methods=['GET'])
@login_required
def connect_statements():
    log.info(f'{current_user.login}: посетил страницу')
    return render_template('/connect_statements/index.html')


@app.route('/connect_statements/<endp>', methods=['GET'])
@login_required
def connect_statements_list(endp):
    if endp == 'open':
        # получить открытые и ожидающие ответа заявки
        statements = db.session.query(
            models.ConnectStatements
        ).filter(models.ConnectStatements.status >= 1).all()
        log.info(f'{current_user.login}: запросил список открытых и ожидающих ответа заявок')
    elif endp == 'close':
        # получить закрытые заявки
        statements = db.session.query(
            models.ConnectStatements
        ).filter(models.ConnectStatements.status == 0).all()
        log.info(f'{current_user.login}: запросил список закрытых заявок')
    else:
        return abort(404)
    return jsonify([statement.to_serializeble for statement in statements][::-1])


@app.route('/connect_statements', methods=['POST'])
@login_required
def connect_statements_add():
    form = request.form
    date: str = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    messages: list = [
        {
            'sender': current_user.login,
            'date': date,
            'message': form.get('message')
        }
    ]
    db.session.add(
        models.ConnectStatements(
            name=form.get('name'),
            date=date,
            for_whom=form.get('for_whom'),
            status=1,
            messages=pickle.dumps(messages)
            )
        )
    try:
        db.session.flush()
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        log.info(f'{current_user.login}: ошибка БД при создании заявки')
        return abort(500)
    log.info(f'{current_user.login}: создал новую заявку <{form.get("name")}>')
    return 'OK', 200


@app.route('/connect_statements/<int:iid>', methods=['POST', 'GET'])
@login_required
def connect_statements_resource(iid):

    statement = db.session.query(models.ConnectStatements).get_or_404(iid)
    if request.method == 'GET':
        messages: list = pickle.loads(statement.messages)
        log.info(f'{current_user.login}: запросил данные заявки <{statement.name}> | <id={statement.id}>')
        return jsonify({
            'messages': messages,
            'name': statement.name,
            'status': statement.status

        })
    form = request.form

    if form.get('message'):
        date: str = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        messages: list = pickle.loads(statement.messages)
        messages.append({'sender': current_user.login, 'date': date, 'message': form['message']})
        statement.messages = pickle.dumps(messages)
        log.info(f'{current_user.login}: отправил сообщение <{form["message"]}>'
                 f' в заявку <{statement.name}> | <id={statement.id}>')
    if form.get('status'):
        statement.status = int(form['status'])
    if form.get('for_whom'):
        statement.for_whom = form['for_whom']
    try:
        db.session.flush()
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        return abort(500)
    return 'OK', 200




