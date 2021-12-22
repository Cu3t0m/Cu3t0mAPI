from Cu3t0mAPI import API
import json
import random
import requests

rs = API("Cu3t0mAPI9f7d9933bc30e3564d791e73ebc66986a82ffa9159b7c5e8c481406a53f62adbba3d1808d6a723027536852a940fac28f7c22226d1961b53ec2c845081c26bff")

x=69
print("Simple use of the 'ai_response' function.")
while x == 69:
  q = input("")
  resp = rs.ai_response(q)
  response = json.loads(resp)
  print(response["response"])