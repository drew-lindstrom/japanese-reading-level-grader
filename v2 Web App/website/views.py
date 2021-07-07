from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Url
from . import db
import json
from .textScraper import getUrlData

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        if request.form.get("knownKanji"):
            knownKanji = ""
            knownKanji += request.form.get("knownKanji")

        if request.form.get("url"):
            url = request.form.get("url")

            if len(url) < 1:
                flash("Note is too short!", category="error")
            else:
                newUrl = getUrlData(url, knownKanji)
                db.session.add(newUrl)
                db.session.commit()
                flash("URL added!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/delete-note", methods=["POST"])
def delete_note():
    url = json.loads(request.data)
    urlId = url["urlId"]
    url = Url.query.get(urlId)
    if url:
        if url.user_id == current_user.id:
            db.session.delete(url)
            db.session.commit()

    return jsonify({})