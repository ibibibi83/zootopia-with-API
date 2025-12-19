import requests

API_KEY = "Sqskv86JLRfYitkeDMkZ0A==SYQLhMidYptBiHtV"
API_BASE_URL = "https://api.api-ninjas.com"

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  response = requests.get(API_BASE_URL+"/v1/animals", params={"name":animal_name}, headers={"X-Api-Key":API_KEY})
  return response.json()
