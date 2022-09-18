import requests 

page = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
page.encoding ='utf-8'
changing_url = 'https://hacker-news.firebaseio.com/v0/item/16619917.json'
print(page.status_code)
content = page.json()


#print('json', page.json())
#print(dir(page))
#print(help(page.json))
urls = []
html = "<html><body>\n"
for i in content:
    urls.append(f'https://hacker-news.firebaseio.com/v0/item/{i}.json')

for url in urls:
    res = requests.get(url)
    ans:dict = res.json()
    #print(ans.keys())

    link = ans.get('url')
    author=ans['by']
    title = ans['title']
    type_ = ans['type']

    htmlrepr = f"""
        <div>
            <h2>{title}</h2>
            by <p>{author}</p>
            type:{type_}
            <a href="{link}" style="display:block; color:red;">Read more </a>
        </div>\n
    """
    print(htmlrepr)
    html+=htmlrepr
    with open('api.html', 'a') as api:
        api.write(html)

html.join("</body></html>")
with open('api.html', 'w') as api:
    api.write(html)
# #print(urls)

