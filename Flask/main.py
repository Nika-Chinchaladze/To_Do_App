from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PREPARE DATABASE:
app.config["SECRET_KEY"] = "TommyShelby"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True)

    def get_dictionary(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        if "newId" in request.form:
            task_name = request.form.get("newTask")
            control = db.session.query(Task).filter_by(title=task_name).first()
            if not control:
                new_task = Task(
                    title=task_name
                )
                db.session.add(new_task)
                db.session.commit()
                return redirect(url_for("home_page"))
            else:
                flash("Task Already Exists!")
                return redirect(url_for("home_page"))

        if "updateId" in request.form:
            update_id = request.form.get("taskId")
            task = db.session.query(Task).filter_by(id=update_id).first()
            task.title = request.form.get("updateInput")
            db.session.commit()
            return redirect(url_for("home_page"))

    all_tasks = db.session.query(Task).all()
    return render_template("index.html", all_tasks=all_tasks)


@app.route("/delete/<int:record_id>")
def delete_page(record_id):
    task = db.session.query(Task).filter_by(id=record_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home_page"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
