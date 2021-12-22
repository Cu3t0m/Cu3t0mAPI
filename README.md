<div>
  <h1 align='center'>
    Cu3t0mAPI
  </h1>
</div>
<div>
  <p align='center'>
    <img src=https://img.shields.io/pypi/dm/Cu3t0mAPI?color=success&label=PyPi%20Downloads&style=flat-square>
    <img src=https://img.shields.io/badge/Stable_Version-0.0.2-informational>
    <img src=https://img.shields.io/badge/Development_Version-0.0.4-informational>
  </p>
  <p align='center'>
    A Python api wrapper.
  </p>
</div>
<br>


# About
---

Cu3t0mApi is an API wrapper for my API that I made for fun in around 20 minutes. As of writing, there are only a few endpoints but I plan to add more. My code is badly and lazily written but hey, it works!

# Memes
---
```py
Cu3t0mAPI.memes(topic, amount)
# Default topic is the subreddit 'memes' and default amount is '1'.
```
Will return Memes from Reddit.

Usage:
```py
from Cu3t0mAPI import API

rs = API("api_key")
memes = rs.memes()
print(memes)
```
```
{"code":200,"post_link":"https://redd.it/r9i13b","subreddit":"memes","title":"Friendship Destroyer in a nutSHELL.","url":"https://i.redd.it/a87g8erqsq381.jpg","ups":189,"author":"1Shadowspark1","spoilers_enabled":true,"nsfw":false,"image_previews":["https://preview.redd.it/a87g8erqsq381.jpg?width=108&crop=smart&auto=webp&s=c1484e18100a3b6d2ba903ade6ecf186d069c9ee","https://preview.redd.it/a87g8erqsq381.jpg?width=216&crop=smart&auto=webp&s=3dba4111ceb5a328f971a3c55b84e251d52bd20c","https://preview.redd.it/a87g8erqsq381.jpg?width=320&crop=smart&auto=webp&s=8a0f4a2742e252fa63828cbe63bd00ba0cbbe479","https://preview.redd.it/a87g8erqsq381.jpg?width=640&crop=smart&auto=webp&s=1ae7bab3747227b0458b676fcd0a183ea9595bb8","https://preview.redd.it/a87g8erqsq381.jpg?width=960&crop=smart&auto=webp&s=44141f4bc79d4361a641b51b1a00724fb6076e62","https://preview.redd.it/a87g8erqsq381.jpg?width=1080&crop=smart&auto=webp&s=9ea0bad596f1be4f292fe090d89fe343e7cc0fb3"]}
```
# Ai Response
---
```py
Cu3t0mAPI.ai_response(question, prev_question=None)
# Question is a required argument.
```
Will return an AI response.

Usage:
```py
from Cu3t0mAPI import API

rs = API("api_key")

x=69
print("Simple use of the 'ai_response' function.")
while x == 69:
  q = input("")
  resp = rs.ai_response(q)
  response = json.loads(resp)
  print(response["response"])
  
```
```
Simple use of the 'ai_response' function.
Hi
Wassup man, how you doing.
im good
Glad to hear it. Want to read any news?
ok
<a href="http://www.msn.com/en-us/news">click here to search and view news</a>
why lol
The explanation is rather complicated.
ig it is
I see. May I ask you some simple questions?
ok
Great! How many languages can you speak?
3
3 is fine although the more the better.
bruh
I'm very enthusiastic.
clearly
Yes, it's obvious.

```