from flask import Flask, render_template, request
# import RPi.GPIO as GPIO

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET', 'POST'])
def index():
    # GPIO.setup(2, GPIO.OUT)
    # GPIO.setup(3, GPIO.OUT)
    # GPIO.setup(4, GPIO.OUT)
    # GPIO.setup(5, GPIO.OUT)
    # GPIO.setup(6, GPIO.OUT)
    # GPIO.setup(13, GPIO.OUT)
    # GPIO.setup(17, GPIO.OUT)
    # GPIO.setup(19, GPIO.OUT)
    # GPIO.setup(22, GPIO.OUT)
    # GPIO.setup(26, GPIO.OUT)
    # GPIO.setup(27, GPIO.OUT)

    print(request.method)
    if request.method == 'POST':
        if request.form.get('Varanda1ON') == 'Varanda1ON':
            #GPIO.output(2, GPIO.HIGH)
            print("Varanda1")
        elif request.form.get('Varanda2ON') == 'Varanda2ON':
            # GPIO.output(3, GPIO.HIGH)
            print("Varanda2")
        elif request.form.get('Varanda3ON') == 'Varanda3ON':
            # GPIO.output(4, GPIO.HIGH)
            print("Varanda3")
        elif request.form.get('AndarSuperiorON') == 'AndarSuperiorON':
            # GPIO.output(5, GPIO.HIGH)
            print("AndarSuperior")
        elif request.form.get('CozinhaVON') == 'CozinhaVON':
            # GPIO.output(6, GPIO.HIGH)
            print("CozinhaV")
        elif request.form.get('CozinhaION') == 'CozinhaION':
            # GPIO.output(13, GPIO.HIGH)
            print("CozinhaI")
        elif request.form.get('QuartoPPON') == 'QuartoPPON':
            # GPIO.output(17, GPIO.HIGH)
            print("QuartoPP")
        elif request.form.get('QuartoFJON') == 'QuartoFJON':
            # GPIO.output(19, GPIO.HIGH)
            print("QuartoFJ")
        elif request.form.get('Sala1ON') == 'Sala1ON':
            # GPIO.output(22, GPIO.HIGH)
            print("Sala1")
        elif request.form.get('Sala2ON') == 'Sala2ON':
            # GPIO.output(26, GPIO.HIGH)
            print("Sala2")
        elif request.form.get('Sala3ON') == 'Sala3ON':
            # GPIO.output(27, GPIO.HIGH)
            print("Sala3")
        if request.form.get('Varanda1OFF') == 'Varanda1OFF':
            #GPIO.output(2, GPIO.LOW)
            print("Varanda1")
        elif request.form.get('Varanda2OFF') == 'Varanda2OFF':
            # GPIO.output(3, GPIO.LOW)
            print("Varanda2")
        elif request.form.get('Varanda3OFF') == 'Varanda3OFF':
            # GPIO.output(4, GPIO.LOW)
            print("Varanda3")
        elif request.form.get('AndarSuperiorOFF') == 'AndarSuperiorOFF':
            # GPIO.output(5, GPIO.LOW)
            print("AndarSuperior")
        elif request.form.get('CozinhaVOFF') == 'CozinhaVOFF':
            # GPIO.output(6, GPIO.LOW)
            print("CozinhaV")
        elif request.form.get('CozinhaIOFF') == 'CozinhaIOFF':
            # GPIO.output(13, GPIO.LOW)
            print("CozinhaI")
        elif request.form.get('QuartoPPOFF') == 'QuartoPPOFF':
            # GPIO.output(17, GPIO.LOW)
            print("QuartoPP")
        elif request.form.get('QuartoFJOFF') == 'QuartoFJOFF':
            # GPIO.output(19, GPIO.LOW)
            print("QuartoFJ")
        elif request.form.get('Sala1OFF') == 'Sala1OFF':
            # GPIO.output(22, GPIO.LOW)
            print("Sala1")
        elif request.form.get('Sala2OFF') == 'Sala2OFF':
            # GPIO.output(26, GPIO.LOW)
            print("Sala2")
        elif request.form.get('Sala3OFF') == 'Sala3OFF':
            # GPIO.output(27, GPIO.LOW)
            print("Sala3")
        else:
            # pass # unknown
            return render_template("index.html")
    # elif request.method == 'GET':
    #     # return render_template("index.html")
    #     print("No Post Back Call")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
