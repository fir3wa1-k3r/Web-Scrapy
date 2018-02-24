#                                                    <<<<by fir3wa1k3r>>>>
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

#url of the website
url="https://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=routers&rh=i%3Aaps%2Ck%3Arouters"

#grab the contents of the site
content = req(url)
#reading the data
grab = content.read()
#closing the connection
content.close()
#file name
fname = input("Please Enter the name of the .csv file to be saved as:")
fname = fname+".csv"

#open file to write data
fp = open(fname,"w")
header = "Product, Price\n"
fp.write(header)

#parsing the contents in the html format
html_parse=soup(grab, "html.parser")
#collect info about each product
containers = html_parse.findAll("div",{"class":"s-item-container"})

for container in containers:

	#title of the product
	pro = container.findAll("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
	pro_title = pro[0]
	title = pro_title["title"]

	cost = container.findAll("span",{"class":"a-size-base a-color-price s-price a-text-bold"})
	price = cost[0].text.strip()
	
	print("Product: " + title)
	print("Price: " + price)

	fp.write(title + "," + price.replace(",","") + "\n")
#close the csv file
fp.close()
