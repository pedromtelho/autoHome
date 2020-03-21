from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET', 'POST'])
def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    if request.method == 'POST':
        if request.form.get('Varanda1ON') == 'Varanda1ON':
            GPIO.setup(2, GPIO.OUT)
            GPIO.output(2, GPIO.HIGH)        
        elif request.form.get('Varanda2ON') == 'Varanda2ON':
            GPIO.setup(3, GPIO.OUT)
            GPIO.output(3, GPIO.HIGH)
        elif request.form.get('Varanda3ON') == 'Varanda3ON':
            GPIO.setup(4, GPIO.OUT)
            GPIO.output(4, GPIO.HIGH)
        elif request.form.get('AndarSuperiorON') == 'AndarSuperiorON':
            GPIO.setup(5, GPIO.OUT)
            GPIO.output(5, GPIO.HIGH)
        elif request.form.get('CozinhaVON') == 'CozinhaVON':
            GPIO.setup(6, GPIO.OUT)
            GPIO.output(6, GPIO.HIGH)
        elif request.form.get('CozinhaION') == 'CozinhaION':
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, GPIO.HIGH)
        elif request.form.get('QuartoPPON') == 'QuartoPPON':
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.HIGH)
        elif request.form.get('QuartoFJON') == 'QuartoFJON':
            GPIO.setup(19, GPIO.OUT)
            GPIO.output(19, GPIO.HIGH)
        elif request.form.get('Sala1ON') == 'Sala1ON':
            GPIO.setup(22, GPIO.OUT)
            GPIO.output(22, GPIO.HIGH)
        elif request.form.get('Sala2ON') == 'Sala2ON':
            GPIO.setup(26, GPIO.OUT)
            GPIO.output(26, GPIO.HIGH)
        elif request.form.get('Sala3ON') == 'Sala3ON':
            GPIO.setup(27, GPIO.OUT)
            GPIO.output(27, GPIO.HIGH)
        elif request.form.get('Varanda1OFF') == 'Varanda1OFF':
            GPIO.setup(2, GPIO.OUT)
            GPIO.output(2, GPIO.LOW)
        elif request.form.get('Varanda2OFF') == 'Varanda2OFF':
            GPIO.setup(3, GPIO.OUT)
            GPIO.output(3, GPIO.LOW)
        elif request.form.get('Varanda3OFF') == 'Varanda3OFF':
            GPIO.setup(4, GPIO.OUT)
            GPIO.output(4, GPIO.LOW)
        elif request.form.get('AndarSuperiorOFF') == 'AndarSuperiorOFF':
            GPIO.setup(5, GPIO.OUT)
            GPIO.output(5, GPIO.LOW)
        elif request.form.get('CozinhaVOFF') == 'CozinhaVOFF':
            GPIO.setup(6, GPIO.OUT)
            GPIO.output(6, GPIO.LOW)
        elif request.form.get('CozinhaIOFF') == 'CozinhaIOFF':
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, GPIO.LOW)
        elif request.form.get('QuartoPPOFF') == 'QuartoPPOFF':
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.LOW)
        elif request.form.get('QuartoFJOFF') == 'QuartoFJOFF':
            GPIO.setup(19, GPIO.OUT)
            GPIO.output(19, GPIO.LOW)
        elif request.form.get('Sala1OFF') == 'Sala1OFF':
            GPIO.setup(22, GPIO.OUT)
            GPIO.output(22, GPIO.LOW)
        elif request.form.get('Sala2OFF') == 'Sala2OFF':
            GPIO.setup(26, GPIO.OUT)
            GPIO.output(26, GPIO.LOW)
        elif request.form.get('Sala3OFF') == 'Sala3OFF':
            GPIO.setup(27, GPIO.OUT)
            GPIO.output(27, GPIO.LOW)
        else:
            return render_template("index.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
