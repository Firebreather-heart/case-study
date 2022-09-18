from celery import shared_task
from .models import NewsObject


@shared_task
def sync(id, type_, url, author, title, status='ext',):
    try:
        obj = NewsObject.ext.get(id=id)
    except:
        pass 
    newobj = NewsObject(id = id, type=type_ , author=author, title=title)
    newobj.save()
    return 

