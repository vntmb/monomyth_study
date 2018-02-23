import re
import requests
import lxml.html

num_movies = 899

for num in range(1, num_movies + 1):

    num = str(num)
    # Find the movie's title to be used as document name
    title_url = "http://moviegalaxies.com/movies/" + num
    edge = ") " # Right most edge of the film's title before irrelevant information
    content = lxml.html.parse(title_url)
    title = content.find(".//title").text
    movie_title = title[:title.find(edge) + 1] # Find movie title
    movie_title = re.sub(r'[~#%&*{}\:<>?/+|"\']', '', movie_title)

    # Download document and give it movie's title
    root = "http://media.moviegalaxies.com/gexf/"
    suf = ".gexf"
    url = root + num + suf
    r = requests.get(url, allow_redirects=True)
    open(movie_title + ".xml", "wb").write(r.content)
