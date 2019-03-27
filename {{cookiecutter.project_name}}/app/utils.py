from flask import render_template


def not_exist(error):
    return render_template("errors/404.html")
