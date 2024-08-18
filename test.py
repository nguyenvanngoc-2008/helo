import os
try:
	import requests
except:
	os.system("pip install requests")
link="https://run.mocky.io/v3/22bc8970-76a1-4d68-9cae-ea7a180a3c47"
def ghi():
	global link
	nd=eval(requests.get(link).text)
	nd.append("helo")
	json_data = {
	    'content': str(nd),
	    'content_type': 'application/json',
	    'charset': 'UTF-8',
	    'status': 200,
	    'secret': 'Ngocdaica',
	    'expiration': 'never',
	    'headers': {
	        'X-FOO': 'bar',
	        'X-BAR': 'foo',
	    },
	}
	
	response = requests.put(f'http://api.mocky.io/api/mock/{id}', json=json_data)
	if response.status_code==204:
	    return True
	else:
		return False
print(ghi())