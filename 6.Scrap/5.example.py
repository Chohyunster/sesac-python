import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page3.html'
#웹에서 ctl shift c 눌러서(f12의 소스) 어디서 뭘 가져올지 판독한다. 

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

#여기에서 상품명과 가격을 출력하시오

# table_tag = soup.find('table', id='gistList') 아래랑 같음.
table_tag = soup.select_one('#giftList')

product_trs = table_tag.find_all('tr')
print(product_trs)

item_list = []

for product_tr in product_trs[1:]:
    product_tds = product_tr.select('td')
    # print(product_tds[0], product_tds[2])
    item_list.append((product_tds[0].text.strip(), product_tds[2].text.strip() ))
    # print(f'상품명: {product_tds[0].text.strip()}, 가격: {product_tds[2].text.strip()}') #공백을 제거해야 줄바꿈이 안된다.

print(item_list)

for item in item_list:
    print(f'상품명: {item[0]}, 가격: {item[1]}')


