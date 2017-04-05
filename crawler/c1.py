import urllib.request
import gzip

def getContent(htmlObj):
    html = ''
    type = htmlObj.info().get('Content-Encoding')
    print(type)
    if type == 'gzip':
        html = gzip.decompress(htmlObj.read()).decode("utf-8")
    else :
        html = htmlObj.read()
    return html
if __name__ == '__main__':
    url = "http://www.baidu.com/"
    request = urllib.request.Request(url)
    request.add_header('Accept-Encoding', 'gzip')
    htmlObj = urllib.request.urlopen(request)
    html = getContent(htmlObj)
    print(html)
