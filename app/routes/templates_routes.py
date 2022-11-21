from services.config import *
from services.utils import *

''' Rota: [ home_route ]
    descrição: Retorna o template da tela inicial da aplicação.
'''
@app.route("/")
def home_route():
    return render_template("pages/home.html")

''' Rota: [ join_route ]
    descrição: Retorna o template da tela de registro.
'''
@app.route("/join")
def join_route():
    return render_template("pages/register.html")

''' Rota: [ login_route ]
    descrição: Retorna o template da tela de login.
'''
@app.route("/login")
def login_route():
    return render_template("pages/login.html")

@app.route("/new/game")
def new_game_route():
    return render_template ("pages/game-form.html")

@app.route("/myprofile")
def profile_route():
    return render_template("pages/my-profile.html")

@app.route("/giftcard")
def giftcard_route():
    return render_template("pages/giftcard.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("utils/_error.html", code=404, message = "PAGE NOT FOUND" )

@app.errorhandler(401)
def page_not_found(error):
    return render_template("utils/_error.html", code=401, message = "UNAUTHORIZED USER")