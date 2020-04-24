import tornado.web

import tornado.ioloop

import pdf

class UploadHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

	def post(self):
		files = self.request.files['imgFile']
		x = self.get_body_argument('keys')
		s = "".join(x.split())
		input_keys_list = s.split(',')
		input_keys = {}
		for key in input_keys_list:
			input_keys[key]='N/A'

		type_text = self.get_body_argument('type')

		for f in files:
			fh = open(f"input/{f.filename}","wb")
			fh.write(f.body)
			fh.close()

			if(type_text == 'text'):	
				text = pdf.sb_get_text(f"input/{f.filename}")
			else:
				text = pdf.sb_get_text(f"input/{f.filename}")
				keys = pdf.sb_get_value(text,input_keys)

		if(type_text == 'text'):	
			self.write(f"{text}")
		else:
			html = '<h3>Key Data</h3><table class="table">'
			for k in keys:
				html += f'<tr><th>{k}: </th><td>{keys[k]}</td></tr>'
			html +='</table>'	 
			self.write(html)	



if(__name__ == "__main__"):
	app = tornado.web.Application([
		("/",UploadHandler),
		("/input/(.*)",tornado.web.StaticFileHandler,{"path":"input"})
		])
	app.listen(8080)
	print("Listening port 8080")

	tornado.ioloop.IOLoop.instance().start()

