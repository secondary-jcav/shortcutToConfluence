import json

import requests


class Confluence:

    def __init__(self, key):
        self.headers = self.build_headers(key)
        self.base_url = 'https://juliopedia.atlassian.net/wiki'
        self.api_endpoint = '/rest/api/content'

    def create_confluence_page(self, title, body='<p>This is a new page</p>'):
        """
        Creates a basic page in Confluence using the title & body provided
        """
        data = {'type': 'page', 'title': '[DRAFT] ' + title,
                'space': {'key': 'SC'},
                'body': {'storage': {'value': body, 'representation':
                    'storage'}}}
        try:
            response = requests.post(f'{self.base_url}{self.api_endpoint}', json=data, headers=self.headers)

            if response.status_code == 200:
                print(f'Confluence page "{title}" created successfully.')
            else:
                print(f'Failed to create Confluence page. Status code: {response.status_code}')
                print(response.json())

        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')

    def add_sc_link(self, page_title, url):
        data = {'title': f'{page_title}'}
        try:
            response = requests.get(f'{self.base_url}{self.api_endpoint}', json=data, headers=self.headers)
            parent_page = response.json()['results'][-1]
            comment_data = {'type': 'comment', 'container': parent_page,
                            'body': {'storage': {'value':f"<a href=\"{url}\">Link to story</a>", 'representation': 'storage'}}}
            response = requests.post(f'{self.base_url}{self.api_endpoint}',
                                     data=json.dumps(comment_data),
                                     headers=self.headers)

        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')
        print(response)

    @staticmethod
    def build_headers(token):
        headers = {
            'Authorization': f'Basic {token}',
            'Content-Type': 'application/json'
        }
        return headers
