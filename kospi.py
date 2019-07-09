import requests
import bs4

url = "https://finance.naver.com/sise/"

response = requests.get(url).text

document = bs4.BeautifulSoup(response, "html.parser")

kospi = document.select_one("#KOSPI_now").text
kosdaq = document.select_one("#KOSDAQ_now").text
print("KOSPI 지수 : " + kospi)
print("KOSDAQ 지수 : " + kosdaq)


url2 = "https://www.naver.com"
response2 = requests.get(url2).text
doc2 = bs4.BeautifulSoup(response2,'html.parser')
firstsearch = doc2.select_one("ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)").text
print(firstsearch)

#for i in range(1,11) : 
#    searchlist = doc2.select("ul.ah_l:nth-child(5) > li:nth-child(" + str(i) + ") > a:nth-child(1) > span:nth-child(2)")
#    for search in searchlist : 
#        print(search.text)

# 밑의 방식이 더 좋다. css 체크하자.
rank = doc2.select('.ah_k')
for i in range(0,10) :
    print(rank[i].text)



    
    
