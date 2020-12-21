from flask import Flask, render_template, request, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from decimal import Decimal, DecimalException

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

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
    try:
        amount = Decimal(request.args["amount"])
    except DecimalException:
        session['error'] = "Amount Is Not Valid"
        return redirect("/error")

    """ Request arguments """

    c = CurrencyRates()
    try:
        text = c.convert(from_conv, to, amount)
    except RatesNotAvailableError:
        session['error'] = "Invalid Currency Code"
        return redirect("/error")
    """ Convert currency """

    return render_template("conversion.html", text=text)
    """ Append conversion.html to browser. """


@app.route('/error')
def get_error():
    """ Display the home page with error message """

    msg = session['error']
    return render_template('error.html', msg=msg)
