import requests

url = "https://raw.githubusercontent.com/MrBluebyte/hello-phython/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("File fetched successfully!")
    print(response.text)
else:
    print("Failed to fetch file.")
