from flask import Flask as Управлялка
from langchain.chat_models import init_chat_model as сделай_мне_разговорник
from pydantic import BaseModel as БазоваяМодель
from pydantic import Field as Поле

строка = str
__имя__ = "__главный__"
проект = Управлялка(__имя__)
рука = проект.route
запускай = проект.run
наша_модель_для_общения = сделай_мне_разговорник(
    model="mistral-small-latest", model_provider="mistralai"
)


class ВыходныеДанныеОтИИ(БазоваяМодель):
    идея_проекта: строка = Поле(description="Ты мне должен дать идею проекта")
    описание_проекта: строка = Поле(description="Описание проекта")
    убийственная_фишка_проекта: строка = Поле(
        description="Киллерфича проекта, в чем его прикол."
    )


@рука("/главная", methods=["POST", "GET"])
def поехали():
    return "Привет"


@рука("/зарегистрируй-пж", methods=["POST", "GET"])
def зарегистрируй_пж():
    return "ок"


@рука("/войди-пж", methods=["POST", "GET"])
def войди_пж():
    return "да"


if __имя__ == "__главный__":
    запускай(debug="Правда")
