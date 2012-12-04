from bs4 import BeautifulSoup

def getpostsforuser(profilesrc):
    soup = BeautifulSoup(open(profilesrc))
    
    tableofinterest = soup.find("td",class_="windowbg").find_all("td")
    print tableofinterest[3].get_text()
    

def main():
    getpostsforuser("/home/mel/Documents/2012-2013/COMM 645/paper/test_forum.html")


if __name__ == "__main__":
    main()
