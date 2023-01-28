from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!!!!"
#   < >
@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    if request.method =="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        if request.form.get("rbd") =="suma":
            return "<h2> La suma es: {}</h2>".format(str(int(num1)+int(num2)))
        elif request.form.get("rbd") =="resta":
            return "<h2> La resta es: {}</h2>".format(str(int(num1)-int(num2)))
        elif request.form.get("rbd") =="multiplicacion":  
            return "<h2> La multiplicacion es: {}</h2>".format(str(int(num1)*int(num2)))
        elif request.form.get("rbd") =="division":  
            return "<h2> La division es: {}</h2>".format(str(int(num1)/int(num2)))
        #return "<h2> La suma es: {}".format(str(int(num1)+int(num2)))
    else:
        return """
        <form action="/operasBas" method="POST">
        <label> N1: </label>
        <input type="text" name="num1" />
        <br><br>
        <label> N2: </label>
        <input type="text" name="num2"/> 
        <br><br>
        <label> Operacion: </label>
        <br>
        <fieldset> 
        
        <input type="radio" name="rbd" id="rbd" value="suma"/>
        <label for="rbd">Suma</label>
        <br> 
        <input type="radio" name="rbd" id="rbd" value="resta"/>
        <label for="rbd">Resta</label>
        <br> 
        <input type="radio" name="rbd" id="rbd" value="multiplicacion"/>
        <label for="rbd">Multiplicacion</label>
        <br>  
        <input type="radio" name="rbd" id="rbd" value="division"/>
        <label for="rbd">Division</label><br> 
       
        </fieldset>
        <input type="submit" value="calcular" />
        <form/>
        """





if __name__ =="__main__":
    app.run(debug=True, port=3000)