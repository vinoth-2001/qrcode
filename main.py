from flask import Flask, render_template, request, flash
import qrcode


app = Flask(__name__)

app.secret_key = "jd9wy9r82hedj"

@app.route('/')
def Qrpage():
    return render_template('index.html')

@app.route('/generater', methods=['POST'])
def generater():
    name = request.form['Qrtext']
    if not name:
        flash('Please enter a URL.')
        return redirect(url_for('index'))
    qr = qrcode.make(name)
    qr.save('static/qr.png')
    return render_template('qr.html')

if __name__ == '__main__':
    app.run(debug=True)
