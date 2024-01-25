from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name="Kimata")

@app.route('/your_url', methods=['GET', 'POST'])
def your_url():
    code = request.form['code']
    if request.method == 'POST':
        return render_template('your_url.html', code=code)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
