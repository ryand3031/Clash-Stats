import requests
import json

#ADD clash API key here
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZjYTU0ZDBmLTM0OWMtNGYxZi05MTBlLWYzYmEzOGU4ZTVhNCIsImlhdCI6MTYzMTE0ODA3Niwic3ViIjoiZGV2ZWxvcGVyLzYxODg1YzA5LWQ0NjYtOWVlMC1hYjQ0LTA5MGI5NGZlYzM3NCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMjguMTI4LjEyOC4xMjgiXSwidHlwZSI6ImNsaWVudCJ9XX0.Ch_c0BkFbgFqdo9XzJh-BYVceXm6_PwMiLhvXCo7aBgOsRSMjrLkIiQvK8zgPC7E17tp8paftk-jPQVqs9RQ8Q"

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