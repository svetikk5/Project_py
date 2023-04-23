from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from sqlalchemy import orm
from wtforms import StringField, TextAreaField, FileField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    foto = FileField("Изображение", validators=[FileAllowed(['jpg','jpeg','png'])])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')

    categories = orm.relationship("Category",
                                  secondary="association",
                                  backref="news")