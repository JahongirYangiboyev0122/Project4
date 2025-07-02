import requests

url = "https://real-time-finance-data.p.rapidapi.com/company-cash-flow"

querystring = {"symbol":"AAPL:NASDAQ","period":"QUARTERLY","language":"en"}

headers = {
	"x-rapidapi-key": "4723686d83msheb42294b7d13717p1ac803jsn4f0ac9c03620",
	"x-rapidapi-host": "real-time-finance-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())