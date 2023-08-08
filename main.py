from dotenv import load_dotenv, find_dotenv
import os

from Confluence import Confluence
from Shortcut import Shortcut
from ContentGenerator import ContentGenerator


def write_draft(subject_matter, title, details):
    """
    Uses ContentGenerator class to ask the GPT endpoint.
    Uses Confluence class to post to confluence.
    """
    cf_api_key = os.environ['CONFLUENCE_TOKEN']
    gpt_api_key = os.environ['GPT_TOKEN']
    bot = ContentGenerator(gpt_api_key)
    # Get GPT response
    draft = bot.get_completions_response(subject_matter, title, details)
    # Post to confluence
    docs = Confluence(cf_api_key)
    docs.create_confluence_page(story.title, draft)
    # Shortcut link in confluence
    docs.add_link(story.title, story.link)
    # Confluence link in shortcut
    story.add_link_to_comment(story.id, docs.post_link)


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())  # read local .env file
    sc_api_key = os.environ['SHORTCUT_TOKEN']
    story = Shortcut(sc_api_key)
    # Get story details
    story.get_story(22)
    print(f'Does it need docs: {story.is_doc_needed()}')
    if story.is_doc_needed():
        domain = story.get_content_labels()[0]["name"]
        write_draft(domain, story.title, story.body)
