import requests
import bs4
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
    parser = argparse.ArgumentParser(descripition='Options for scraping Google images')   #引数のhelp前に表示
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
    header={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    soup = get_soup(url,header)
    ActualImages=[]

    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =ison.loads(a.text)["ou"]   ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
    for i , (img , Type) in enumerate( ActualImages[0:max_images]):
        try:
            Type = Type if len(Type) > 0 else 'jpg'
            print("Downloading image {} ({}), type is {}".format(i, img, Type))
            raw_img = urllib.request.urlopen(img).read()
            f = open(os.path.join(save_directory , "img_"+str(i)+"."+Type), 'wb')
            f.write(raw_img)
            f.close()
        except Exception as e:
            print ("could not load : "+img)
            print (e)

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
