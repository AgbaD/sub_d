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


class SubError(Exception):
    pass


class Sub:
    def __init__(self):
        self.base_url = "https://subtitleshub.net"

    def search(self, string):
        path = "/subtitles/search/"
        search_path = "".join([self.base_url, path])

        headers = {'application': 'sub_d',
                   'User-Agent': 'https://github.com/BlankGodd/sub_d'}
        print(f"Title: {string}")
        print()
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

        if html.find('td', attrs={'class': 'name'}, string=re.compile('season')):
            seasons = html.find('td', attrs={'id': 'rating_td'}).find_all('a', string=re.compile('#'))
            print('Seasons...')
            for season in seasons:
                print(season.text)
            print()
            season = input("Enter season e.g 1 or #1: ")
            if int(season) > len(seasons):
                raise SubError('Invalid Input')
            if len(season) == 1:
                pass
            else:
                if season[0] == '#':
                    season = season[1:]
                else:
                    pass
            season = "season " + str(season)
            print()
            print(season)
            print()
            link_html = html.find_all('td', attrs={'colspan': '4'})
            for i in link_html:
                if i.find('a', string=re.compile(season)):
                    link_html = i.find('a', string=re.compile(season))
                    break
            link = link_html['href']
            full_link = ''.join([self.base_url, link])
            response1 = requests.get(full_link, headers=headers)
            html1 = bs(response1.content, 'html.parser')
            episodes_raw = html1.find_all('span', attrs={'class': 'movie_name'})
            i = 1
            episodes = {}
            for epi in episodes_raw:
                episode = epi.find('a')
                link = episode['href']
                title = episode.text
                episodes[title] = link
            for k in episodes.keys():
                print("NUMBER: ", i, "\n", k)
                print()
                i += 1
            print()
            episode = input("Enter episode number: ")
            episode = int(episode) - 1
            titles = [k for k in episodes.keys()]
            try:
                title = titles[episode]
            except:
                raise SubError('Invalid Input')
            link = episodes[title]
            main_link = ''.join([self.base_url, link])
            response2 = requests.get(main_link, headers=headers)
            html2 = bs(response2.content, 'html.parser')
            from pprint import pprint
            pprint(html2)

            try:
                span = html2.find_all('span', attrs={'class': 'item'})
                link = None
                for i in span:
                    link = i.find('a', string=re.compile('English'))
                link = link['href']
                print(link)
                real_link = ''.join([self.base_url, link])
                response3 = requests.get(real_link, headers=headers)
                print('ok')
            except:
                print('not ok')


if __name__ == "__main__":
    # init class
    current_search = Sub()
    s = "Friends"
    movies = current_search.search(s)
    current_search.get_sub(movies['Friends (1994)'])
