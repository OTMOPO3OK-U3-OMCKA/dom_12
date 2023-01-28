from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import JsonF
from json import JSONDecodeError
from logger import my_logg


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"


bp = Blueprint('bp', __name__)

@bp.route("/")
def page_index():
    return render_template('index.html')


@bp.route("/post_form")
def page_post_form():
    return render_template('post_form.html')


@bp.route("/search", methods=['GET'])
def page_post_search():
    reg = request.args.get('s')
    try:
        jsonf = JsonF(POST_PATH)
    except FileNotFoundError:
        my_logg.warning("no file-json")
        return "зайдите на сайт в другой раз"
    except JSONDecodeError:
        my_logg.warning("the content of the file does not match")
        return 'содержание файла не соответствует морально-нравственным устоям компьютрной религии'
    listik = jsonf.filter_reverse(reg)
    return render_template('post_list.html', reg=reg, listik=listik)


@bp.route("/uploads", methods=['POST'])
def static_dir():
    try:
        formats = ["png", "jpg", "jpeg"]
        picture = request.files.get('picture')
        filename = picture.filename
        picture_type = filename.split(".")[-1]
        element = {"pic": picture.filename,
                   "content": request.form.get('content')}
        my_logg.info('ddd')
        if picture_type in formats:
            if bool(element["content"]):
                try:
                    picture.save(f'./static/images/{filename}')
                    jsonf = JsonF(POST_PATH)
                    jsonf.add_element(element)
                    f = jsonf.load_data()
                    f.reverse()
                except FileNotFoundError:
                    my_logg.warning("not json-file")
                    return "нет доступа к базе, зайдите в другой раз"
                except JSONDecodeError:
                    my_logg.warning("the content of the file does not match")
                    return 'нет доступа к базе, зайдите в другой раз'
                else:
                    return render_template("post_uploaded.html", f=f)
            return "не введен текст"
        else:
            return "нет картинки"
    except:
        return "вообще не знаю чё произошло"
    finally:
        my_logg.warning("there was an attempt to publish a post")

'''
@bp.route("/uploads/<path:path>")
def static_dir2(path):
    return send_from_directory("static/images", path)
'''
