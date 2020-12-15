from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
from decimal import Decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask countries currencies."""

    return render_template("form.html")
    """ Append question.html to browser. """


@app.route("/conversion")
def show_amount():
    """Show conversion result."""

    from_conv = request.args["convert_from"]
    to = request.args["convert_to"]
    amount = Decimal(request.args["amount"])
    """ Request arguments """

    c = CurrencyRates()
    text = c.convert(from_conv, to, amount)
    """ Convert currency """

    return render_template("conversion.html", text=text)
    """ Append conversion.html to browser. """
