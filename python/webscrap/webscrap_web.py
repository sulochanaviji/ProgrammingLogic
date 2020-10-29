//program to scraping a data from html file and writing data to csv file

from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("sample.html"), features="lxml")

final_link = soup.p.a
final_link.decompose()

f = csv.writer(open("sample.csv", "w"))
f.writerow(["Name", "Link"])    # Write column headers as the first line

links = soup.find_all('a')
for link in links:
    names = link.contents[0]
    fullLink = link.get('href')

    f.writerow([names,fullLink])
