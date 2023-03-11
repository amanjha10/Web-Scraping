import requests
from bs4 import BeautifulSoup
with open('piano.text', 'w') as file:

    for i in range(2,11):
        url="https://www.flipkart.com/search?q=musical+keyboard+61+keys&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
        r=requests.get(url)
        # print(r)

        soup=BeautifulSoup(r.text,"lxml")
        # print(soup)

        nextpage=soup.find("a",class_ ='_1LKTO3').get("href")

        # print(nextpage)
        cnp="https://www.flipkart.com"+nextpage
        # print(cnp)

        # for i in cnp:
        #     response = requests.get(i)
        #     soup=BeautifulSoup(response.content,'lxml')

        products=soup.find_all('a',class_='s1Q9rs')
        price=soup.find_all('div',class_='_30jeq3')
        rating=soup.find_all('div',class_='_3LWZlK')
        discount=soup.find_all('div',class_='_3Ay6Sb')
        for j,x,y,z in zip(products,price,rating,discount):
            print(j.text,x.text,y.text,z.text)
            for  a,b,c,d in zip(j,x,y,z):
                file.write("Product= ")
                file.write(a.text)
                file.write('\n')
                file.write("Price= ")
                file.write(b.text.encode('ascii', 'ignore').decode('ascii'))
                file.write('\n')
                file.write("Rating= ")
                file.write(c.text)
                file.write('\n')
                file.write("Discount= ")
                file.write(d.text)
                file.write('\n')
                file.write('\n')



        
        
        
        # url=cnp
        # r=requests.get(url)
        # soup = BeautifulSoup(r.text,'lxml')