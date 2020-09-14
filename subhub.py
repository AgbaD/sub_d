#!/usr/bin/python3
# Author: @BlankGodd_

import requests
import os
from pathlib import Path
# import ast
# import json
# from bs4 import BeautifulSoup
# import re


download_dir = os.path.join(Path.home(), 'Downloads')


class Sub:
    def __init__(self):
        base_url = "https://subtitleshub.net"
        search_path = "/subtitles/search/"
        self.search_path = "".join([base_url, search_path])

    def search(self, string):
        headers = {'application': 'sub_d',
                   'User-Agent': 'https://github.com/BlankGodd/sub_d'}
        params = {'SubtitleSearch[stext]': string}
        print("Searching...")
        response = requests.get(self.search_path, params=params, headers=headers)
        print(response.status_code)


if __name__ == "__main__":
    # init class
    current_search = Sub()
    s = "friends"
    current_search.search(s)
