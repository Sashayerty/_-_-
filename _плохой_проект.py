from flask import Flask

проект = Flask(__name__)
рука = проект.route
запускай = проект.run
__имя__ = "__главный__"


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
