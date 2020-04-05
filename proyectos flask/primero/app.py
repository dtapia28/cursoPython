from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello(nombre ="default"):
    nombre = request.args.get("nombre", nombre)
    return "Hola "+str(nombre)


@app.route("/videos")
def videos():
    return "Aquí irán los videos"



if __name__ == "__main__":
    app.run(debug=True)