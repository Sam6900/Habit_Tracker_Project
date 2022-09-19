import requests
from pswds import TOKEN, USERNAME
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
print(graph_endpoint)
graph_config = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "min",
    "type": "int",
    "color": "momiji",
    "timezone": "Asia/Calcutta",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)