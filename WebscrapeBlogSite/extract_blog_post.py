import csv
import requests
from bs4 import BeautifulSoup

# this program does the following:
# get link inside a csv
# make request to that link
# scrape the page for the blog title
# scrape the page for the blog text
# do this for all links in the csv

blog_list = []

# read the csv and make a list out of the rows
with open("SarahsBlogPosts.csv") as csv_file:
    reader = csv.reader(csv_file)
    reader_list = list(reader)

# iter over the rows excluding the header row
for row in reader_list[1:]:
    # words[] will store all words in one blog post to get rid of extra whitespace, then rejoining the words later
    words = []
    title = row[0]  # title of blog post
    href = row[1]  # blog post link
    response = requests.get(href)  # make a request to the blog post link
    soup = BeautifulSoup(response.text, "html.parser")  # create the soup
    article_content = soup.section.find_all("p")  # get all p tags of the section tag

    # iter over the list of p tags
    for content in article_content:
        s = str(content.get_text()).strip()  # a stripped string from a p tag
        words += s.split()  # add the words from p tag to the list of words getting rid of extra whitespace

    # finally, append the title of the post, and words[] as a single string, to the list of blog posts
    blog_list.append((title, ' '.join(words)))

print(blog_list[3][1])

#TODO - Make every blog post organized on the print screen and save it to a file

#TODO - search the blog posts for a search term, and return the title and link to the blogpost with the search term