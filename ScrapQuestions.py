from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
QuesitonAndOptions={} #{"question":{"option1","option2","option3","optin4}}
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeXCQSemX_8SCeMm6aqL-9KdotN22oDkeKKJ0RnLilCia9ofg/viewform")

content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

allQuestionsDiv=soup.findAll('div', attrs={'class':'freebirdFormviewerComponentsQuestionBaseRoot'})


for questionDiv in allQuestionsDiv:
	question=questionDiv.find('div',attrs={'class':'freebirdFormviewerComponentsQuestionBaseTitle'})
	optionsSpan=questionDiv.findAll('span',attrs={'class':'docssharedWizToggleLabeledLabelText'})
	options = [i.text  for i in optionsSpan]
	QuesitonAndOptions[question.text]=options
print(QuesitonAndOptions)