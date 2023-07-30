from dotenv import load_dotenv, find_dotenv
import os

from Confluence import Confluence as cf
from Shortcut import Shortcut as sc

# def get_completion(inputs, parameters=None,ENDPOINT_URL=os.environ['HF_API_SUMMARY_BASE']):
#     headers = {
#       "Authorization": f"Bearer {hf_api_key}",
#       "Content-Type": "application/json"
#     }
#     data = { "inputs": inputs }
#     if parameters is not None:
#         data.update({"parameters": parameters})
#     response = requests.request("POST",
#                                 ENDPOINT_URL, headers=headers,
#                                 data=json.dumps(data)
#                                )
#     return json.loads(response.content.decode("utf-8"))
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())  # read local .env file
    sc_api_key = os.environ['SHORTCUT_TOKEN']
    cf_api_key = os.environ['CONFLUENCE_TOKEN']
    story = sc(sc_api_key)
    story.get_story(16)
    print(f'Does it need docs: {story.is_doc_needed()}')
    if story.is_doc_needed():
        docs = cf(cf_api_key)
        docs.create_confluence_page(story.title, story.body)


