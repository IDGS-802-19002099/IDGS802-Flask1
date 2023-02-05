from flask import Flask, render_template
from flask import request
from CinepolisFlaskMetodos import CinepolisFlaskMetodos 

app=Flask(__name__)

@app.route("/CinepolisFlask", methods=["GET"])
def CinepolisFlask():
    return render_template("CinepolisFlask.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    obj=CinepolisFlaskMetodos()
    obj.numeroBoletos=int(request.form.get("txtCantBoletos"))
    obj.numeroCompradores=int(request.form.get("txtCantComp"))
    obj.tarjeta=request.form.get("rbtnTarjetaC")
    obj.calculo()
    
    return render_template("CinepolisFlaskResultado.html", res=obj.resultado)

if __name__ =="__main__":
    app.run(debug=True, port=3000)