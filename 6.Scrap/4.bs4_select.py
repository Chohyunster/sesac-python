from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 HTML 예제</title>
</head>
<body>
    <div class="container">
        <h1>Hello</h1>
        <p>이것은 간단한 것이다</p>
    </div>
    <a herf="https://www.naver.com">
    <img src = "example1.jpg" alt="예제이미지">
    <img src = "example2.jpg" alt="예제이미지2" width='500', height='600'>

    <div class='content'>
        <ul>
            <li>항목1</li>
            <li>항목2</li>
            <li>항목3</li>
        </ul>
    </div>
    <div id="footer">
        <p>Copyright C <b>2024.</b> 이 <i>페이지는</i> 내꺼</p>
    </div>
</body>
</html>
"""

# html_doc = requests.get('https://www.naver.com').text

soup = BeautifulSoup(html_doc, 'html.parser') #html.parser, lxml.parser

link_tag = soup.select_one('a') #select의 문법 = css 셀렉터
print(link_tag)

all_imgs = soup.select('img')
print(all_imgs)

for img in all_imgs:
    print(img['src'])


content_div = soup.select_one('div.content') #주황 글씨는 div아래에 있는 content를 가져온다는 말

footer_div = soup.select_one('div#footer')
print(footer_div)

li_lists = soup.select('div.content li') #div 아래에 있는 content 클래스 아래에 있는 li들을 가져온다는 말
print(li_lists)

li_lists = soup.find_all('div_content li') #find 시리즈는 태그명 등으로 검색하는 거라 이거는 안 맞는 문법이다.
print(li_lists)

p_tag_div_footer = soup.select_one('div#footer p')
b_text = p_tag_div_footer.select_one('b').get_text()
i_text = p_tag_div_footer.select_one('i').text #텍스트로 가져오는 건 위아래 둘다 가능

print(f'볼드텍스트: {b_text}, 이탤릭텍스트: {i_text}')
