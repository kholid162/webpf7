from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def dataa():
    return render_template('PAGE.html')
@app.route('/page2', methods=['GET', 'POST'])
def datab():
    return render_template('PAGE2.html')
@app.route('/page3', methods=['GET', 'POST'])
def datac():
    return render_template('PAGE3.html')
@app.route('/page4', methods=['GET', 'POST'])
def dataf():
    return render_template('PAGE4.html')


if __name__ == '__main__':
    app.run(debug=True)
