# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from pprint import pprint
from typing import Dict

import praw as praw


class RedditProductSearch:
    def __init__(self, auth_creds):
        pprint(auth_creds)
        self.reddit_client = praw.Reddit(client_id=auth_creds['client_id'],
                                 client_secret=auth_creds['client_secret'],
                                 user_agent=auth_creds['user_agent'],
                                 username=auth_creds['username'],
                                 password=auth_creds['password'])

    def search(self, product_search_query: str):
        all = self.reddit_client.subreddit("all")
        search_results = all.search(product_search_query)
        for submission in search_results:
            pprint(submission.title + ":")
            for comment in submission.comments:
                pprint(comment.body)
                print("_______")
            print("#################")
            print("")


def get_reddit_auth_creds() -> Dict[str, str]:
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    user_agent = os.getenv('USER_AGENT')
    username = os.getenv('REDDIT_USERNAME')
    password = os.getenv('PASSWORD')


    if client_id and client_secret and user_agent and username and password:
        return {
            'client_id': client_id,
            'client_secret': client_secret,
            'user_agent': user_agent,
            'username': username,
            'password': password
        }
    else:
        raise Exception("check if auth variables declared")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    auth_creds = get_reddit_auth_creds()
    reddit_prod = RedditProductSearch(auth_creds)
    reddit_prod.search('best budget vacuum cleaner')

