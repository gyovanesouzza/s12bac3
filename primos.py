import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primeiros_100_primos():
    limite = 100
    c = 1
    p = 1
    numero = 3
    primos = "2,"
    while p < limite:
        primo = True
        for x in range(2,numero):
            if numero % x == 0:
               primo = False
               break
        if(primo):
            primos = primos + str(numero) + ","
            p += 1
            if(p%20==0):
                primos+="<br>"
        numero+=1
    return primos
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

