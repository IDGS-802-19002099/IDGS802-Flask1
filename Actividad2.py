from flask import Flask, render_template
from flask import request 

app=Flask(__name__)

@app.route("/operasBas", methods=["GET"])
def operasBas():
    return render_template("operasBas.html")



@app.route("/resultado", methods=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    i=0
    res1=0
    while i < int(n2):
            res1=int(n1)+res1
            i += 1
    res=res1
    return render_template("resultado.html", res=res)

if __name__ =="__main__":
    app.run(debug=True, port=3000)