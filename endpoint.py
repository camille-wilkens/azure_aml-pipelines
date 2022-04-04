import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://b9cf3749-154a-464c-912e-c3a88f8409a6.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'YXl253qjvEEXHhIfRvc18FUmcerc68SA'




# Request data goes here
data = {
    "Inputs": {
        "data":
        [
            {
                "age": "53",
                "job": "technician",
                "marital": "married",
                "education": "professional.course",
                "default": "no",
                "housing": "no",
                "loan": "yes",
                "contact": "cellular",
                "month": "jul",
                "day_of_week": "tue",
                "duration": "178",
                "campaign": "11",
                "pdays": "999",
                "previous": "0",
                "poutcome": "nonexistent",
                "emp.var.rate": "1.4",
                "cons.price.idx": "93.918",
                "cons.conf.idx": "-42.7",
                "euribor3m": "4.961",
                "nr.employed": "5228.1"
            },
            {
                "age": "24",
                "job": "blue-ollar",
                "marital": "married",
                "education": "professional.course",
                "default": "no",
                "housing": "no",
                "loan": "yes",
                "contact": "cellular",
                "month": "may",
                "day_of_week": "tue",
                "duration": "178",
                "campaign": "1",
                "pdays": "999",
                "previous": "1",
                "poutcome": "nonexistent",
                "emp.var.rate": "-1.4",
                "cons.price.idx": "93.918",
                "cons.conf.idx": "-46.7",
                "euribor3m": "1.961",
                "nr.employed": "6228.1"
            },
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}

body = str.encode(json.dumps(data))


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

req = urllib.request.Request(scoring_uri, body, headers)

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)


try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))