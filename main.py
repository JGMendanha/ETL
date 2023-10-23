import pandas as pd
import requests
import json
import openai

def update_user(user):
    sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}, json=user")
    return True if response.status_code == 200 else False

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
     "content": "You are a banking marketing specialist."
    }
  ]
)
  return completion.choices[0].message.content.strip('\"')

def get_poke_name(id):
  pokemon_api_url = "https://pokeapi.co/api/v2"
  response = requests.get(f'{pokemon_api_url}/pokemon/{id}')
  return response.json() if response.status_code == 200 else None


df = pd.read_csv('POKE.csv')
poke_ids = df["PokeName"].tolist()

pokes = [poke for id in poke_ids if (poke := get_poke_name(id)) is not None]
print(json.dumps (pokes, indent=2))

OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

for user in pokes:
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "O Santander tem solu\u00e7\u00f5es de cr\u00e9dito sob medida pra voc\u00ea. Confira!"
  })

for user in pokes:
  success = update_user(user)
  print(f"User {user['name']} update? {success}!")



