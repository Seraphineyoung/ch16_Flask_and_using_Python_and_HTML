from flask import Flask, render_template,request

app = Flask('SeraphineSpecialApp')


@app.route('/')
def hello():
    return render_template('hello.html', title='home')


@app.route('/about')
def about():
    return 'About page'


@app.route("/<name>")
def hiya(name):
    return render_template('hiya.html', name=name)

@app.route("/confirmation", methods=['POST'])
def confirmation():
    print(request)
    print(request.form)
    form_data = request.form
    print(form_data)
    print(form_data['email'])
    email = form_data['email']
    result = 'hello'
    return render_template('confirmation.html', title='Form confirmation', **locals())


@app.route("/players/<name>")
def hobbies(name):
    return render_template('hobbies.html', name=name)


app.run(debug=True)
