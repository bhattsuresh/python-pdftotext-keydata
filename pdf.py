import pdftotext

def sb_get_text(secure,password=None):
	output = ''
	with open(secure, "rb") as f:
		if(password):
			pdf = pdftotext.PDF(f, password)
		else:
			pdf = pdftotext.PDF(f)	

		for page in pdf:
			output += page

	return output


def sb_get_value(text,keys,match = " "):

	s = " ".join(text.split())
	  
	for key in keys:
		res = s.partition(key)[2]
		r = res.split(match)
		if len(r)>1:
				keys[key]=r[1]
			
	return keys 
	

	
	
		
sb=5

	