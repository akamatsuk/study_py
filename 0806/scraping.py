import requests  #HTMLの取得
import bs4   #HTMLのパース処理
import re
import urllib.request, urllib.error
import os
import argparse
import sys
import json

def get_soup(url,header):
    return bs4.Beautifulsoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')
# -s: Google Imagesにかける検索キーワード、複数可 (デフォルト "banana") 
# -n: ダウンロードする画像の数量 (デフォルト 10枚)
# -o: 画像の保存先 (デフォルト　<DEFAULT_SAVE_DIRECTORY>で指定する)
def main(args):
    parser = argparse.ArgumentParser(descripition='Options for scraping Google images')　　#引数のhelp前に表示
    parser.add_argument('-s', '--search', default='banana', type=str, help='search term')   #引数の追加
    parser.add_argument('-n', '--num_images', default=10, type=int, help='num of images to scrape')
    parser.add_argument('-o', '--directory', default='<DEFAULT_SAVE_DIRECTORY>', type=str, help='output directory')
    args = parser.parse_args()

    #複数ワードをつなげる
    query = args.search.split()
    query = '+'.join(query)
    max_images = args.num_images
    
    #画像をグループ化する
    save_directory = args.directory + '/' + query
    if not os.path.exists(save_directiory):
        os.makedirs(save_directory)

    # scraping
    url="https://www.google.co.jp/search?q="+query+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0(Windoxs NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    ActualImages=[]