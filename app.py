from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

from config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE
)

app = Flask(__name__)
app.secret_key = "todo-list-secret-key"


def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


@app.route("/")
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, title, status, created_at
        FROM tasks
        ORDER BY created_at DESC
    """)

    todos = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", todos=todos)


@app.route("/todos/create", methods=["POST"])
def create_todo():
    title = request.form.get("title", "").strip()

    if not title:
        flash("Todo tidak boleh kosong.", "danger")
        return redirect(url_for("index"))

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title)
        VALUES (%s)
        """,
        (title,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    flash("Todo berhasil ditambahkan.", "success")

    return redirect(url_for("index"))


@app.route("/todos/<int:todo_id>/toggle", methods=["POST"])
def toggle_todo(todo_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET status =
            CASE
                WHEN status = 'pending'
                THEN 'completed'
                ELSE 'pending'
            END
        WHERE id = %s
        """,
        (todo_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("index"))


@app.route("/todos/<int:todo_id>/edit", methods=["GET", "POST"])
def edit_todo(todo_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":

        title = request.form.get("title", "").strip()

        if not title:
            flash("Todo tidak boleh kosong.", "danger")
            return redirect(url_for("edit_todo", todo_id=todo_id))

        cursor.execute(
            """
            UPDATE tasks
            SET title = %s
            WHERE id = %s
            """,
            (title, todo_id)
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Todo berhasil diperbarui.", "success")

        return redirect(url_for("index"))

    cursor.execute(
        """
        SELECT id, title, status
        FROM tasks
        WHERE id = %s
        """,
        (todo_id,)
    )

    todo = cursor.fetchone()

    cursor.close()
    connection.close()

    if not todo:
        flash("Todo tidak ditemukan.", "danger")
        return redirect(url_for("index"))

    return render_template("edit.html", todo=todo)


@app.route("/todos/<int:todo_id>/delete", methods=["POST"])
def delete_todo(todo_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id = %s
        """,
        (todo_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    flash("Todo berhasil dihapus.", "success")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)