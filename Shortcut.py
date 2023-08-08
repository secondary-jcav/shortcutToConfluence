import requests


class Shortcut:
    def __init__(self, key):
        self.headers = self.build_headers(key)
        self.key = key
        self.api_url_base = 'https://api.app.shortcut.com/api/v3'
        self.search_endpoint = '/search/stories'
        self.id = ''
        self.link = ''
        self.owner = ''
        self.doc_tag = 'doc_needed'
        self.title = ''
        self.body = ''
        self.labels = []

    def get_story(self, story_id):
        """
        Uses shortcut rest api to get details about a specific story
        """
        search_query = {'query': story_id, 'page_size': 1}
        try:
            url = self.api_url_base + self.search_endpoint
            response = requests.get(url, params=search_query, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
        story = response.json()['data'][0]
        self.title = story['name']
        self.id = story['id']
        self.link = story['app_url']
        self.body = story['description']
        self.labels = story['labels']
        self.owner = self.get_member(story['owner_ids'][0])
        print(self.title)

    def add_link_to_comment(self):

        pass

    def get_member(self, member_id):
        """
        Translates shortcut's member id to a name, with the idea to tag them,
        email them...
        :return: member name as string
        """
        headers = {
            "Content-Type": "application/json",
            "Shortcut-Token": self.key
        }
        try:
            url = self.api_url_base + '/members/' + member_id
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
        member = response.json()
        return member['profile']['name']

    def is_doc_needed(self):
        """
        :return: True if story has a 'doc_needed' label. False otherwise.
        """
        has_doc_label = any(label['name'] == self.doc_tag for label in self.labels)
        return has_doc_label

    def get_content_labels(self):
        """
        :return: removes doc label and returns everything else
        """
        return [string for string in self.labels if string != self.doc_tag]

    @staticmethod
    def build_headers(token):
        headers = {
            "Content-Type": "application/json",
            "Shortcut-Token": token
        }
        return headers



