import requests

# Use an outdated version of the requests library.
response = requests.get("https://example.com")

# Print the response status code.
print(response.status_code)
