# coding=utf-8
from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, PasswordField, SelectField, HiddenField, IntegerField
from wtforms.validators import DataRequired, ValidationError, URL
import re

class Url_Form(Form):
	url = StringField(u"url", [DataRequired(u"请填写url")])
	submit = SubmitField(u"缩短")


	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
		reg = "^(http|https)+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$"
		if not re.match(reg,self.url.data):
		#if 'http' not in self.url.data:
			self.url.errors.append(u"not a http url")
			return False


		
