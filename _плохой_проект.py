from flask import Flask

проект = Flask(__name__)


@проект.route("/", methods=["POST", "GET"])
def поехали():
    return "Привет"


if __name__ == "__main__":
    проект.run(debug="Правда")
