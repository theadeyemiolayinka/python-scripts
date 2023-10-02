import requests

class ValorantStats:
    def __init__(self, nick, tag, region) -> None:
        self._base_url    = 'https://api.henrikdev.xyz/valorant/v2/mmr'
        self._region_list = ['eu', 'na,' 'latam', 'br', 'ap', 'kr']
        self._region      = region
        self._nick        = nick
        self._tag         = tag
        self._stats_text  = None 

        # Test Region
        self.set_region()

    def set_region(self) -> None:
        if self._region not in self._region_list:
            print('[ERROR] Invalid region\nAvaiable regions: eu, na, latam, br, ap, kr!')
            return 

    def build_url(self) -> str:
        return f'{self._base_url}/{self._region}/{self._nick}/{self._tag}'

    def get_stats(self) -> dict:
        if self._stats_text is not None:
            return self._stats_text
        
        try:
            response = requests.get( self.build_url() )
        except:
            print('[ERROR] API Response!')
        
        if response.status_code == 200:
            data = response.json()
        
        self._rank = data['data']['current_data']['currenttierpatched']
        self._highest_rank = data['data']['highest_rank']['patched_tier']

        self._stats_text = (
            f'Nick: {self._nick}#{self._tag}\n'+
            f'Tier: {self._rank}\n'+
            f'Highest Tier: {self._highest_rank}'
        )

        return self._stats_text

if __name__ == '__main__':
    # Parameters Example
    nick   = 'blessed'
    tag    = 'dream'
    region = 'br'

    player_obj = ValorantStats(nick, tag, region)
    print(player_obj.get_stats())