from dotenv import load_dotenv, find_dotenv
import os

from Confluence import Confluence as cf
from Shortcut import Shortcut as sc
from DocWriter import DocWriter as dw


def write_draft(subject_matter, title, details):
    cf_api_key = os.environ['CONFLUENCE_TOKEN']
    gpt_api_key = os.environ['GPT_TOKEN']
    writer = dw(gpt_api_key)
    docs = cf(cf_api_key)
    draft = writer.get_completions_response(subject_matter, title, details)
    docs.create_confluence_page(story.title, draft)


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())  # read local .env file
    sc_api_key = os.environ['SHORTCUT_TOKEN']
    story = sc(sc_api_key)
    story.get_story(22)
    print(f'Does it need docs: {story.is_doc_needed()}')
    if story.is_doc_needed():
        domain = story.get_content_labels()[0]["name"]
        write_draft(domain, story.title, story.body)
