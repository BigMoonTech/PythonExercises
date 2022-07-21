
from bs4 import BeautifulSoup
import requests
import csv

sara_url = "https://www.sarasoueidan.com/blog/"
res = requests.get(url=sara_url)
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.find_all(class_="blog__post")
blog_list = []

for title in titles:
    title_txt = title.get_text()
    l = title_txt.split()
    fixed_title = ' '.join(l)
    url_prefix = "https://www.sarasoueidan.com"
    parent_href = title.parent["href"]
    url = url_prefix + parent_href
    blog_list.append({"Blog Title": fixed_title, "href" : url})
    print(fixed_title)
    print(f"{url}\n")

with open("SarahsBlogPosts.csv", "w") as csv_file:
    headers = ["Blog Title", "href"]
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for blog in blog_list:
        writer.writerow(blog)
