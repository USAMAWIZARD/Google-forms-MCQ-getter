
from bs4 import BeautifulSoup
import  sys
import requests
import json
QuesitonAndOptions={} #{"question":{"option1","option2","option3","optin4}}

page =requests.get(sys.argv[1])
content = page.content
soup = BeautifulSoup(content,"html.parser")

allQuestionsDiv=soup.findAll('div', attrs={'class':'freebirdFormviewerComponentsQuestionBaseRoot'})


for questionDiv in allQuestionsDiv:
	question=questionDiv.find('div',attrs={'class':'freebirdFormviewerComponentsQuestionBaseTitle'})
	optionsSpan=questionDiv.findAll('span',attrs={'class':'docssharedWizToggleLabeledLabelText'})
	options = [i.text  for i in optionsSpan]
	QuesitonAndOptions[question.text]=options
sys.stdout.write(json.dumps(QuesitonAndOptions))
