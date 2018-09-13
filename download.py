import chess
import chess.pgn
import urllib2
import urllib
import zipfile
import os
import xml.etree.ElementTree as ET
import bz2

def get_urls(min_year, max_year):
    urls = []

    for year in range(min_year, max_year + 1):
        for month in range(1, 13):
            url = "https://database.lichess.org/chess960/lichess_db_chess960_rated_%s-%s.pgn.bz2" % ('%02d' % year, '%02d' % month)
            try:
                response = urllib2.urlopen(url)
                print('Adding: ' + url)
                urls.append(url)
            except urllib2.HTTPError:
                print('Not reachable: ' + url)

        return urls

def retrieve_file(url):
    print "Downloading " + url

    _file = urllib.URLopener()
    _file.retrieve(url, url.split("/")[-1])
    print "Retrieved " + url + " successfully."
    return True

def decompress(_file):
    with open(_file, 'rb') as source, open(_file[: -4], 'wb') as dest:
        dest.write(bz2.decompress(source.read()))

def download_files(min_year, max_year):
    urls = get_urls(min_year, max_year)

    for url in urls:
        _file = retrieve_file(url)
        file_name = url.split("/")[-1]
        print("Decompressing %s" % file_name)
        decompress(file_name)
        os.remove(file_name)


if __name__ == "__main__":
    download_files(2018, 2018)
