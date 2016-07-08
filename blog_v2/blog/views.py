from flask import render_template

from . import app
from .database import session, Entry

PAGINATE_BY = 10

@app.route("/")
@app.route("/page/<int:page>")
def entries(page=1):
    # Zero-indexed page
    page_index = page - 1

    count = session.query(Entry).count()

    start = page_index * PAGINATE_BY
    end = start + PAGINATE_BY

    total_pages = (count - 1) // PAGINATE_BY + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0

    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries[start:end]

    return render_template("entries.html",
        entries=entries,
        has_next=has_next,
        has_prev=has_prev,
        page=page,
        total_pages=total_pages
    )

@app.route("/entry/add", methods=["GET"])
def add_entry_get():
    return render_template("add_entry.html")

from flask import request, redirect, url_for

#@app.route("/entry/add", methods=["POST"])
@app.route("/entry/add", methods=["GET","POST"])
def add_entry_post():
    entry = Entry(
        title=request.form["title"],
        content=request.form["content"],
    )
    session.add(entry)
    session.commit()
    return redirect(url_for("entries"))

@app.route("/entry/<id>" , methods=["GET"])
def show_entry(id):
    entries=session.query(Entry)
    entry=entries.get(id)
    return render_template('entries.html', entries=[entry])

@app.route("/entry/<id>")
def post(id=id):
    post = session.query(Entry).filter(Entry.id == postid).first()
    return render_template(
        "single_post.html",
        post=post,
        id=id,
    )

@app.route("/entry/<entryid>/edit", methods=["GET"])
def edit_post_get(entryid=Entry.id):
    entry = session.query(Entry).filter_by(id=entryid).first()
    return render_template("edit_post.html",entry=entry)


@app.route("/entry/<entryid>/edit", methods=["POST"])
def edit_post(entryid):

    title = request.form["title"]
    content = mistune.markdown(request.form["content"])

    session.query(Entry).filter_by(id=entryid).update(
        {"title": title, "content": content}
    )

    session.commit()
    return redirect(url_for("entries"))


@app.route("/entry/<entryid>/delete", methods=["GET"])
def delete_post(entryid):
    session.query(Entry).filter_by(id=entryid).delete()
    session.commit()
    return redirect(url_for("entries"))


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")
