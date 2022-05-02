from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")
 

@app.route("/<string:name>")
def session(name):
    return render_template ("session.html", name = name)

@app.route("/hello", methods=["POST"])
def login():
	name = request.form.get("nombre")
	return render_template(
		"session.html",
		name=name,
		)

@app.route ("/register_form")
def regist ():
	return render_template ("form_regist.html")	


@app.route("/active",  methods=["POST"])
def profile():
	name = request.form.get("nombre")
	sname = request.form.get("apellido")
	dire = request.form.get("direccion")
	mail = request.form.get("E-mail")
	numer = request.form.get("numero")
	fecha = request.form.get("fecha")
	return render_template("profile.html", 
	name = name, 
	sname = sname, 
	dire = dire, 
	mail = mail, 
	numer = numer, 
	fecha = fecha
	)


@app.route("/users")
def names():
	# Query a DB for users.
	name_list = ["Jose", "Pedro", "Maria"]
	return render_template("list.html", names=name_list )