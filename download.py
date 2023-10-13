from flickrapi import FlickrAPI   # flickrapi
from urllib.request import urlretrieve  # urlretrieve
from pprint import pprint               # pprint
import os
import time
import sys                               # os, time, sys

# APIキーの情報
key = "a726238ced8937b6b5447c482f08926a" # APIキー
secret = "9afe7c106a20fb4e"               # シークレットキー
waite_time = 1                             # 待機時間

# 保存フォルダの指定
vegetable = sys.argv[1]                   # 検索ワード
savedir = "./" + vegetable               # 保存フォルダ

# FlickrAPIの設定
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = vegetable,           # 検索ワード
    per_page = 400,             # 取得件数
    media = 'photos',           # 写真を検索
    sort = "relevance",         # 検索語の関連順に取得
    safe_search = 1,            # セーフサーチ
    extras = 'url_q, licence'   # 追加情報の指定
)

# 結果の確認
photos = result['photos']
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(waite_time)