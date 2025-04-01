import sqlalchemy as хз_как_назвать
import sqlalchemy.orm as управление_базой_данных
from dotenv import dotenv_values as дай_мне_переменные_виртуального_окружения
from flask import Flask as Управлялка
from flask import redirect as перенеси
from flask import render_template_string as покажи_мне_строчку
from flask import request as запрос
from flask_login import LoginManager as МенеджерВходов
from flask_login import UserMixin as МодельПользователя
from flask_login import login_user as войти_пользователю
from langchain_core.prompts import ChatPromptTemplate as ШаблонДляПромпта
from langchain_mistralai import ChatMistralAI as ФранцузДляОбщения
from pydantic import BaseModel as БазоваяМодель
from pydantic import Field as Поле

строка = str
БазоваяМодельДляВхода = управление_базой_данных.declarative_base()
__имя__ = "__главный__"
проект = Управлялка(__имя__)
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
<html>
<head>
<meta charset="UTF-8">
<style>
body {
    background: #8B4513 url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="%234B3621"/><circle cx="25" cy="25" r="10" fill="%238B4513"/><circle cx="75" cy="25" r="10" fill="%238B4513"/><circle cx="25" cy="75" r="10" fill="%238B4513"/><circle cx="75" cy="75" r="10" fill="%238B4513"/></svg>');
    color: #FFF;
    font-family: 'Times New Roman', serif;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

.кнопкоКонтейнер {
    position: relative;
    width: 100vw;
    height: 100vh;
}

.убегающаяКнопка {
    position: absolute;
    padding: 20px 40px;
    font-size: 24px;
    cursor: pointer;
    border: 3px solid #A0522D;
    border-radius: 10px;
    transition: all 0.3s;
    box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
    text-shadow: 1px 1px 2px #000;
}

#кнопкаВхода {
    background: #556B2F;
    color: #FFF8DC;
}

#кнопкаРегистрации {
    background: #6B8E23;
    color: #FFF8DC;
}

h1 {
    text-align: center;
    margin-top: 30px;
    font-size: 36px;
    color: #FFF8DC;
    text-shadow: 2px 2px 4px #000;
    padding: 20px;
    background: rgba(139, 69, 19, 0.7);
    border-radius: 10px;
    margin: 20px auto;
    width: fit-content;
}

.модальноеОкно {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #A0522D;
    padding: 30px;
    border: 5px solid #8B4513;
    border-radius: 15px;
    box-shadow: 0 0 30px rgba(0,0,0,0.7);
    z-index: 1000;
    width: 300px;
}

.модальноеОкно h2 {
    color: #FFF8DC;
    text-align: center;
    margin-bottom: 20px;
}

.формаГруппа {
    margin-bottom: 20px;
}

.формаГруппа label {
    display: block;
    margin-bottom: 5px;
    color: #FFF8DC;
}

.формаГруппа input {
    width: 100%;
    padding: 10px;
    border: 2px solid #8B4513;
    border-radius: 5px;
    background: #FFF8DC;
}

.кнопкаОтправки {
    background: #6B8E23;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    font-size: 18px;
}

.кнопкаОтправки:hover {
    background: #556B2F;
}

.уведомление-контейнер {
    position: fixed;
    bottom: 20px;
    left: 0;
    right: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 10000;
    pointer-events: none;
}

.уведомление {
    background: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 15px 25px;
    border-radius: 8px;
    margin-bottom: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.3s ease;
    max-width: 80%;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.уведомление.show {
    transform: translateY(0);
    opacity: 1;
}

.уведомление.success {
    background: rgba(46, 125, 50, 0.9);
}

.уведомление.error {
    background: rgba(198, 40, 40, 0.9);
}

.прогресс-бар {
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
</style>
</head>
<body>
<h1>ПОЙМАЙТЕ КНОПКУ</h1>
<div class="уведомление-контейнер" id="уведомление-контейнер"></div>

<div class="кнопкоКонтейнер">
    <button id="кнопкаВхода" class="убегающаяКнопка">ВХОД</button>
    <button id="кнопкаРегистрации" class="убегающаяКнопка">РЕГИСТРАЦИЯ</button>
</div>


<div id="модальноеРегистрация" class="модальноеОкно">
    <h2>Регистрация</h2>
    <form id="формаРегистрации" method="POST" action="/главная?вид=регистрация">
        <div class="формаГруппа">
            <label for="никнейм">Никнейм (2-15 символов):</label>
            <input type="text" id="никнейм" name="никнейм" required minlength="2" maxlength="15">
        </div>
        <div class="формаГруппа">
            <label for="пароль">Пароль (2-15 символов):</label>
            <input type="пароль_пользователяword" id="пароль" name="пароль" required minlength="2" maxlength="15">
        </div>
        <button type="submit" class="кнопкаОтправки">Зарегистрироваться</button>
    </form>
</div>

<script>
const всеКнопки = document.querySelectorAll('.убегающаяКнопка');
let кнопкаПоймана = false;
let скоростьПеремещения = 3000;
const модальноеОкно = document.getElementById('модальноеРегистрация');

function показатьУведомление(текст, тип = 'info') {
    const контейнер = document.getElementById('уведомление-контейнер');
    const уведомление = document.createElement('div');
    уведомление.className = `уведомление ${тип}`;
    уведомление.innerHTML = `
        ${текст}
        <div class="прогресс-бар"></div>
    `;
    
    контейнер.appendChild(уведомление);
    
    setTimeout(() => {
        уведомление.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        уведомление.classList.remove('show');
        setTimeout(() => {
            контейнер.removeChild(уведомление);
        }, 300);
    }, 5000);
}

function перемешатьКнопки() {
    if(кнопкаПоймана) return;
    
    всеКнопки.forEach(кнопка => {
        const x = Math.random() * (window.innerWidth - 200);
        const y = Math.random() * (window.innerHeight - 100);
        кнопка.style.left = `${x}px`;
        кнопка.style.top = `${y}px`;
        кнопка.style.transform = `rotate(${Math.random() * 10 - 5}deg)`;
    });
    
    setTimeout(перемешатьКнопки, скоростьПеремещения);
}

всеКнопки.forEach(кнопка => {
    кнопка.addEventListener('mouseover', () => {
        if(!кнопкаПоймана) {
            const x = Math.random() * (window.innerWidth - 200);
            const y = Math.random() * (window.innerHeight - 100);
            кнопка.style.transition = 'all 1s ease';
            кнопка.style.left = `${x}px`;
            кнопка.style.top = `${y}px`;
            
            setTimeout(() => {
                кнопка.style.transition = 'all 0.3s ease';
            }, 1000);
        }
    });
    
    кнопка.addEventListener('click', (e) => {
        e.stopPropagation();
        кнопкаПоймана = true;
        кнопка.style.border = '3px solid #FFF';
        кнопка.style.boxShadow = '0 0 20px #FFF';
        кнопка.textContent = 'УСПЕХ!';
        кнопка.style.transform = 'scale(1.2) rotate(0deg)';
        кнопка.style.transition = 'all 0.5s ease';
        
        setTimeout(() => {
            if(кнопка.id === 'кнопкаРегистрации') {
                модальноеОкно.style.display = 'block';
            } else {
                показатьУведомление('Поздравляем! Вы поймали кнопку входа!', 'success');
            }
        }, 500);
    });
});

window.addEventListener('click', (e) => {
    if(e.target === модальноеОкно) {
        модальноеОкно.style.display = 'none';
        кнопкаПоймана = false;
        document.getElementById('кнопкаРегистрации').textContent = 'РЕГИСТРАЦИЯ';
    }
});

document.getElementById('формаРегистрации').addEventListener('submit', function(e) {
    const никнейм = document.getElementById('никнейм').value;
    const пароль = document.getElementById('пароль').value;
    
    if(никнейм.length < 2 || никнейм.length > 15) {
        e.preventDefault();
        показатьУведомление('Никнейм должен быть от 2 до 15 символов!', 'error');
        return;
    }
    
    if(пароль.length < 2 || пароль.length > 15) {
        e.preventDefault();
        показатьУведомление('Пароль должен быть от 2 до 15 символов!', 'error');
        return;
    }
});


всеКнопки[0].style.left = '30%';
всеКнопки[0].style.top = '40%';
всеКнопки[1].style.left = '60%';
всеКнопки[1].style.top = '40%';

перемешатьКнопки();
</script>
</body>
</html>
"""


@логин_менеджер.user_loader
def загрузи_пользователя(ид_пользователя):
    return Пользователь.query.get(int(ид_пользователя))


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
    идея_проекта: строка = Поле(description="Ты мне должен дать идею проекта")
    описание_проекта: строка = Поле(description="Описание проекта")
    убийственная_фишка_проекта: строка = Поле(
        description="Киллерфича проекта, в чем его прикол."
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


@рука("/главная", methods=["POST", "GET"])
def поехали():
    global база_данных_пользователей
    if запрос.method == "POST":
        имя = запрос.form.get("никнейм")
        пароль = запрос.form.get("пароль")
        вид = запрос.args.get("вид")

        if вид == "вход":
            if найди_в_базе_данных_пользователя(имя, пароль):
                пользователь = Пользователь.query.filter_by(
                    имя_пользователя=имя
                ).first()
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
                return f"Пользователь уже существует! Его пароль: {дай_данные_пользователя(имя_пользователя=имя)["пароль_пользователя"]}"

    return покажи_мне_строчку(source=ШАБЛОН)


@рука("/зарегистрируй-пж", methods=["POST", "GET"])
def зарегистрируй_пж():
    вопрос = цепочка_для_генерации_проекта.invoke(
        {"тема_для_проекта": "Программирование"}
    )
    return вопрос.убийственная_фишка_проекта + "\n" + вопрос.идея_проекта


@рука("/войди-пж", methods=["POST"])
def войди_пж():
    return "да"


if __имя__ == "__главный__":
    запускай(debug="Правда")
