import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# ensures every HTTP response dose noy get cached
# @app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get user id
    userid = session["user_id"]

    # Get user cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = ?", userid)[0]['cash']

    # Query transactions for symbols and shares owned # example [{'symbol': 'GOOGL', 'total_shares': 4}, {'symbol': 'NFLX', 'total_shares': 1}]
    symbols_shares_total = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", userid,)

    # Initialize variables
    table_list = []
    stocks_total = 0

    # For each user symbol
    for symbol_share in symbols_shares_total:
        # Get each symbol
        symbol = symbol_share["symbol"]
        # Get total_shares
        total_shares = symbol_share["total_shares"]

        # Get the current stock info
        stock_data = lookup(symbol)

        current_price = stock_data["price"]
        total_value = total_shares * current_price
        stocks_total = stocks_total +  total_value

        # Append data to table list
        table_list.append({"symbol": symbol,"shares": total_shares,"price": usd(current_price),"total": usd(total_value),})

    # Calculate grand total (cash + total value of stocks)
    grand_total = stocks_total + cash

    return render_template("index.html", table_list=table_list, cash=usd(cash), grand_total=usd(grand_total),)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # look up for stocks name
        lookup_symbol_info = lookup(request.form.get("symbol"))

        # if not lookup_symbol_info send to apology
        if not lookup_symbol_info:
            return apology("symbol not found", 400)

        # Get shares
        # not a positive integer
        try:
            shares = int(request.form.get("shares"))
            if shares <= 0:
                return apology("Shares must be a positive integer.", 400)
        except (TypeError, ValueError):
            return apology("Shares must be a positive integer.", 400)

        # Extract data from the stock dictionary
        latestPrice = lookup_symbol_info["price"]

        # get submit info
        buy_price = shares * latestPrice
        symbol = request.form.get("symbol")

        # Extract data from the stock dictionary
        userid = session["user_id"]
        action = "Buy"

        # Get users table rows info
        rows = db.execute("SELECT * FROM users WHERE id = ?", userid)

        # Get users cash info
        cash = rows[0]["cash"]

        # Check if enought money
        if cash - buy_price >= 0:
            # sum up the left_over after buy
            left_over = cash - buy_price

            # update users cash after Buy
            db.execute("UPDATE users SET cash = ? WHERE id = ?", left_over, userid)

            # Add buy transaction into transactions database
            db.execute("INSERT INTO transactions (user_id, action, symbol, shares, price) VALUES(?, ?, ?, ?, ?)", userid, action, symbol, shares, buy_price)
        else:
            return apology("Not enough money", 400)

        # Flash success
        flash("Successfully bought shares!")

        return redirect("/")

    return render_template("/buy.html")


@app.route("/history")
@login_required
def history():

    userid = session["user_id"]
    rows = db.execute("SELECT * FROM transactions WHERE user_id = ?", userid)

    history_data = 1 if rows else 0

    for row in rows:
        row["price"] = f"${float(row['price']):.2f}"

    return render_template("/history.html", rows=rows, history_data=history_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]  # Store user ID in session
        session["user_name"] = rows[0]["username"]  # Store user ID in session

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))

        # Ensure lookup returned valid data
        if not symbol:
            return apology("symbol not found", 400)

        # Extract data from the stock dictionary
        latestPrice = usd(symbol["price"])
        symbol = symbol["symbol"]

        # Render the template with stock details
        return render_template("/quote.html", output=symbol, latest_price=latestPrice, symbol = symbol)
    else:
        symbol = None
        return render_template("/quote.html", output=None)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", "400")

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", "400")

        # Ensure confirm password was submitted
        if not request.form.get("confirmation"):
            return apology("must provide confirm password", "400")

        # Ensure password matches confirm password
        if not (request.form.get("password") == request.form.get("confirmation")):
            return apology("password and confirm password must match", "400")

        # If user exist in database
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) > 0:
            return apology("username already exist", 400)

        # Pass username and password to database
        db.execute("INSERT INTO users (username, hash) VALUES(?,?)", request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Redirect to the home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Get user ID
    userid = session["user_id"]

    if request.method == "POST":

        # Get the selected symbol and shares from the form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check for symbol exist
        if not symbol:
            return apology("Must select a stock to sell", 400)

        # Check for shares exist
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Shares must be a positive integer", 400)
        except (TypeError, ValueError):
            return apology("Shares must be a positive integer", 400)

        # Check if user owns enough shares
        user_shares = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",userid, symbol)

        # Check if user as enought shares
        if not user_shares or user_shares[0]["total_shares"] < shares:
            return apology("Not enough shares to sell", 400)

        # Get current stock price
        stock_data = lookup(symbol)
        if not stock_data:
            return apology("Stock lookup failed", 400)

        sell_price = stock_data["price"]
        total_sell_value = shares * sell_price

        # add total_sell_value to users cash
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sell_value, userid)

        # add sell transaction # add a -value so its easier
        db.execute("INSERT INTO transactions (user_id, action, symbol, shares, price) VALUES (?, 'Sell', ?, ?, ?)", userid, symbol, -shares, total_sell_value)

        # Flash success
        flash("Successfully sold shares!")

        return redirect("/")

    # creata a group symbol by aading all the symbols
    user_symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",userid,)

    symbols = []
    for row in user_symbols:
        symbols.append(row["symbol"])

    return render_template("sell.html", symbols=symbols)
