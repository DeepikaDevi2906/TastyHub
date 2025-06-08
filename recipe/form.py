from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError,Optional,URL
from recipe.models import User

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=2, max=25), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6, max=25), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('That username is taken! Please choose a different one.')

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError('That email is already registered. Please log in or use a different email.')

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class RecipeForm(FlaskForm):
    name=StringField(label='Recipe Name:', validators=[Length(min=2, max=25), DataRequired()])
    description=TextAreaField(label='Recipe Description:', validators=[DataRequired()])
    ingredients=TextAreaField(label='Recipe Ingredients:', validators=[DataRequired()])
    instructions=TextAreaField(label='Recipe Instructions:', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[Optional(), URL()])
class EditForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=5, max=300)])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    image_url = StringField('Image URL (Optional)')