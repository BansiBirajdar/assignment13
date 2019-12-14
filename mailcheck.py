
import re 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):
	if(re.search(regex,email)): 
		return True
		
	else: 
		return False