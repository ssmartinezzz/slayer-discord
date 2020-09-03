from requests import *
from riotwatcher import *
import config
import json

watcher = LolWatcher(config.RIOT_TOKEN)

region = 'la2'


def get_summoner(summoner):
    try:
        summ = watcher.summoner.by_name(region=region, summoner_name=summoner)
        league = watcher.league.by_summoner(region=region, encrypted_summoner_id=summ['id'])
        json.dumps(league)
        name = summ['name']
        level = summ['summonerLevel']
        #tier = league['tier']
        #rank = league['rank']

        return f"Perfil encontrado: {name} \n\n Nivel {level} \n\n " # Error al usar liga tipo de objetoLiga : {tier} "

    except HTTPError:
        return "Summoner no encontrado!"
