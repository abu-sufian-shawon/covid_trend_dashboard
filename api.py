import requests

def fetch_covid_data(country, days=90):
    url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays={days}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
