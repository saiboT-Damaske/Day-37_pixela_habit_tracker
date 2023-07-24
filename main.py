import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "12345678"
USERNAME = ""
GRAPH_ID = "graph01"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# # create username
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "mb_graph",
    "unit": "occurrences",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# # creating the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = datetime.datetime.now()
today = datetime.datetime(year=2023, month=7, day=22)
print(today.strftime("%Y%m%d"))
request_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}
# # creating a pixel
# response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", headers=headers, json=request_body)
# print(response.text)

day_to_update = datetime.datetime(year=2023, month=7, day=23).strftime("%Y%m%d")

update_body = {
    "quantity": "4"
}
# updating a pixel
# response = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/{day_to_update}", headers=headers, json=update_body)
# print(response.text)


# deleting a pixel
response = requests.delete(url=f"{graph_endpoint}/{GRAPH_ID}/{day_to_update}", headers=headers)
print(response.text)