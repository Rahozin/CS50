import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get data from db
    portfolio_table = db.execute(
        "SELECT shares.symbol AS Symbol, shares.name AS Name, SUM(orders.shares) AS Shares FROM orders INNER JOIN shares ON shares.id=orders.share_id WHERE user_id = :user_id GROUP BY Symbol",
        user_id=session['user_id'])
    actual_cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                             user_id=session['user_id'])[0]['cash']

    # Get actual prices, count totals and add to the table
    total = actual_cash
    for row_num in range(len(portfolio_table)):
        actual_price = lookup(portfolio_table[row_num]['Symbol'])['price']
        portfolio_table[row_num]['Price'] = actual_price
        row_total = portfolio_table[row_num]['Shares'] * \
            lookup(portfolio_table[row_num]['Symbol'])['price']
        portfolio_table[row_num]['TOTAL'] = row_total
        total += row_total

    # Typed manualy else raise an error if no orders
    table_headers = ("Symbol", "Name", "Shares", "Price", "TOTAL")
    # table_headers = list(portfolio_table[0].keys())

    # Display page
    return render_template(
        "portfolio.html", table=portfolio_table, headers=table_headers,
        cash=actual_cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Ensure symbol was entered
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure symbol exists
        if not lookup(symbol):
            return apology("symbol doesn`t exist", 400)

        # Ensure shares is positive integer
        try:
            shares = int(shares)
        except:
            return apology("shares must be whole number", 400)
        if shares < 1:
            return apology("shares must be positive whole number", 400)

        # Check amount of the user`s cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session['user_id'])[0]['cash']

        # Get share data using symbol
        share_data = lookup(symbol)

        # Cash needed to buy the order
        price = float(share_data['price']) * shares

        # Ensure there is enough cash
        if price > cash:
            return apology("not enough cash to buy this order, please top up", 400)

        # Add new share to db if needed
        try:
            db.execute("INSERT INTO shares (name, symbol) VALUES (:name, :symbol)",
                       name=share_data['name'], symbol=share_data['symbol'])
        except:
            pass

        # Get the share's id
        share_id = db.execute("SELECT id FROM shares WHERE symbol = :symbol",
                              symbol=symbol)[0]['id']

        # Update user's cash with the purchase
        db.execute("UPDATE users SET cash = :user_cash WHERE id = :user_id",
                   user_cash=cash-price, user_id=session['user_id'])

        # Add a new line to the history of orders
        db.execute(
            "INSERT INTO orders (user_id, share_id, shares, by_price) VALUES (:user_id, :share_id, :shares, :by_price)",
            user_id=session['user_id'],
            share_id=share_id, shares=shares, by_price=price)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)
        # if len(rows) != 1 or not rows[0]["hash"] == request.form.get("password"):
        #     return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@ app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@ app.route("/quote", methods=["GET", "POST"])
@ login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        # Ensure symbol was entered
        if not symbol:
            return apology("missing symbol", 400)

        quoted = lookup(symbol)
        # lookup doesn`t work because of old API, so ...
        # quoted = {
        #     "name": "International Business Machines Corp.",
        #     "price": "122.51",
        #     "symbol": "IBM"
        # }

        # Ensure symbol was entered
        if not quoted:
            return apology("invalid symbol", 400)

        message = f"A share of {quoted['name']} ({quoted['symbol']}) costs ${quoted['price']}."

        return render_template("quoted.html", message=message)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@ app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        hash = generate_password_hash(request.form.get("password"))

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password confirmation was submitted
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("must provide the same password two times", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # Ensure username is not already registered
        if len(rows) > 0:
            return apology("username is not available", 403)

        # Add new user to db
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                   username=username, hash=hash)

        # Query database with a new user for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@ app.route("/sell", methods=["GET", "POST"])
@ login_required
def sell():
    """Sell shares of stock"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Ensure symbol was entered
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure symbol exists
        if not lookup(symbol):
            return apology("symbol doesn`t exist", 400)

        # Ensure shares is positive integer
        try:
            shares = int(shares)
        except:
            return apology("shares must be whole number", 400)
        if shares < 1:
            return apology("shares must be positive whole number", 400)

        # Get data from db
        share_quantity = db.execute(
        "SELECT SUM(orders.shares) AS shares FROM orders INNER JOIN shares ON shares.id=orders.share_id WHERE user_id = :user_id AND symbol = :symbol",
        user_id=session['user_id'], symbol=symbol)[0]['shares']

        # Ensure shares are sufficient
        if shares > share_quantity:
            return apology("you have not enough shares", 400)
        
        # Check amount of the user`s cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session['user_id'])[0]['cash']

        # Get share data using symbol
        share_data = lookup(symbol)

        # Free up cash by selling the order
        price = float(share_data['price']) * shares

        # Get the share's id
        share_id = db.execute("SELECT id FROM shares WHERE symbol = :symbol",
                              symbol=symbol)[0]['id']

        # Update user's cash due to the sell
        db.execute("UPDATE users SET cash = :user_cash WHERE id = :user_id",
                   user_cash=cash+price, user_id=session['user_id'])

        # Add a new line to the history of orders
        db.execute(
            "INSERT INTO orders (user_id, share_id, shares, by_price) VALUES (:user_id, :share_id, :shares, :by_price)",
            user_id=session['user_id'],
            share_id=share_id, shares=-shares, by_price=price)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        shares_table = db.execute("SELECT shares.symbol AS symbol FROM orders INNER JOIN shares ON shares.id = orders.share_id WHERE user_id = :user_id GROUP BY symbol;",
                          user_id=session['user_id'])

        return render_template("sell.html", shares=shares_table)



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


# Activate debug mode if runs directly debugger
if __name__ == '__main__':
    app.run(debug=True)
