from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "hello gittest2-was (v1)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

