from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, ValidationError

class URLForm(FlaskForm):
    url = StringField(validators=[DataRequired(), ])
    submit=SubmitField(label='Submit')

    def validate_url(self, url):
        if not (self.url.data.startswith("https://www.zaubacorp.com/company/")):
            raise ValidationError(
                f"URL must be from Zaubacorp website search result"
            )
    


class ContactUsForm(FlaskForm):
    pass