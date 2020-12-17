import flask
from flask import jsonify

from ImageReader import ImageReadingService

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    # todo: get image from FE and pass along
    df = ImageReadingService.fetch_readings_from_image(4)
    return jsonify(df)


app.run()
