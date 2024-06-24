#pip install bs4

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 HTML 예제</title>
</head>
<body>
    <h1>Hello</h1>
    <p>이것은 간단한 것이다</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser') #html.parser(기본 파서), lxml.parser(추가설치해야 하는 파서)
print(html_doc)
print(soup)

print(soup.head)
print(soup.body.h1.text)