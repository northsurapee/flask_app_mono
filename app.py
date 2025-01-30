from flask import Flask, render_template, request

from logic import get_diff

app = Flask(__name__, template_folder="templates")


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def fill_json():
    return render_template("fill_json.html")


@app.route('/compare', methods=['POST'])
def compare():
    # Retrieve expected and actual json string from request
    expected_json_str = request.form['expectedJson']
    actual_json_str = request.form['actualJson']

    # Call compare function
    result = get_diff(expected_json_str, actual_json_str)

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run()
