import requests
import json
response_API = requests.get('https://hiring.bajajfinservhealth.in/api/renderMe')
#print(response_API.status_code)
data = response_API.text
parse_json = json.dumps(data)
active_case = parse_json
print("login:", active_case)
