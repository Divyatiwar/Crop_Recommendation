from flask import Flask, render_template
import serial
import time
import threading

app = Flask(__name__)


try:
    arduino = serial.Serial('COM6', 9600, timeout=1)
    time.sleep(2)  
    print("Arduino connected successfully!")
except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None  

temperature = "N/A"
humidity = "N/A"

def read_from_arduino():
    global temperature, humidity
    while True:
        if arduino:
            try:
                data = arduino.readline().decode('utf-8').strip()
                if data:
                    values = data.split(",")
                    if len(values) == 2:
                        temperature = values[0]
                        humidity = values[1]
                        print(f"Temperature: {temperature} °C, Humidity: {humidity} %")  
            except Exception as e:
                print(f"Error reading from Arduino: {e}")

if arduino:
    thread = threading.Thread(target=read_from_arduino, daemon=True)
    thread.start()

@app.route("/")
def index():
    return render_template("h1.html", temperature=temperature, humidity=humidity)

if __name__ == "__main__":
    app.run(debug=True)
