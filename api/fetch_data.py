# Logic to extract data from the API

import requests
response = requests.get("https://holidays.abstractapi.com/v1/?api_key=4ee75957cd434a1e8d0514606f8ec94c&country=US&year=2025&month=12&day=25")
print(response.status_code)
print(response.content)