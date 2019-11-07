import csv
from ural.youtube import is_youtube_url, parse_youtube_url

BLACKLIST = {
    'https://www.youtube.com',
    'http://www.youtube.com',
    'https://youtube.com',
    'http://youtube.com',
    'http://www.youtube.com/watch',
    'https://gaming.youtube.com',
    'https://music.youtube.com',
    'https://studio.youtube.com',
    'http://www.youtube.com/channels/paid_channels'
}

with open('./scripts/data/youtube-urls.csv') as f:
    reader = csv.reader(f)
    next(reader)

    for line in reader:
        youtube_url = line[1]

        if youtube_url in BLACKLIST:
            continue

        # if not is_youtube_url(youtube_url):
        #     print(youtube_url)

        result = parse_youtube_url(youtube_url)

        if result is None:
            print(youtube_url)