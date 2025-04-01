import sqlalchemy as хз_как_назвать
import sqlalchemy.orm as управление_базой_данных
from dotenv import dotenv_values as дай_мне_переменные_виртуального_окружения
from flask import Flask as Управлялка
from flask import jsonify as переведи_в_формат_для_фронтенда
from flask import redirect as перенеси
from flask import render_template_string as покажи_мне_строчку
from flask import request as запрос
from flask_login import LoginManager as МенеджерВходов
from flask_login import UserMixin as МодельПользователя
from flask_login import login_required as нужен_пользователь
from flask_login import login_user as войти_пользователю
from flask_login import logout_user as выйти_пользователю
from langchain_core.prompts import ChatPromptTemplate as ШаблонДляПромпта
from langchain_mistralai import ChatMistralAI as ФранцузДляОбщения
from pydantic import BaseModel as БазоваяМодель
from pydantic import Field as Поле

строка = str
Ничего = None
скажи_мне_кто_ты = print
БазоваяМодельДляВхода = управление_базой_данных.declarative_base()
__имя__ = "__главный__"
проект = Управлялка(__имя__)
проект.config["SECRET_KEY"] = дай_мне_переменные_виртуального_окружения(
    "./.переменные"
)["СЕКРЕТНЫЙ_КЛЮЧ"]
рука = проект.route
запускай = проект.run
наша_модель = ФранцузДляОбщения(
    model="mistral-small-latest",
    temperature=1.0,
    api_key=дай_мне_переменные_виртуального_окружения("./.переменные")[
        "АПИ_КЛЮЧ_ФРАНЦУЗА"
    ],
)
промпт = ШаблонДляПромпта.from_messages(
    [
        (
            "system",
            "Ты ассистент для создания максимально"
            "абсурдных идей для проектов.",
        ),
        (
            "human",
            "Создай мне идею для максимально абсурдного проекта на тему"
            "{тема_для_проекта}",
        ),
    ]
)
логин_менеджер = МенеджерВходов()
логин_менеджер.init_app(проект)

ШАБЛОН = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Генератор абсурдных бизнес-идей</title>
    <style>
        :root {
            --primary: #8B4513;
            --secondary: #A0522D;
            --accent: #6B8E23;
            --text-light: #FFF8DC;
            --text-dark: #333;
            --error: #8B0000;
            --success: #556B2F;
            --highlight: #FFD700;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background: var(--primary) url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="%234B3621"/><circle cx="25" cy="25" r="10" fill="%238B4513"/><circle cx="75" cy="25" r="10" fill="%238B4513"/><circle cx="25" cy="75" r="10" fill="%238B4513"/><circle cx="75" cy="75" r="10" fill="%238B4513"/></svg>');
            color: var(--text-light);
            font-family: 'Times New Roman', serif;
            line-height: 1.6;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin: 20px auto;
            font-size: 2.5rem;
            color: var(--text-light);
            text-shadow: 2px 2px 4px #000;
            padding: 20px;
            background: rgba(139, 69, 19, 0.7);
            border-radius: 10px;
            width: fit-content;
            max-width: 90%;
        }

        .button-container {
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }

        .runaway-button {
            position: absolute;
            padding: 15px 30px;
            font-size: 1.2rem;
            cursor: pointer;
            border: 3px solid var(--secondary);
            border-radius: 10px;
            transition: all 0.3s;
            box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
            text-shadow: 1px 1px 2px #000;
            z-index: 10;
        }

        #loginButton {
            background: var(--success);
            color: var(--text-light);
        }

        #registerButton {
            background: var(--accent);
            color: var(--text-light);
        }

        .modal {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: var(--secondary);
            padding: 25px;
            border: 5px solid var(--primary);
            border-radius: 15px;
            box-shadow: 0 0 30px rgba(0,0,0,0.7);
            z-index: 1000;
            width: 90%;
            max-width: 400px;
        }

        .modal h2 {
            color: var(--text-light);
            text-align: center;
            margin-bottom: 20px;
            font-size: 1.8rem;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: var(--text-light);
            font-size: 1.1rem;
        }

        .form-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid var(--primary);
            border-radius: 5px;
            background: var(--text-light);
            font-size: 1rem;
            font-family: inherit;
        }

        .submit-button {
            background: var(--accent);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 1.1rem;
            transition: all 0.3s;
            margin-top: 10px;
        }

        .submit-button:hover {
            background: var(--success);
            transform: translateY(-2px);
        }


        .idea-menu {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: var(--secondary);
            padding: 30px;
            border: 5px solid var(--primary);
            border-radius: 15px;
            box-shadow: 0 0 30px rgba(0,0,0,0.7);
            z-index: 1001;
            width: 90%;
            max-width: 700px;
            max-height: 90vh;
            overflow-y: auto;
        }

        .idea-menu h2 {
            color: var(--text-light);
            text-align: center;
            margin-bottom: 25px;
            font-size: 2rem;
        }

        .idea-textarea {
            width: 100%;
            height: 180px;
            padding: 15px;
            border: 2px solid var(--primary);
            border-radius: 5px;
            background: var(--text-light);
            margin-bottom: 25px;
            resize: none;
            font-family: inherit;
            font-size: 1rem;
        }

        .result-container {
            margin-top: 30px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 25px;
            color: white;
        }

        .result-block {
            margin-bottom: 25px;
            padding-bottom: 25px;
            border-bottom: 1px dashed rgba(255, 255, 255, 0.3);
        }

        .result-block:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }

        .result-title {
            font-weight: bold;
            color: var(--highlight);
            margin-bottom: 15px;
            font-size: 1.3rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .result-text {
            white-space: pre-line;
            text-align: justify;
            font-size: 1.1rem;
            line-height: 1.7;
        }

        #logoutButton {
            background: var(--error) !important;
            margin-top: 25px;
        }

        .notification-container {
            position: fixed;
            bottom: 30px;
            left: 0;
            right: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 10000;
            pointer-events: none;
        }

        .notification {
            background: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 18px 30px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.3);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.4s ease;
            max-width: 90%;
            text-align: center;
            position: relative;
            overflow: hidden;
            font-size: 1.1rem;
        }

        .notification.show {
            transform: translateY(0);
            opacity: 1;
        }

        .notification.success {
            background: rgba(46, 125, 50, 0.95);
        }

        .notification.error {
            background: rgba(198, 40, 40, 0.95);
        }

        .progress-bar {
            position: absolute;
            bottom: 0;
            left: 0;
            height: 4px;
            background: rgba(255, 255, 255, 0.5);
            width: 100%;
            transform-origin: left;
            animation: progress 5s linear forwards;
        }

        @keyframes progress {
            0% { transform: scaleX(1); }
            100% { transform: scaleX(0); }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .result-block {
            animation: fadeIn 0.6s ease-out forwards;
        }

        .result-block:nth-child(2) {
            animation-delay: 0.2s;
        }

        .result-block:nth-child(3) {
            animation-delay: 0.4s;
        }


        @media (max-width: 768px) {
            h1 {
                font-size: 1.8rem;
                padding: 15px;
            }

            .modal {
                width: 95%;
                padding: 20px;
            }

            .idea-menu {
                padding: 20px;
            }

            .idea-textarea {
                height: 150px;
            }

            .runaway-button {
                padding: 12px 25px;
                font-size: 1rem;
            }

            .result-title {
                font-size: 1.1rem;
            }

            .result-text {
                font-size: 1rem;
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 1.5rem;
            }

            .modal h2, .idea-menu h2 {
                font-size: 1.4rem;
            }

            .submit-button {
                padding: 10px 15px;
                font-size: 1rem;
            }

            .idea-textarea {
                height: 120px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ГЕНЕРАТОР АБСУРДНЫХ БИЗНЕС-ИДЕЙ</h1>
        <div class="notification-container" id="notificationContainer"></div>

        <div class="button-container">
            <button id="loginButton" class="runaway-button">ВХОД</button>
            <button id="registerButton" class="runaway-button">РЕГИСТРАЦИЯ</button>
        </div>

        <div id="ideaMenu" class="idea-menu">
            <h2>Ваш источник вдохновения</h2>
            <textarea id="ideaField" class="idea-textarea" placeholder="Опишите тему для вашей гениальной (или безумной) бизнес-идеи..."></textarea>
            <button id="getIdeaButton" class="submit-button">Генерировать идею</button>

            <div class="result-container" id="ideaResult">
                <!-- Результат будет вставлен сюда -->
            </div>

            <button id="logoutButton" class="submit-button">Выйти</button>
        </div>

        <div id="loginModal" class="modal">
            <h2>Вход в систему</h2>
            <form id="loginForm" method="POST" action="/главная?вид=вход">
                <div class="form-group">
                    <label for="loginUsername">Никнейм:</label>
                    <input type="text" id="loginUsername" name="никнейм" required>
                </div>
                <div class="form-group">
                    <label for="loginPassword">Пароль:</label>
                    <input type="password" id="loginPassword" name="пароль" required>
                </div>
                <button type="submit" class="submit-button">Войти</button>
            </form>
        </div>

        <div id="registerModal" class="modal">
            <h2>Регистрация</h2>
            <form id="registerForm" method="POST" action="/главная?вид=регистрация">
                <div class="form-group">
                    <label for="registerUsername">Никнейм (2-15 символов):</label>
                    <input type="text" id="registerUsername" name="никнейм" required minlength="2" maxlength="15">
                </div>
                <div class="form-group">
                    <label for="registerPassword">Пароль (2-15 символов):</label>
                    <input type="password" id="registerPassword" name="пароль" required minlength="2" maxlength="15">
                </div>
                <button type="submit" class="submit-button">Зарегистрироваться</button>
            </form>
        </div>
    </div>

    <script>
        const allButtons = document.querySelectorAll('.runaway-button');
        let buttonCaught = false;
        let moveSpeed = 3000;
        const loginModal = document.getElementById('loginModal');
        const registerModal = document.getElementById('registerModal');
        const ideaMenu = document.getElementById('ideaMenu');


        function showNotification(text, type = 'info') {
            const container = document.getElementById('notificationContainer');
            const notification = document.createElement('div');
            notification.className = `notification ${type}`;
            notification.innerHTML = `
                ${text}
                <div class="progress-bar"></div>
            `;

            container.appendChild(notification);

            setTimeout(() => {
                notification.classList.add('show');
            }, 10);

            setTimeout(() => {
                notification.classList.remove('show');
                setTimeout(() => {
                    container.removeChild(notification);
                }, 300);
            }, 5000);
        }

        function moveButtons() {
            if(buttonCaught) return;

            allButtons.forEach(button => {
                const x = Math.random() * (window.innerWidth - 200);
                const y = Math.random() * (window.innerHeight - 100);
                button.style.left = `${x}px`;
                button.style.top = `${y}px`;
                button.style.transform = `rotate(${Math.random() * 10 - 5}deg)`;
            });

            setTimeout(moveButtons, moveSpeed);
        }

        function submitIdea() {
            const idea = document.getElementById('ideaField').value;
            if (!idea.trim()) {
                showNotification('Введите идею!', 'error');
                return;
            }

            const container = document.getElementById('ideaResult');
            container.innerHTML = `
                <div class="result-block">
                    <div class="result-title">⏳ Генерация идеи...</div>
                    <div class="result-text">Мы создаем для вас уникальную бизнес-идею. Подождите немного!</div>
                </div>
            `;

            fetch(`/дай-мне-идею-проекта?идея=${encodeURIComponent(idea)}`)
                .then(response => response.json())
                .then(data => {
                    container.innerHTML = `
                        <div class="result-block">
                            <div class="result-title">💡 Идея проекта</div>
                            <div class="result-text">${data.идея_проекта}</div>
                        </div>
                        <div class="result-block">
                            <div class="result-title">📝 Описание</div>
                            <div class="result-text">${data.описание_проекта}</div>
                        </div>
                        <div class="result-block">
                            <div class="result-title">🔥 Убийственная фишка</div>
                            <div class="result-text">${data.убийственная_фишка_проекта}</div>
                        </div>
                    `;
                })
                .catch(error => {
                    container.innerHTML = '';
                    showNotification('Ошибка при получении ответа', 'error');
                    console.error('Ошибка:', error);
                });
        }

        allButtons.forEach(button => {
            button.addEventListener('mouseover', () => {
                if(!buttonCaught) {
                    const x = Math.random() * (window.innerWidth - 200);
                    const y = Math.random() * (window.innerHeight - 100);
                    button.style.transition = 'all 1s ease';
                    button.style.left = `${x}px`;
                    button.style.top = `${y}px`;

                    setTimeout(() => {
                        button.style.transition = 'all 0.3s ease';
                    }, 1000);
                }
            });


            button.addEventListener('click', (e) => {
                e.stopPropagation();
                buttonCaught = true;
                button.style.border = '3px solid #FFF';
                button.style.boxShadow = '0 0 20px #FFF';
                button.textContent = 'УСПЕХ!';
                button.style.transform = 'scale(1.2) rotate(0deg)';
                button.style.transition = 'all 0.5s ease';

                setTimeout(() => {
                    if(button.id === 'registerButton') {
                        registerModal.style.display = 'block';
                    } else {
                        loginModal.style.display = 'block';
                    }
                }, 500);
            });
        });

        window.addEventListener('click', (e) => {
            if(e.target === loginModal || e.target === registerModal) {
                loginModal.style.display = 'none';
                registerModal.style.display = 'none';
                buttonCaught = false;
                document.getElementById('loginButton').textContent = 'ВХОД';
                document.getElementById('registerButton').textContent = 'РЕГИСТРАЦИЯ';
            }
        });

        document.getElementById('registerForm').addEventListener('submit', function(e) {
            const username = document.getElementById('registerUsername').value;
            const password = document.getElementById('registerPassword').value;

            if(username.length < 2 || username.length > 15) {
                e.preventDefault();
                showNotification('Никнейм должен быть от 2 до 15 символов!', 'error');
                return;
            }

            if(password.length < 2 || password.length > 15) {
                e.preventDefault();
                showNotification('Пароль должен быть от 2 до 15 символов!', 'error');
                return;
            }
        });

        document.getElementById('getIdeaButton').addEventListener('click', submitIdea);

        document.getElementById('logoutButton').addEventListener('click', function() {
            fetch('/уйди-нечисть')
                .then(response => {
                    if(response.ok) {
                        window.location.href = '/главная';
                    }
                });
        });

        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();

            const username = document.getElementById('loginUsername').value;
            const password = document.getElementById('loginPassword').value;

            if(!username || !password) {
                showNotification('Заполните все поля!', 'error');
                return;
            }

            fetch(this.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `никнейм=${encodeURIComponent(username)}&пароль=${encodeURIComponent(password)}`
            })
            .then(response => response.text())
            .then(data => {
                if(data === 'Ошибка входа!') {
                    showNotification('Неверный логин или пароль', 'error');
                } else {
                    window.location.href = '/главная?сообщение=Вход+выполнен+успешно&тип=success';
                }
            })
            .catch(error => {
                showNotification('Ошибка при входе', 'error');
            });
        });

        document.addEventListener('DOMContentLoaded', function() {
            const urlParams = new URLSearchParams(window.location.search);
            const message = urlParams.get('сообщение');
            const type = urlParams.get('тип');

            if(message && type) {
                showNotification(decodeURIComponent(message), type);


                if (message.includes('успешн') || message.includes('Вход+выполнен')) {
                    ideaMenu.style.display = 'block';
                    document.getElementById('loginButton').style.display = 'none';
                    document.getElementById('registerButton').style.display = 'none';
                    buttonCaught = true;
                }
            }
        });

        allButtons[0].style.left = '30%';
        allButtons[0].style.top = '40%';
        allButtons[1].style.left = '60%';
        allButtons[1].style.top = '40%';

        moveButtons();
    </script>
</body>
</html>
"""


@логин_менеджер.user_loader
def загрузи_пользователя(ид_пользователя):
    return дай_данные_пользователя_по_идентификатору(
        идентификационный_номер_пользователя=ид_пользователя
    )


база_данных_пользователей = """идентификационный_номер_пользователя\tимя_пользователя\tпароль_пользователя
1\tСаша\t123123123
"""


def найди_в_базе_данных_пользователя(имя_пользователя, пароль_пользователя):
    for строка in база_данных_пользователей.split("\n")[1:]:
        if строка:
            идентификационный_номер_пользователя, имя, пароль = строка.split(
                "\t"
            )
            if имя == имя_пользователя and пароль == пароль_пользователя:
                return True
    return False


def дай_данные_пользователя(имя_пользователя):
    for строка in база_данных_пользователей.split("\n")[1:]:
        if строка:
            идентификационный_номер_пользователя, имя, пароль = строка.split(
                "\t"
            )
            if имя_пользователя == имя:
                return {
                    "id": идентификационный_номер_пользователя,
                    "имя_пользователя": имя_пользователя,
                    "пароль_пользователя": пароль,
                }
    return Ничего


def дай_данные_пользователя_по_идентификатору(
    идентификационный_номер_пользователя,
):
    for строка in база_данных_пользователей.split("\n")[1:]:
        if строка:
            идентификационный_номер, имя, пароль = строка.split("\t")
            if идентификационный_номер_пользователя == идентификационный_номер:
                return Пользователь(
                    идентификационный_номер_пользователя=идентификационный_номер_пользователя,
                    имя_пользователя=имя,
                    пароль_пользователя=пароль,
                )
    return None


def добавь_в_базу_данных_пользователя(
    имя_пользователя: строка, пароль_пользователя: строка
):
    global база_данных_пользователей
    пользователь = Пользователь(
        имя_пользователя=имя_пользователя,
        пароль_пользователя=пароль_пользователя,
    )
    if найди_в_базе_данных_пользователя(
        имя_пользователя=имя_пользователя,
        пароль_пользователя=пароль_пользователя,
    ):
        for пользователь_ in база_данных_пользователей.split("\n"):
            if имя_пользователя in пользователь_:
                return f"У Вас другой пароль: {пользователь_.split("\t")[2]}"
    else:
        база_данных_пользователей = f"{база_данных_пользователей}\n{пользователь.идентификационный_номер_пользователя}\t{пользователь.имя_пользователя}\t{пользователь.пароль_пользователя}"
        return "Все готово!"


class OutputDataFormat(БазоваяМодель):
    идея_проекта: строка = Поле(
        description="Ты мне должен дать идею бизнес проекта, который"
        "максимально окупится."
    )
    описание_проекта: строка = Поле(description="Описание бизнес проекта")
    убийственная_фишка_проекта: строка = Поле(
        description="Киллерфича бизнес проекта, в чем его прикол."
    )


class Пользователь(МодельПользователя, БазоваяМодельДляВхода):
    __tablename__ = "Пользователь"
    идентификационный_номер_пользователя = хз_как_назвать.Column(
        хз_как_назвать.Integer, primary_key=True
    )
    имя_пользователя = хз_как_назвать.Column(
        хз_как_назвать.String, nullable=False, unique=True
    )
    пароль_пользователя = хз_как_назвать.Column(
        хз_как_назвать.String, nullable=False
    )

    def get_id(self):
        return str(self.идентификационный_номер_пользователя)


структурированная_модель_француза_для_общения = (
    наша_модель.with_structured_output(OutputDataFormat)
)

цепочка_для_генерации_проекта = (
    промпт | структурированная_модель_француза_для_общения
)


@рука("/")
def да():
    return перенеси("/главная")


@рука("/главная", methods=["POST", "GET"])
def поехали():
    global база_данных_пользователей
    if запрос.method == "POST":
        имя = запрос.form.get("никнейм")
        пароль = запрос.form.get("пароль")
        вид = запрос.args.get("вид")

        if вид == "вход":
            if найди_в_базе_данных_пользователя(имя, пароль):
                данные = дай_данные_пользователя(имя_пользователя=имя)
                пользователь = Пользователь(
                    идентификационный_номер_пользователя=данные["id"],
                    имя_пользователя=данные["имя_пользователя"],
                    пароль_пользователя=данные["пароль_пользователя"],
                )
                войти_пользователю(пользователь)
                return перенеси("/главная")
            else:
                return "Ошибка входа!"
        elif вид == "регистрация":
            if not дай_данные_пользователя(имя):
                новый_id = len(база_данных_пользователей.split("\n"))
                новая_строка = f"\n{новый_id}\t{имя}\t{пароль}"
                база_данных_пользователей += новая_строка
                return "Регистрация успешна!"
            else:
                return "Пользователь уже существует!"
                "Его пароль:"
                f"{дай_данные_пользователя(имя_пользователя=имя)[
                    "пароль_пользователя"
                    ]}"

    return покажи_мне_строчку(ШАБЛОН)


@рука("/зарегистрируй-пж", methods=["POST", "GET"])
def зарегистрируй_пж():
    вопрос = цепочка_для_генерации_проекта.invoke(
        {"тема_для_проекта": "Программирование"}
    )
    return вопрос.убийственная_фишка_проекта + "\n" + вопрос.идея_проекта


@рука("/войди-пж", methods=["POST"])
def войди_пж():
    return "да"


@рука("/дай-мне-идею-проекта", methods=["POST", "GET"])
def дай_идею_для_проекта():
    идея = запрос.args.get("идея")
    вопрос = цепочка_для_генерации_проекта.invoke({"тема_для_проекта": идея})
    скажи_мне_кто_ты(
        {
            "идея_проекта": вопрос.идея_проекта,
            "описание_проекта": вопрос.описание_проекта,
            "убийственная_фишка_проекта": вопрос.убийственная_фишка_проекта,
        }
    )
    return переведи_в_формат_для_фронтенда(
        {
            "идея_проекта": вопрос.идея_проекта,
            "описание_проекта": вопрос.описание_проекта,
            "убийственная_фишка_проекта": вопрос.убийственная_фишка_проекта,
        }
    )


@рука("/уйди-нечисть", methods=["POST", "GET"])
@нужен_пользователь
def уйди_нечисть():
    выйти_пользователю()
    скажи_мне_кто_ты("Успешно!")
    return перенеси("/главная")


if __имя__ == "__главный__":
    запускай(debug="Правда")
