# you gotta download the library before you use it
# pip install _______
# if you dont have pip, go google how to download it
# its a pain in the dick if you dont do it right
# anyways here's a library that's commonly used: requests and json
import requests
import json

# you can import sub-libraries of libraries as well
# this one usually goes hand-in-hand with requests
from requests.auth import HTTPBasicAuth
# HTTPBasicAuth can simulate a username password combination, or key+username, or other security authorization

# requests is a library that lets you make api calls
# api call (also called HTTP Requests) = communicating with another web server and doing stuff
# typically, an api call consists of 3 parts
    # 1. an endpoint - a url, the server youre communicating with
    # 2. headers - information about the data thats being sent, the data thats being sent back from the endpoint, and authentication information (api keys etc)
    # 3. payload/data - data you're sending to the endpoint
# typically your calls will look something like this:

# API keys are basically a key that's generated that allows your code to access endpoints
# like a key to unlock the door to your house
# typically the level of access you get once you're in the dev section matches your regular access to the software
# if im making an API call to access a document, if i cant access that document regularly on the software, i cant access it with my api calls
# either that or the keys are generated with attached permissions, separate from your typical levels of access

# API keys are either obtained by:
# 1. creating it yourself on the website (usually most software has a developer/API section that handles key generation)
# 2. asking your manager lmao
KEY = "##########"

# all software has several endpoints you can send your request to
# you have to read the developer documentation to figure out where to point your calls to
url = "https://www.yourendpoint.net/api/endpoint"

# headers typically contain these same 3 things
headers = {
    'Authorization': KEY,
    'Content-Type': 'application/json',
    'Accepts': 'application/json'
}

# typically you use data to refine your search
# or the endpoint forces you to put certain fields into your endpoints to make sure you're getting the right data as a response
# some developers call this the "payload", instead of "data"
data = {
    'user_id': 'xxxxxxxxx',
    'username': 'xxxxxxxxx',
}

# this is the call itself
# API Calls/HTTP Requests have 6 methods you can do
# GET - Get data from the endpoint
# POST - Post data to the endpoint
# PUT - Replace the data that exists at that endpoint, in the response, with the data in your... data. Or Payload if you specified it as Payload
# DELETE - Delete the specified resource within the endpoint
# there's more but for now just get used to those 4
response = requests.get(url=url, headers=headers, data=data)

# the response is typically returned as a JSON object
# basically, a JSON object looks like this (we'll also use this as our example response):
# {
#   status_code: '200',
#   user_info: {
#       user_id: 'xxxxxxx'
#       username: 'austin@austin.com'
#   }
# }
# we'll save this for a future lesson, this requires its own little explanation, but we'll probably go over that in part 6

# let's go over HTTPBasicAuth while we're here (i mentioned it earlier anyways so might as well)
# sometimes the endpoint forces you to go through some type of authorization if you wanna access the resources there
# HTTPBasicAuth gives you some built in functions that allow you to do some basic authorization as part of your request
# for example, let's use HTTPBasicAuth to simulate a username and password combo

username = "austin@austin.com"
password = "dog123"

headers = {
    'Authorization': HTTPBasicAuth(username, password),
    'Content-Type': 'application/json',
    'Accepts': 'application/json'
}

data = {
    'user_id': 'xxxxxxxxx',
    'username': 'xxxxxxxxx',
}

response = requests.get(url=url, headers=headers, data=data)

# it mostly looks the same, sometimes Authorization isn't a part of the header, so it'll look something like this:

headers = {
    'Content-Type': 'application/json',
    'Accepts': 'application/json'
}

auth = HTTPBasicAuth(username, password)

data = {
    'whocares': 'i dont im tired'
}

response = requests.post(url=url, auth=auth, headers=headers, data=data)

# now with this go ahead and go fiddle around with API calls
# most software has an api you can call to, just manage to get credentials (a key) if you can
# google "[name of software] developers" or "[name of software] api" and youll be surprised at how much data you can retrieve