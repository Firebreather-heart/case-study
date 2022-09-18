from django.conf import settings
from json import JSONDecodeError
from django.db import IntegrityError
import requests
from  hacker.models import NewsObject


class ApiObject:
    def __init__(self, link, author, title, type_, id) -> None:
        self.link = link 
        self.author = author 
        self.title = title 
        self.type_ = type_
        self.id = id

    def to_db(self):
        try:
            obj = NewsObject(type=self.type_, url = self.link, id=self.id, title= self.title, author=self.author,)
            obj.save()
        except IntegrityError:
            print("Object exists in db already")
        except:
            print('failed to save')

def spewApiContent(url_one:str="https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty",length:int=100):
    try:
        resp = requests.get(url_one)
    except ConnectionError:
        print('Connection error')
    else:
        try:
            json__ = resp.json()
        except JSONDecodeError:
            return JSONDecodeError("The Api Url has no valid Json content")
        else:
            for i in json__[:length]:
                url_two = f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
                try:
                    ans = requests.get(url_two).json()
                except ConnectionError:
                    print("Connection Failure")
                else:
                    link = ans.get('url')
                    author=ans['by']
                    id = ans['id']
                    title = ans['title']
                    type_ = ans['type']
                    ret_obj = ApiObject(link, author, title, type_, id).to_db()
                    print('saved, .........., working')
        
def schedule_api():
    spewApiContent(length=5) 
    print('db_updated')
