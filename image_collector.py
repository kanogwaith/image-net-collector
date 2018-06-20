#!/usr/bin/env python3

import requests
import os
import sys
from pymongo import MongoClient

def get_pic(http, pic_path, coll, is_cat=True):
    '''
    get_pic() downloads the picture by the URL given and makes a record in the database
    '''
    r_pic = requests.get(http)
    filename = http.split('/')[-1]
    with open(pic_path + filename, 'wb') as f:
        f.write(r_pic.content)
    if is_cat:
        coll.insert_one({'category': 'cat', 'path': pic_path + filename})
    else:
        coll.insert_one({'category': 'dog', 'path': pic_path + filename})

def collect(st_cat, st_dog):
    '''
    collect() is the main function, it takes the data from image-net.org
    '''

    #проверка формата вызова команды
    if __name__ == '__main__' and len(sys.argv) != 2:
        print('Usage: {} <amount_of_pics>'.format(sys.argv[0]))
        sys.exit(1)

    #сбор списка синсетов с сайта, приведение в удобный для парсинга вид
    r = requests.get('http://image-net.org/archive/words.txt')
    synset_dict = r.text.split('\n')
    print('List of synsets is ready!')

    #поиск по синсетам
    for i in synset_dict:
        if st_cat in i:
            cat_synset = i.split()[0]
        if st_dog in i:
            dog_synset = i.split()[0]

    #для найденных синсетов получаются списки ссылок
    r = requests.get('http://image-net.org/api/text/imagenet.synset.geturls?wnid=' + do$
    dog_dict = r.text.split('\r\n')
    print('Dogs are almost ready!')

    #создание папок
    if not (os.path.exists('data/train/cat')):
        os.makedirs('data/train/cat')
    if not (os.path.exists('data/train/dog')):
        os.makedirs('data/train/dog')
    if not (os.path.exists('data/test/cat')):
        os.makedirs('data/test/cat')
    if not (os.path.exists('data/test/dog')):
        os.makedirs('data/test/dog')

    #подсчет нужного количества изображений
    amount_train = round(int(sys.argv[1])*0.8)
    amount_test = int(sys.argv[1]) - amount_train

    #подключение к БД, самый простой вариант
    client = MongoClient('localhost', 27017)
    db = client.image_base
    coll = db.coll_cats_dogs

    #скачивание картинок, заполнение базы
    for i in range(amount_train):
        get_pic(cat_dict[i], 'data/train/cat/', coll)
        get_pic(dog_dict[i], 'data/train/dog/', coll, is_cat=False)
    print('Train base is done!')
    for i in range(amount_train, amount_train + amount_test):
        get_pic(cat_dict[i], 'data/test/cat/', coll)
        get_pic(dog_dict[i], 'data/test/dog/', coll, is_cat=False)
    print('Test base is done!')
    sys.exit(0)

if __name__ == '__main__':
    collect('domestic cat', 'domestic dog')

