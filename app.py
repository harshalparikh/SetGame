from model import InputForm
from flask import Flask, render_template, request
from game import Sets
import itertools

app = Flask(__name__)

@app.route('/setgame', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.dims.data < 3:
            raise ValueError("Dimensions should be greater than 2 for a three card SET game")
        if form.dim_size.data < 3:
            raise ValueError("Dimension size should be greater than 2 for a three card SET game")
        s = form.dims.data * [range(form.dim_size.data)]
        possible_cards = len(list(itertools.product(*s)))
        if form.n_cards.data > possible_cards:
            raise ValueError("Number of cards on the deck cannot be greater than %s" %possible_cards)
        game_set = Sets(form.dims.data, form.dim_size.data, form.n_cards.data)
        if form.dim_size.data == 3:
            result = game_set.get_sets()
        else:
            result = game_set.getsets_brute()
    else:
        result = None

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)