from flask import Flask, render_template
import os
import random

app = Flask(__name__)
# list of dog images
images = [
    "giphy.gif",
    "giphy01.gif",
    "R9V7tnR.gif",
    "R9V8tnz.gif",
    "S9V7tna.gif",
    "ride.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
