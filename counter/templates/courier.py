import requests

url = "https://api.courier.com/send"

payload = {
  "message": {
    "content": {
      "title": "Calory",
      "body": "Hello there"
    },
    "to": {
      "email": "laxya20supercell@gmail.com",
      "phone_number": " "
    }
  }
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "Bearer pk_prod_TQK3K26XEK40GVKJEB02QM9M03MV"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)