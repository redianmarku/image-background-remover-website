from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_data = None
    if request.method == "POST":
        file = request.files["image"]
        img = Image.open(file.stream)
        result = remove(img)

        img_io = BytesIO()
        result.save(img_io, "PNG")
        img_io.seek(0)

        image_data = base64.b64encode(img_io.getvalue()).decode('utf-8')
    return render_template("index.html", image_data = image_data)
