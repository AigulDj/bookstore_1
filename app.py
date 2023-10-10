import os
from flask import Flask, request, jsonify

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def post_vowels():
    text = request.form['text']
    vowels = 'aouie'
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return f'There are {count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return 'Please provide a name and a message', 400
    else:
        names = request.form['names']
        name_list = names.split(',')
        sorted_names = sorted(name_list)
        return ','.join(sorted_names)


@app.route('/names')
def get_names():
    pre_defined_names = 'Julia, Alice, Karim'
    name = request.args['name']
    return f"{pre_defined_names}, {name}"









# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


