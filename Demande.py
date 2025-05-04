import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# === Example 1: Basic GET Request ===
url = "https://www.example.com"
response = requests.get(url)
# It will show the HTTP status code
print(f"Status code: {response.status_code}")

# === Example 2: Print the content of a GET request ===
response = requests.get("https://www.example.com")
print(response.content)

# === Example 3: POST request with JSON data ===
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"
response = requests.post(url, json=data)
response_data = response.json()
# Shows the data as a dictionary
print(response_data)

# === Example 4: Error handling with status code ===
response = requests.get("https://httpbin.org/status/404")
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

# === Example 5: Handling timeout ===
url = "https://httpbin.org/delay/10"
try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout as err:
    print("Request timed out:", err)

# === Example 6: Authenticated request with Bearer Token ===
auth_token = "XXXXXXXX"
headers = {
    "Authorization": f"Bearer {auth_token}"
}
url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())

# === Example 7: Web scraping with BeautifulSoup ===
url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text if soup.title else "No title"
content = soup.find("p").text if soup.find("p") else "No paragraph"
links = [a["href"] for a in soup.find_all("a", href=True)]

print("Title:", title)
print("First paragraph:", content)
print("Links:", links)

# === Example 8: Sending POST request using urllib ===
data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
req = urllib.request.Request("https://www.example.com", data=data, method="POST")
with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")
print("HTML Response:", html)
