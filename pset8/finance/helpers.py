import yfinance as yf

import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    # try:
    #     response = requests.get(
    #         f"https://api.iextrading.com/1.0/stock/{urllib.parse.quote_plus(symbol)}/quote")
    #     response.raise_for_status()
    # except requests.RequestException:
    #     return None

    # API doesn`t work and I don't know how to fix it yet? so
    if urllib.parse.quote_plus(symbol).upper() == "USD":
        return {
            "name": "ProShares Trust - ProShares Ultra Semiconductors 2X Shares",
            "price": "13.30",
            "symbol": "USD"
        }
    elif urllib.parse.quote_plus(symbol).upper() == "IBM":
        return {
            "name": "International Business Machines Corp.",
            "price": "122.51",
            "symbol": "IBM"
        }
    elif urllib.parse.quote_plus(symbol).upper() == "APP":
        return {
            "name": "Applovin Corp - Class A",
            "price": "17.44",
            "symbol": "APP"
        }
    else:
        return None

    # # Parse response
    # try:
    #     quote = response.json()
    #     return {
    #         "name": quote["companyName"],
    #         "price": float(quote["latestPrice"]),
    #         "symbol": quote["symbol"]
    #     }
    # except (KeyError, TypeError, ValueError):
    #     return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
