from flask import request, redirect, url_for, render_template, g
from . import admin
from .form import Url_Form
import hashlib
import zlib
from hashids import Hashids
from . import db
import datetime

@admin.route('/',methods=["GET", "POST"])
def index():
	form = Url_Form()
	if request.method == "GET":
		return render_template('index.html', form=form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template('index.html', form=form)
			#return render_template('index.html', form=form)
		url = request.form['url']
		url_sha = hashlib.sha1(url).hexdigest()		
		url_crc = zlib.crc32(url) & 0xffffffff
		hashids = Hashids(min_length=6)
		url_hashids = hashids.encode(url_crc)
		url_key = "url:" + url_sha + "-" + str(url_crc)
		url_value = {"hashid":url_hashids,"url":url,"create_time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"count":1}
		db.hmset(url_key,url_value)	
		return "url is %s,sha1 is %s, crc is %s,hashids is %s" % (url,url_sha,url_crc,url_hashids)
