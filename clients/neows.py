from nsh.nsh.settings import NASA_API_KEY, NEOWS_HOST
from requests import get, exceptions


class NeoWs():
    endpoints = {
        'browse': '/neo/rest/v1/neo/browse/',
        'by_date': '/neo/rest/v1/feed?start_date={}&end_date={}/',
        'detail': '/neo/rest/v1/neo/{}'
    }

    @staticmethod
    def build_url(endpoint):
        param_char = '&' if '?' in endpoint else '?'
        return f'{NEOWS_HOST}{endpoint}{param_char}api_key={NASA_API_KEY}'

    def browse(self):
        url = self.build_url(self.endpoints.get('browse'))

        try:
            response = get(url)
        except exceptions.RequestException as e:
            print(e)
        
        return response

    def get_approaches_by_date(self, start_date='2021-08-01', end_date='2021-08-07'):
        url = self.build_url(self.endpoints.get('by_date').format(start_date, end_date))

        try:
            response = get(url)
        except Exception as e:
            print(e)
        
        return response

    def get_asteroid_detail(self, asteroid_id='2250680'):
        url = self.build_url(self.endpoints.get('detail').format(asteroid_id))

        try:
            response = get(url)
        except Exception as e:
            print(e)
        
        return response
