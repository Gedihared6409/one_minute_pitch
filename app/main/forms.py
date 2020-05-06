from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from ..models import User



class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What do you want to pitch about ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('Pickuplinespitch','pickuplinespitch'), ('interviewpitch','interviewpitch'),('bussinessplan','bussinessplan'),('promotionpitch','promotionpitch')],validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')	