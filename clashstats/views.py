from django.shortcuts import render
from . import clashapi
#'#YQJVLLY8'


def home_page(request):
    return render(request, 'home.html')

def player_page(request, player_id):
    
    playerInfo = clashapi.get_player_info(player_id)
    print(playerInfo['name'])
    contex = {
        'pid': player_id
    }
    return render(request, 'player.html', playerInfo)

def search(request):
    if request.method == 'GET' and request.GET['pid'] :
        pid = request.GET['pid'].upper()
        #print(pid[1:])
        if(pid[0]=='#'):
            pid=pid[1:]
        playerInfo = clashapi.get_player_info(pid)
        #print(playerInfo)
        if('tag' in playerInfo):
            clashapi.addWinRate(playerInfo)
            chestInfo = clashapi.get_player_chests(pid)
            #print(chestInfo)
            playerInfo['chestInfo'] = chestInfo
            print(playerInfo['chestInfo'])
            return render(request, 'player.html', playerInfo)
    return render(request, 'notfound.html')

# 'YQJVLLY8'