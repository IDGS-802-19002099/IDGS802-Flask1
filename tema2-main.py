from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!!!! ---nuevo---"


@app.route("/hola")
def holz():
    return "Hola en la nueva ruta"

if __name__ =="__main__":
    app.run(debug=True, port=3000)