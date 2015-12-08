from wtforms import Form, IntegerField, validators

class InputForm(Form):
    dims = IntegerField(
        label='Number of dimensions', default=4,
        validators=[validators.InputRequired()])
    dim_size = IntegerField(
        label='Dimension size', default=3,
        validators=[validators.InputRequired()])
    n_cards = IntegerField(
        label='Number of sample cards from the deck', default=12,
        validators=[validators.InputRequired()])