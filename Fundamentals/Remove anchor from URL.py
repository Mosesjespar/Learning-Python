# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

def remove_url_anchor(url):
    # TODO: complete
    x = '#'
    if x in url:
        url = url[0:url.index(x)]
        return url
    else:
        return url