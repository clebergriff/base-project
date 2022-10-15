# create a method to read the RSS feed http://99vidas.com.br/feed.xml and return as a JSON ordered by pubDate

from datetime import datetime
import feedparser
import json
import time
import requests

feeds = [
    # pt-br
    # feed_tecmundo
    'https://rss.tecmundo.com.br/feed',
    # feed_99vidas
    'http://99vidas.com.br/feed.xml',
    # feed_olhardigital
    'https://olhardigital.com.br/feed/',
    # feed_g1
    'https://g1.globo.com/rss/g1/tecnologia/',
    # feed_xbox_br
    'https://news.xbox.com/pt-br/feed/',

    # en
    # feed_ign
    'http://feeds.ign.com/ign/games-all',
    # feed_xbox_wire
    'https://news.xbox.com/en-us/feed/',
    # feed_nintendo
    'https://mynintendonews.com/feed/',
    # feed_playstation
    'https://blog.playstation.com/feed/',
    # feed_pcgamer
    'https://www.pcgamer.com/rss/',


    # noticias br
    "http://www.ebc.com.br/rss/feed.xml",
    "https://noticias.r7.com/feed.xml",
    "http://rss.home.uol.com.br/index.xml",
    "https://riotimesonline.com/feed/",
    "http://www.brasilwire.com/feed/",
    "https://jornaldebrasilia.com.br/feed/",
    "https://www.riotimesonline.com/feed/",
    "https://www.brazilbeautynews.com/spip.php?page=backend",
    "https://www.cbc.ca/cmlink/rss-world",
    "https://www.cbc.ca/cmlink/rss-sports-cfl",
    "https://www.cbc.ca/cmlink/rss-sports-nba",
    "https://www.cbc.ca/cmlink/rss-sports-mlb",
    "https://www.cbc.ca/cmlink/rss-canada",
    "https://www.cbc.ca/cmlink/rss-canada-toronto",
    "https://www.cbc.ca/cmlink/rss-sports-nfl",
    "https://pm.gc.ca/en/news.rss",
    
    # new feeds
    "http://www.giantitp.com/comics/oots.rss",
    "http://www.engadget.com/rss.xml",
    "http://xkcd.com/atom.xml",
    "https://appleinsider.com/appleinsider.rss",
    "https://9to5mac.com/feed/",
    "http://www.vox.com/rss/index.xml"
]

summary = {
    'created': 0,
    'already_exists': 0,
    'failed': 0,
}

# API_URL = 'http://186.209.0.119:8001/api/articles/'
API_URL = 'http://localhost:8001/api/articles/'
entries = []


def get_feed(url):
    feed = feedparser.parse(url)
    return feed


def get_image(entry):
    if 'media_content' in entry:
        return entry['media_content'][0]['url']
    elif 'media_thumbnail' in entry:
        return entry['media_thumbnail'][0]['url']
    elif 'image' in entry:
        return entry['image']['href']
    elif 'links' in entry:
        for link in entry['links']:
            if link['type'].startswith('image'):
                return link['href']
    return ''


def save_bulk(entries):
    # entries is an array of objects
    # each object is an article
    # turn it into a JSON string
    entries_json = json.dumps(entries).encode('utf-8')
    r = requests.post(API_URL,
                      data=entries_json, headers={'Content-Type': 'application/json'})
    log(f"{r.status_code}, {r.reason}, {r.text}")
    summary['created'] += r.json()['created']
    summary['already_exists'] += r.json()['already_exists']
    summary['failed'] += r.json()['failed']


def save_to_database(entries):
    for entry in entries:
        entry_json = json.dumps(entry).encode('utf-8')
        r = requests.post(API_URL,
                          data=entry_json, headers={'Content-Type': 'application/json'})
        # print_log(f"{r.status_code}, {r.reason}, {r.text}")


def get_language(feed):
    return feed['feed']['language'] if 'language' in feed['feed'] else '*'


def get_title(entry):
    if 'title' in entry:
        return entry['title']
    elif 'summary' in entry:
        return entry['summary']
    return ''


def get_description(entry):
    if 'summary' in entry:
        return entry['summary']
    elif 'title' in entry:
        return entry['title']
    return ''


def get_link(entry):
    if 'link' in entry:
        return entry['link']
    elif 'id' in entry:
        return entry['id']
    return ''


def get_publish_date(entry):
    fields = ['published_parsed', 'created_parsed', 'published', 'time']
    published_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    for field in fields:
        try:
            if field in entry and entry[field]:
                published_date = time.strftime(
                    '%Y-%m-%dT%H:%M:%SZ', entry[field])
                break
        except:
            pass

    return published_date


def get_new_articles(feed):
    feed = get_feed(feed)

    for entry in feed['entries']:
        entries.append({
            "title": get_title(entry),
            "description": get_description(entry),
            "url": get_link(entry),
            "thumbnail": get_image(entry),
            "published_date": get_publish_date(entry),
            "language": get_language(feed)
        })

    if len(entries) > 200:
        save_bulk(entries)
        # save_to_database(entries)
        entries.clear()

    if len(entries) > 0:
        log(
            f'{len(entries)} entries from {feed["href"]} ready to import')


def log(message):
    # save_to_database(entries)
    # print a message as in:
    # [dd/mm/yyyy hh:mm:ss:ms] message
    print(f'[{time.strftime("%d/%m/%Y %H:%M:%S")}] {message}')


if __name__ == '__main__':

    log('* Starting import')

    for feed in feeds:
        get_new_articles(feed)

    if len(entries) > 0:
        save_bulk(entries)
        entries.clear()

    log(
        f'* Import finished! Created: {summary["created"]}, Already exists: {summary["already_exists"]}, Failed: {summary["failed"]}')
