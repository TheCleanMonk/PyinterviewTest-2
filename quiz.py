import re, selenium,os,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#Question 1
def getIndividualNumbersFromInteger(integerInput):
    input = str(integerInput)
    for item in input:
        print(item)
getIndividualNumbersFromInteger(2342)

#Question 2
def longestWord(input):
    newList = list(filter(None, re.split("[, ;'\-!?:]+", input)))
    print(newList)

userInput = "Emoticons, irregular spellings and exclamation points in text messages aren't sloppy or a sign that written language is going down the tubes—these 'textisms' help convey meaning and intent in the absence of spoken conversation, according to newly published research from Binghamton University, State University of New York."
longestWord(userInput)
if 1 == 1:
    print("eat shit")

#Question 3
def setup():
    driver = webdriver.Chrome("C:/cygwin64/home/Zach Hitchens/pySeleniumTest/chromedriver.exe",port=4444)
    driver.get("http://www.xkcd.org")
    return driver
def seleniumTest():
    driver = setup()
    python_link = driver.find_elements_by_xpath("//*[@id='middleContainer']/ul[1]/li[2]/a")[0]
    archive_link = "/html/body/div[1]/div[1]/ul/li[1]/a"
    thirdArchivedComic = "/html/body/div[2]/a[3]"
    python_link.click()
    time.sleep(5)
    python_link.click()
    time.sleep(5)
    pageTitle = driver.title
    archive_link.click()
    time.sleep(5)
    thirdArchivedComicText = thirdArchivedComic.text
    assert (pageTitle == thirdArchivedComicText, "the titles don't match") 
    return "test is over"
    
seleniumTest()