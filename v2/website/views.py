from flask import Blueprint, render_template, request, flash, jsonify
import json

views = Blueprint("views", __name__)

notes_list = ["情報番組"]


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            notes_list.append(note)

    return render_template("home.html", notes_list=notes_list)