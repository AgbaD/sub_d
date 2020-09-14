#!/usr/bin/python3
# Author: @BlankGodd_

import requests
import os
from pathlib import Path
# import ast
# import json
from bs4 import BeautifulSoup as bs
import re


download_dir = os.path.join(Path.home(), 'Downloads')


class Sub:
    def __init__(self):
        self.base_url = "https://subtitleshub.net"

    def search(self, string):
        path = "/subtitles/search/"
        search_path = "".join([self.base_url, path])

        headers = {'application': 'sub_d',
                   'User-Agent': 'https://github.com/BlankGodd/sub_d'}
        if string.split(' '):
            string = string.split(' ')
            string = '+'.join(string)
        params = {'SubtitleSearch[stext]': string}
        print("Searching...")
        response = requests.get(search_path, params=params, headers=headers)
        if response.status_code != 200:
            return None
        
        html = bs(response.content, 'html.parser')
        table = html.find_all('span', attrs={'class': 'movie_name'})
        movies = {}
        for movie in table:
            title = movie.text
            raw_link = movie.find('a')
            link = raw_link['href']
            movies[title] = link
        return movies

    def get_sub(self, link):
        sub_path = "".join([self.base_url, link])

        headers = {'application': 'sub_d',
                   'User-Agent': 'https://github.com/BlankGodd/sub_d'}
        response = requests.get(sub_path, headers=headers)
        if response.status_code != 200:
            return None
        html = bs(response.content, 'html.parser')

        if html.find('td', string=re.compile('season')):
            ses = html.find('td', attrs={'id': 'rating_td'}).find_all('a', string=re.compile('#'))


if __name__ == "__main__":
    # init class
    current_search = Sub()
    s = "friends"
    movies = current_search.search(s)
    current_search.get_sub(movies['Friends (1994)'])
