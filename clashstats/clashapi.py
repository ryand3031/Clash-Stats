import requests
import json
from . import config
#ADD clash API key here
key = config.api_key
def get_player_info(pid):
    r=requests.get( f"https://proxy.royaleapi.dev/v1/players/%23{pid}", headers={"Accept":"application/json", "authorization":f"Bearer {key}"}, params = {"limit":20})
    #print(json.dumps(r.json(), indent = 2))
    return r.json()

def get_player_chests(pid):
    r=requests.get( f"https://proxy.royaleapi.dev/v1/players/%23{pid}/upcomingchests", headers={"Accept":"application/json", "authorization":f"Bearer {key}"}, params = {"limit":20})
    return r.json()


def addWinRate(playerInfo):
    totalBattles = (playerInfo['wins']+playerInfo['losses'])
    playerInfo['winRate'] = round((playerInfo['wins']/totalBattles)*100,2)
    playerInfo['threeCrownRate'] = round(playerInfo['threeCrownWins']/totalBattles*100, 2)


# playid = 'YQJVLLY8'
# r=requests.get(f"https://api.clashroyale.com/v1/players/%23{playid}", headers={"Accept":"application/json", "authorization":f"Bearer {key}"}, params = {"limit":20})
# print(r.json()['name'])