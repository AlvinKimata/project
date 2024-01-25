from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name="Kimata")

@app.route('/your_url', methods=['GET', 'POST'])
def your_url():
    # url = request.args.get('url')
    code = request.form['code']
    return render_template('your_url.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)
