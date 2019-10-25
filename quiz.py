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

#Question 3

sleepTime = 8
def setup():
    #had issue getting this path to to work, you may have trouble as well
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://www.xkcd.org")
    return driver
def exit():
    driver.close()
    return driver
def seleniumTest():
    driver = setup()
    backBtn = driver.find_elements_by_xpath("//*[@id='middleContainer']/ul[1]/li[2]/a")[0]
    archive_link = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/ul/li[1]/a")[0]
    thirdArchivedComic = driver.find_elements_by_xpath("/html/body/div[2]/a[3]")[0]
    backBtn.click()
    time.sleep(sleepTime)
    backBtn.click()
    time.sleep(sleepTime)
    pageTitleOfThirdComic = driver.title
    backBtn.click()
    time.sleep(sleepTime)
    thirdArchivedComicText = thirdArchivedComic.text
    assert (pageTitleOfThirdComic == thirdArchivedComicText, "the titles don't match") 
    exit(driver)
    return "Test Passed and closed without issue"
def exit(driver):
    driver.close()
    return driver
    
seleniumTest()