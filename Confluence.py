import requests


class Confluence:

    def __init__(self, key):
        self.key = key
        self.base_url = 'https://juliopedia.atlassian.net/wiki'
        self.api_endpoint = '/rest/api/content'

    def create_confluence_page(self, title, body='<p>This is a new page</p>'):

        headers = {
            'Authorization': f'Basic {self.key}',
            'Content-Type': 'application/json'
        }

        data = {'type': 'page', 'title': title,
                'space': {'key': 'SC'},
                'body': {'storage': {'value': body, 'representation':
                'storage'}}}
        try:
            response = requests.post(f'{self.base_url}{self.api_endpoint}', json=data, headers=headers)

            if response.status_code == 200:
                print(f'Confluence page "{title}" created successfully.')
            else:
                print(f'Failed to create Confluence page. Status code: {response.status_code}')
                print(response.json())

        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')


    def get_confluence_page(self, id):
        base_url = 'https://juliopedia.atlassian.net/wiki/confluence'  # Replace with your Confluence URL
        api_endpoint = '/rest/api/spaces/sc/pages'

        headers = {

            'Authorization': f'Basic {self.key}',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.get(f'{base_url}{api_endpoint}{id}', headers=headers)

            if response.status_code == 200:
                print(f'Confluence page  read successfully.')
            else:
                print(f'Failed to create Confluence page. Status code: {response.status_code}')
                print(response.json())

        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')
