from googlesearch import search
import googlesearch

def get_query_links(query):
    links = []
    for j in search(query, tld="com", num=10, stop=10, pause=2): 
        links.append(j)

    return links

