import requests


class Shortcut:
    def __init__(self, key):
        self.key = key
        self.api_url_base = 'https://api.app.shortcut.com/api/beta'
        self.search_endpoint = '/search/stories'
        self.doc_tag = 'doc'
        self.title = ''
        self.body = ''
        self.comments = []
        self.labels = []

    def get_story(self, story_id):
        """
        Uses shortcut rest api to get details about a specific story
        """
        search_query = {'query': story_id, 'page_size': 1}
        try:
            url = self.api_url_base + self.search_endpoint + '?token=' + self.key
            response = requests.get(url, params=search_query)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
        story = response.json()['data'][0]
        self.title = story['name']
        self.body = story['description']
        self.comments = story['comments']
        self.labels = story['labels']
        print(self.title)

    def is_doc_needed(self):
        """
        :return: True if story has a 'doc needed' label. False otherwise.
        """
        has_doc_label = any(label['name'] == self.doc_tag for label in self.labels)
        return has_doc_label






