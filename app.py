"""
trial Flask application
"""
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """
    Root index handler
    """
    return ({ "result": "Hello World!", "now": datetime.now().isoformat('T') })

if __name__ == "__main__":
    app.run(debug=True)
