from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello()
    """Return greeting."""
    return "Hello, world! Yuvin is here to conquer"


@app.route("/healthz")
def health():
    """Health check endpoint."""
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
