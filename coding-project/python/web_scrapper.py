import requests
import inflection

def get_web_titles():

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    
    posts = r.json()

    web_titles = []

    for post in posts:
        title = post['title'] 
        web_title = inflection.titleize(title) 
        web_titles.append(web_title)  

    return web_titles
    


titles = get_web_titles()
for title in titles:
    print(title)

