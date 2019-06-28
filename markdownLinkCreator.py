
from bs4 import *
import requests 
import sys

def createLink(title,url):
    linkTemplate="- [{}]({})"
    return linkTemplate.format(title,url)

def bookmarkParser(htmlFile):
    with open(htmlFile) as fp:
       return BeautifulSoup(fp, "html.parser")

def createLinkFromHtml(file):
    try:
        soup = bookmarkParser(file)
        listOfMDLinks=list()
        for link in soup.find_all('a'):
            mdLink= createLink(link.string,link.get('href'))
            print(mdLink)
            listOfMDLinks.append(mdLink)

        return listOfMDLinks    
    except Exception as e :
        print("Unexpected error:",e)


def sortLinks(links,categories):
    categoriesList={category:list() for category in categories}
    for link in links:
        for category in categories:
            if category.lower() in link.lower():
                print("This MD link:{} was found to belong in this category:{}".format(link,category))
                categoriesList.get(category).append(link)
    tuples =categoriesList.items()
    return (tuples)

def fromListTupleToMD(listTuple,mdFile):
    with open(mdFile,"at") as mdFile:
        for tp in listTuple:
            mdFile.write("## {}".format(tp[0]))
            for line in tp[1]:
                mdFile.write(line)
            mdFile.write("\n")

    
def main():
   tags =createLinkFromHtml("/home/darren/Downloads/bookmarks_6_7_19.html")
   sortedLinks=sortLinks(tags,["python"])
   print(sortLinks)
   fromListTupleToMD(sortLinks,"test.md")
   

if __name__ == '__main__':
    main()