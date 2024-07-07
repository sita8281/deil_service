
function disableScroll() {
    document.body.style.overflow = 'hidden';
}

function enableScroll() {
    document.body.style.overflow = 'auto';
}


function createWinAddState () {
    const rootWin = document.getElementById('root-win');
    rootWin.innerHTML = `<div class="window-background">
            <div class="window">
                <div class="window-content">
                    <div class="window-top">
                        <div class="window-top-label">Новая заявка</div>
                        <a href="javascript: destroyWin()" class="window-top-close">
                            <img class="window-top-close-img" src="/static/img/cross.svg" alt="">
                        </a>
                    </div>
                    <div class="window-middle">
                        <div class="window-middle-row">
                          <label class="window-middle-label">Тема</label>
                          <input class="modal-base-input middle-input" type="text" autocomplete="off" id="form-theme">
                        </div>
                        <div class="window-middle-row">
                          <label class="window-middle-label">Для кого</label>
                          <input class="modal-base-input middle-input" type="text" autocomplete="off" placeholder="можно не заполнять" id="form-whom">
                        </div>
                        <div class="window-middle-row">
                          <label class="window-middle-label">Информация</label>
                          <textarea class="modal-base-input middle-textarea" autocomplete="off" id="form-info"></textarea>
                        </div>
                    </div>
                    <div class="window-bottom">
                        <a class="modal-base-button" href="javascript: addState()">Создать</a>
                    </div>
                </div>
                
            </div>
        </div>`
    disableScroll();
}


function createWinChangeState (id) {
    $.ajax({
        type: "get",
        url: "/connect_statements/" + id,
        dataType: "json",
        success: function (response, _ ,xhr) {
            if (xhr.status == 200) {
                const rootWin = document.getElementById('root-win');
                rootWin.innerHTML = `<div class="window-background">
                    <div class="window">
                        <div class="window-content">
                            <div class="window-top">
                                <div class="window-top-label">${response.name}</div>
                                <a href="javascript: destroyWin()" class="window-top-close">
                                    <img class="window-top-close-img" src="/static/img/cross.svg" alt="">
                                </a>
                            </div>
                            <div class="window-middle">
                                
                            </div>
                            <div class="window-bottom">
                                <input class="modal-base-input send-input" type="text">
                                <a class="modal-base-button" href="javascript: sendMessage(${id})">Отправить</a>
                            </div>
                        </div>

                    </div>
                </div>`
                updateMessages(id);
                disableScroll();
                $('.send-input').on('keydown', function (e) { 
                    //e.preventDefault();
                    if (e.key == 'Enter') {
                        sendMessage(id);
                    }
                    
                });
            } else {
                alert('Не удалось закрыть заявку');
            }
        },
    });
    
}

function destroyWin(update) {
    const rootWin = document.getElementById('root-win');
    rootWin.innerHTML = '';
    enableScroll();
    loadOpenStatements();
    
}