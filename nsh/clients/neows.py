from datetime import datetime, timedelta
import json
from nsh.settings import NASA_API_KEY, NEOWS_HOST
from requests import get, exceptions


class NeoWs():
    date_format = '%Y-%m-%d'
    endpoints = {
        'browse': '/neo/rest/v1/neo/browse/',
        'by_date': '/neo/rest/v1/feed?start_date={}&end_date={}/',
        'detail': '/neo/rest/v1/neo/{}'
    }

    @staticmethod
    def build_url(endpoint):
        param_char = '&' if '?' in endpoint else '?'
        return f'{NEOWS_HOST}{endpoint}{param_char}api_key={NASA_API_KEY}'

    def parse_date(self, date):
        if type(date) == str:
            try:
                return datetime.strptime(date, self.date_format)
            except:
                raise TypeError('Dates should be provided in the format "MM-DD-YYYY"')
        else:
            raise TypeError('Dates should be provided in the format "MM-DD-YYYY"')

    def browse(self):
        url = self.build_url(self.endpoints.get('browse'))

        try:
            response = get(url)
        except exceptions.RequestException as e:
            print(e)

        try:
            data = json.loads(response.text)
        except:
            raise()
        
        return {'status_code': response.status_code, 'data': data}

    def get_approaches_by_date(self, start_date=None, end_date=None):
        # Set default dates
        if start_date is None: start_date = datetime.strftime(datetime.now(), self.date_format)
        if end_date is None: end_date = datetime.strftime(datetime.now() + timedelta(days=7), self.date_format)

        url = self.build_url(self.endpoints.get('by_date').format(start_date, end_date))

        try:
            response = get(url)
        except exceptions.RequestException as e:
            print(e)

        try:
            data = json.loads(response.text)
        except:
            raise()
        
        return {'status_code': response.status_code, 'data': data}

    def get_asteroid_detail(self, asteroid_id='2250680'):
        url = self.build_url(self.endpoints.get('detail').format(asteroid_id))

        try:
            response = get(url)
        except exceptions.RequestException as e:
            print(e)

        try:
            data = json.loads(response.text)
        except:
            raise()
        
        return {'status_code': response.status_code, 'data': data}
