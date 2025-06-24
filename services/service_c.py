from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Resposta do Serviço C"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003)