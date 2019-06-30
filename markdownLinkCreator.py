
from bs4 import *
import requests
import sys

# scholarship ( at ) 7binaryoptions . com ,https://bbpa.org/national-scholarships/


def createLink(title, url):
    linkTemplate = "- [{}]({})"
    return linkTemplate.format(title, url)


def bookmarkParser(htmlFile):
    with open(htmlFile) as fp:
        return BeautifulSoup(fp, "html.parser")


def createLinkFromHtml(file):
    try:
        soup = bookmarkParser(file)
        listOfMDLinks = list()
        for link in soup.find_all('a'):
            mdLink = createLink(link.string, link.get('href'))
            print(mdLink)
            listOfMDLinks.append(mdLink)

        return listOfMDLinks
    except Exception as e:
        print("Unexpected error:", e)


def sortLinks(links, categories):
    categoriesList = {category: list() for category in categories}
    for link in links:
        for category in categories:
            if category.lower() in link.lower():
                print("This MD link:{} was found to belong in this category:{}".format(
                    link, category))
                categoriesList.get(category).append(link)
    tuples = categoriesList.items()
    return (tuples)


def fromListTupleToMD(listTuple, mdFile):
    with open(mdFile, "at") as mdFile:
        for tp in listTuple:
            mdFile.write("## {}".format(tp[0]))
            mdFile.write("\n")
            for line in tp[1]:
                mdFile.write(line)
                mdFile.write("\n")


def main():
    tags = createLinkFromHtml(
        "/home/darren/Documents/bookmarks/bookmarks_28_06_2019.html")
    topics = ["python", "AI", "ML", "Artificial Intelligence", "Reinforcement Learning", "Khan Academy", "Brilliant"
              "Analytics", "Algorithms", "MIT", "Git", "Data Science", "Learning Path", "Http", "Athabasca University", "java", "Neural Network"]
    sortedL = sortLinks(tags, topics)
    print(sortLinks)
    print(type(sortedL))
    fromListTupleToMD(sortedL, "Test.md")


if __name__ == '__main__':
    main()
