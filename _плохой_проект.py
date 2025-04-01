from flask import Flask

проект = Flask(__name__)
__имя__ = "__главный__"


@проект.route("/", methods=["POST", "GET"])
def поехали():
    return "Привет"


@проект.route("/зарегистрируй-пж", methods=["POST", "GET"])
def зарегистрируй_пж():
    return "ок"


@проект.route("/войди-пж", methods=["POST", "GET"])
def войди_пж():
    return "да"


if __имя__ == "__главный__":
    проект.run(debug="Правда")
