
let waitingIO = false;


// создать новую заявку на сервере
function addState () {
    if (waitingIO) {
        return;
    }
    const theme = document.getElementById('form-theme').value;
    let whom = document.getElementById('form-whom').value;
    const info = document.getElementById('form-info').value;
    waitingIO = true;
    if (!whom) {
        whom = 'для всех';
    }
    $.ajax({
        type: "post",
        url: "/connect_statements",
        data: {name: theme, for_whom: whom, message: info},
        dataType: "text",
        timeout: 5000,
        success: function (response, textstatus, xhr) {
            if (xhr.status == 200) {
                // alert('Заявка принята');
                destroyWin();
                waitingIO = false;
                loadOpenStatements();
            } else {
                alert('Не удалось отправить заявку');
                waitingIO = false;
            }
        },
        error: function (response) {
            alert('Не удалось отправить заявку');
            waitingIO = false;
        } 
    });
}


// загрузить список открытых заявок
function loadOpenStatements () {
    $.ajax({
        type: "get",
        url: "/connect_statements/open",
        dataType: "json",
        timeout: 5000,
        success: function (response) {
            if (!Array.isArray(response)) {
                alert('Сервер отдал некорректный ответ');
                return;
            } else {
                $('.list-box').html('');
                $('.list-close-box').html('');
                response.forEach(element => {
                    let status = '';
                    let statusClass = '';
                    switch (element.status) {
                        case 1:
                            status = 'Открыто';
                            statusClass = 'status-open';
                            break;
                        case 2:
                            status = 'Ожидает ответа';
                            statusClass = 'status-wait';
                            break;
                        case 0:
                            status = 'Закрыто';
                            statusClass = 'status-close';
                            break;
                    }
                    let defaultForWhomColor = 'green';
                    if (element.for_whom_color) {
                        defaultForWhomColor = element.for_whom_color;
                    }
                    const content = `
                    <div class="statement" id="id-${element.id}" draggable="true" ondragstart="drag(event)">
                        <div class="statement-date">${element.date}</div>
                        <div class="statement-label">
                            <a class="statement-name" href="javascript: createWinChangeState(${element.id})">${element.name}</a>
                            <a class="statement-whom" href="javascript: createWinChangeWhom(${element.id})" style="color: ${defaultForWhomColor};border: 2px solid ${defaultForWhomColor}">${element.for_whom}</a>
                        </div>
                        <div class="statement-state">
                            <div class="state-box ${statusClass}">${status}</div>
                            <a class="a-btn close-btn" href="javascript: closeStatement(${element.id})">Закрыть</a>
                        </div>
                    </div>
                    <div id="sep-${element.id}" class="separator-statement" ondrop="drop(event)" ondragenter="enterDrag(event)" ondragleave="leaveDrag(event)" ondragover="overDrag(event)"></div>
                    `
                    $(content).appendTo('.list-box');
                });
            }
            
        },
        error: function () {
            alert('Не удалось загрузить список заявок')
        }
    });
}

// открыть окно изменения надписи кому адресована заявка
function changeForWhom(id) {
    
}

// загрузить список закрытых заявок
function loadCloseStatements () {
    $.ajax({
        type: "get",
        url: "/connect_statements/close",
        dataType: "json",
        timeout: 5000,
        success: function (response) {
            if (!Array.isArray(response)) {
                alert('Сервер отдал некорректный ответ');
                return;
            } else {
                $('.list-close-box').html('');
                response.forEach(element => {
                    let status = '';
                    let statusClass = '';
                    switch (element.status) {
                        case 1:
                            status = 'Открыто';
                            statusClass = 'status-open';
                            break;
                        case 2:
                            status = 'Ожидает ответа';
                            statusClass = 'status-wait';
                            break;
                        case 0:
                            status = 'Закрыто';
                            statusClass = 'status-close';
                            break;
                    }
                    const content = `
                    <div class="statement" id="id-${element.id}">
                        <div class="statement-date">${element.date}</div>
                        <div class="statement-label">
                            <div class="statement-number">${element.id}</div>
                            <a class="statement-name" href="javascript: createWinChangeState(${element.id})">${element.name}</a>
                            <div class="statement-whom">${element.for_whom}</div>
                        </div>
                        <div class="statement-state">
                            <div class="state-box ${statusClass}">${status}</div>
                        </div>
                    </div>
                    `
                    $(content).appendTo('.list-close-box');
                });
            }
            
        },
        error: function () {
            alert('Не удалось загрузить список заявок')
        }
    });
}


// закрыть заявку 
function closeStatement (id) {
    $.ajax({
        type: "post",
        url: "/connect_statements/" + id,
        data: {status: 0},
        timeout: 5000,
        dataType: "text",
        success: function (response, _ ,xhr) {
            if (xhr.status == 200) {
                $('#id-' + id).slideUp(500);
                setTimeout(function() {
                    $('#id-' + id).remove()
                }, 500)
            } else {
                alert('Не удалось закрыть заявку');
            }
        },
    });
}

// отправить сообщение
function sendMessage (id) {
    $.ajax({
        type: "post",
        url: "/connect_statements/" + id,
        data: {message: $('.send-input').val(), status: 2},
        dataType: "text",
        timeout: 5000,
        success: function (response, _ ,xhr) {
            if (xhr.status == 200) {
                updateMessages(id);
                $('.send-input').val('');
            } else {
                alert('Не удалось отправить сообщение');
            }
        },
    });
}

// изменить дополнительную надпись 
function sendForWhom (id) {
    $.ajax({
        type: "post",
        url: "/connect_statements/" + id,
        data: {for_whom_color: $('input[name="color-pick"]:checked').val(), for_whom: $('#for_whom_input').val()},
        dataType: "text",
        timeout: 5000,
        success: function (response, _ ,xhr) {
            window.location.href = '/connect_statements';
        },
        error: function (response) {
            alert('Не удалось отправить форму');
        }
    });
}

// обновить сообщения
function updateMessages (id) {
    $.ajax({
        type: "get",
        url: "/connect_statements/" + id,
        dataType: "json",
        timeout: 5000,
        success: function (response, _ ,xhr) {
            if (xhr.status == 200) {
                $('.window-middle').html('');
                response.messages.forEach(message => {
                    let content = `<div class="message">
                                    <div class="msg-text">${message.message.replaceAll('\n', '<br>')}</div>
                                    <div class="msg-box">
                                        <div class="msg-sender">${message.sender}</div>
                                        <div class="msg-date">${message.date}</div>
                                    </div>
                                </div>`
                    $(content).appendTo('.window-middle');
                });
            } else {
                alert('Не удалось обновить список сообщений');
            }
        },
    });
}

function overDrag(e) {
    e.preventDefault();
    //console.log(e);
}

function enterDrag(e) {
    e.preventDefault();
    e.target.style.backgroundColor = 'black';
}

function leaveDrag(e) {
    e.preventDefault();
    e.target.style.backgroundColor = 'transparent';
} 

function drag(e) {
    e.dataTransfer.setData("text", e.target.id);
    console.log(e.target.id);
} 

function drop(e) {
    e.preventDefault();
    e.target.style.backgroundColor = 'transparent';
    let data = e.dataTransfer.getData("text");
    console.log(e.target.id);

    $.ajax({
        timeout: 1000,
        type: "post",
        url: "/connect_statements/replace",
        data: {drag: data, drop: e.target.id},
        dataType: "text",
        success: function (response) {
            loadOpenStatements();
        },
        error: function (response) {
            alert('Не удалось переместить элемент');
            window.location.href = '/connect_statements';
        }
    });
}




window.onload = function () {
    console.log('page on ready');
    loadOpenStatements();
}