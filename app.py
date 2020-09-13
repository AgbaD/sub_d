#!/usr/bin/python3
# Author: @BlankGodd_

import requests
import os
from pathlib import Path


def subub_config():
    base_url = "https://subtitleshub.net"
    search_path = "/subtitles/search/?SubtitleSearch[stext]="
    return base_url, search_path


download_dir = os.path.join(Path.home(), 'Downloads')


def search(s):
    pass
