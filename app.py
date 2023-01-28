from flask import Flask, request, render_template, send_from_directory, Blueprint
from bluer.app2 import bp

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"


app = Flask(__name__)

app.register_blueprint(bp)
if __name__ == '__main__':
   app.run()
