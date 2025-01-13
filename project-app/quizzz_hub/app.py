import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import  login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///quiz.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show your quiz"""
    username = session["username"]
    user_id = session["user_id"]

    # Fetch quizzes to display
    tables = db.execute("SELECT id, name FROM quizzes WHERE user_id = ?", user_id)
    counter = len(tables)

    if request.method == "POST":
        # Loop through each quiz to check if its delete button was clicked
        for table in tables:
            quizzes_id = table["id"]

            if request.form.get(f"delete{quizzes_id}") == "clicked":
                # Delete choices associated with questions of the quiz
                question_ids = db.execute("SELECT id FROM questions WHERE quiz_id = ?", quizzes_id)
                for question in question_ids:
                    db.execute("DELETE FROM choices WHERE question_id = ?", question["id"])

                # Delete questions associated with the quiz
                db.execute("DELETE FROM questions WHERE quiz_id = ?", quizzes_id)

                # Finally, delete the quiz
                db.execute("DELETE FROM quizzes WHERE id = ?", quizzes_id)

                # Redirect to avoid resubmission issues
                return redirect("/")

            if request.form.get(f"copy_link{quizzes_id}") == "clicked":
                #pass quizzes_id
                return redirect(url_for("quiz", quizzes_id=quizzes_id))

    return render_template("index.html", username=username, quiz_list=counter, tables=tables)


@app.route("/results", methods=["GET", "POST"])
def results():
    print("woking<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    return render_template ("/results")



@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        return redirect("/contact")

    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            #return render_template("apology.html", reason="Must provide username", code=403) #  updated error replay
            flash("Must provide username", "danger")
            return render_template("login.html")


        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password", "danger")
            return render_template("login.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password", "danger")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/create_quiz", methods=["GET", "POST"])
@login_required
def create_quiz():
    if request.method == "POST":
        # Get form data
        quiz_name = request.form.get("quizName", "").strip()
        quiz_description = request.form.get("quizDescription", "").strip()
        counter = int(request.form.get("counter", 0))
        user_id = session["user_id"]

        # Collect questions and choices
        questions = []
        for i in range(counter):
            # Get i question
            question_text = request.form.get(f"question{i}", "").strip()
            # Get awnsers
            choices = []  # Initialize an empty list to store choices
            for j in range(4):
                choices.append(request.form.get(f"choice{i}_{j}", "").strip())

            # Get correct awnsers
            correct_choice = request.form.get(f"correctChoice{i}", "")
            # Append to questions
            questions.append({"text": question_text, "choices": choices, "correct": correct_choice})


        # Get what action was submited
        action = request.form.get("action")

        # Add to countrer
        if action == "add":
            counter = int(counter) + 1
        # Remove from counter
        if action == "remove":
            counter = int(counter) - 1
            if int(counter) <= 0: # make sure counter cant go bellow 0
                counter = 0


        # Save to database
        if action == "submit":
            quiz_id = db.execute("INSERT INTO quizzes (name, description, user_id) VALUES (?, ?, ?)", quiz_name, quiz_description, user_id)

            for question in questions:
                question_id = db.execute("INSERT INTO questions (quiz_id, question_text) VALUES (?, ?)", quiz_id, question["text"])

                for idx, choice in enumerate(question["choices"]):
                    is_correct = 1 if str(idx) == question["correct"] else 0
                    db.execute("INSERT INTO choices (question_id, choice_text, is_correct) VALUES (?, ?, ?)", question_id, choice, is_correct)

            return redirect("/")


        return render_template("create_quiz.html", quiz_name=quiz_name, quiz_description=quiz_description, counter=counter, questions=questions)


    return render_template("create_quiz.html", quiz_name="", quiz_description="", counter=1, questions=[])


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":

        action = request.form.get("action")
        quiz_take_name = request.form.get("quizTakeName")
        #question_text = request.form.get("question")

        quizzes_id = request.form.get("quizzes_id")
        question_ids = db.execute("SELECT id FROM questions WHERE quiz_id = ?", quizzes_id)

        print(question_ids,": question_ids <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        correct_awnser = []
        for question_id in question_ids:
            # Find correct_choices_id
            correct_choices_id = db.execute("SELECT id FROM choices WHERE question_id = ? AND is_correct = 1", question_id["id"]) # [{'id': 15}, {'id': 16}, {'id': 17}]
            correct_awnser.append(correct_choices_id[0]["id"])


        if action == "submit":

            selected_awnser = []
            for question_id in question_ids:
                # Find selected_choices_id
                selected_choices_id = request.form.get(f"question_{question_id["id"]}")
                selected_awnser.append(int(selected_choices_id))

            total_answers = 0
            total_correct_answers = 0
            for x, y in zip(correct_awnser, selected_awnser):
                total_answers = total_answers + 1
                if x == y:
                    total_correct_answers = total_correct_answers + 1
            result = f"{total_correct_answers}/{total_answers}"
            print(result)
            return redirect(url_for("result", quiz_take_name=quiz_take_name, result=result))

        return redirect("/")

    # THIS PAGE CAN ONLY BE ACCSESS BY PRESSING COPY LINK BUTTON
    # "quizzes_id" is a argument that's be passed by COPY LINK BUTTON.
    quizzes_id = request.args.get("quizzes_id")

    quizzes_id_info = db.execute("SELECT * FROM quizzes WHERE id = ?", quizzes_id)
    question_info = db.execute("SELECT * FROM questions WHERE quiz_id = ?", quizzes_id)
    choices_info = db.execute("SELECT * FROM choices")


    return render_template("/quiz.html", quizzes_id=quizzes_id, quizzes_id_info=quizzes_id_info, question_info=question_info, choices_info=choices_info)


@app.route("/result")
def result():
    """Log user out"""
    quiz_take_name = request.args.get("quiz_take_name")
    result = request.args.get("result")


    # Redirect user to login form
    return render_template("result.html", quiz_take_name=quiz_take_name, result=result)



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Check username is typed
        if not request.form.get("username"):
            flash("Must provide username", "danger")
            return render_template("register.html")

        # Check username dose not stars the numbers
        if not request.form.get("username")[0].isalpha():
            flash("Username must start with alphabetical", "danger")
            return render_template("register.html")

        # Check password is typed
        if not request.form.get("password"):
            flash("Must provide password", "danger")
            return render_template("register.html")

        # Check confirm password is typed
        if not request.form.get("confirm_password"):
            flash("Must provide confirm password", "danger")
            return render_template("register.html")

        # Check if conform_password match with password
        if not request.form.get("confirm_password") == request.form.get("password"):
            flash("Password and confirm password dont match", "danger")
            return render_template("register.html")

        # Check the database to see if username exies
        username_dic = db.execute("SELECT username FROM users WHERE username = ?", request.form.get("username"))

        if len(username_dic) > 0:
            flash("Username already exists, please choose another name", "danger")
            return render_template("register.html")

        # Add username and password to database
        db.execute("INSERT INTO users (username, hash) VALUES(?,?)", request.form.get("username"), generate_password_hash(request.form.get("password")))

        return redirect("/login")

    return render_template("register.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    """about shares of stock"""
    if request.method == "POST":
        return render_template("about.html")

    return render_template("about.html")
