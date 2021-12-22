import random
import requests


class API():
  def __init__(self, api_key):
    self.api_key = api_key
    


  def jokes(self):
    response = requests.get(f'https://api.cu3t0m.repl.co/api/v1/gimme/jokes')
    return response.text

  def letters(self):
    response = requests.get(f'https://api.cu3t0m.repl.co/api/v1/gimme/letters')
    return response.text

  def numbers(self):
    response = requests.get(f'https://api.cu3t0m.repl.co/api/v1/gimme/numbers')
    return response.text

  def words(self):
    response = requests.get(f'https://api.cu3t0m.repl.co/api/v1/gimme/words')
    return response.text

  def memes(self, topic="memes", amount="1"):
    response = requests.get(f'https://api.cu3t0m.repl.co/api/v1/gimme/memes/{topic}/{amount}?key={self.api_key}')
    return response.text

  def ai_response(self, question, prev_question=None):
    response = requests.get(f'https://api.cu3t0m.repl.co/api/v1/ai/response/{question}?prompt={prev_question}&&key={self.api_key}')
    return response.text