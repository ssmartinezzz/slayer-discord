from riotwatcher import RiotWatcher
import config

watcher = RiotWatcher(config.RIOT_TOKEN)
region = 'la2'


class Player:
    def __init__(self, name):
        """ TODAVIA NO ANDA """

        summoner = watcher.summoner.by_name(region, name)

        # Main account information
        self.name = summoner['name']
        self.summoner_level = str(summoner['summonerLevel'])
        self.revision_date = summoner['revisionDate']
        self.id = summoner['id']
        self.account_id = summoner['accountId']

        # Ranked information
        self.solo_rank = 'N/A'
        self.flex_rank = 'N/A'
        self.threes_rank = 'N/A'
        self.solo_duo_tier = 'N/A'
        self.flex_tier = 'N/A'
        self.threes_tier = 'N/A'

        self.get_ranked_stats()

    def get_ranked_stats(self):
        ranked_stats = watcher.league.positions_by_summoner(
            region, self.id)

        for stats in ranked_stats:
            queue_type = stats.get('queueType')

            if queue_type == 'RANKED_SOLO_5x5':
                self.solo_rank = rank_to_string(stats)
                self.solo_duo_tier = stats.get('tier').lower().capitalize()
            elif queue_type == 'RANKED_FLEX_SR':
                self.flex_rank = rank_to_string(stats)
                self.flex_tier = stats.get('tier').lower().capitalize()
            else:
                self.threes_rank = rank_to_string(stats)
                self.threes_tier = stats.get('tier').lower().capitalize()


def rank_to_string(ranked_stats):
    tier = ranked_stats.get('tier').lower().capitalize()
    rank = ranked_stats.get('rank')
    league_points = str(ranked_stats.get('leaguePoints'))

    ret = tier + ' ' + rank + ' (' + league_points + 'LP)'

    return ret
