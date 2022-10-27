import requests, json
def getApi(origin,destination):
    url = "https://distanceto.p.rapidapi.com/get"

    source = origin
    dest = destination
    querystring = {"route":"[{\"t\":\""+source+"\",\"c\":\"ES\"},{\"t\":\""+dest+"\",\"c\":\"ES\"}]","car":"true"}

    headers = {
        'x-rapidapi-host': "distanceto.p.rapidapi.com",
        'x-rapidapi-key': "a365ad1a8cmsh8c4907a923c8b44p1ddecajsn2ec4d759c257"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.ok:
        data = dict(json.loads(response.text))

    return data["steps"][0]["distance"]["car"]["distance"]