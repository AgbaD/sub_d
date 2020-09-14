#!/usr/bin/python3
# Author: @BlankGodd_
"""Base url and search path for different subtitle domains"""


def subub_config():
    # domain 1
    base_url = "https://subtitleshub.net"
    search_path = "/subtitles/search/"
    return base_url, search_path


Config = {
    'default': subub_config()
}
