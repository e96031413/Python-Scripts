import requests
import random
from bs4 import BeautifulSoup

page = random.randint(1,636)
page = str(page)
print('The Page is:',page+'\n')
resp = requests.get('http://wod-gen.com/exercise/'+page)
soup = BeautifulSoup(resp.text, 'html.parser')
name=soup.find_all('h2')[0].get_text()
print(name)

try:
	time=soup.find_all('h2')[1].get_text()
	print(time)
except:
	pass

workout=soup.find_all('ul')[0].get_text()
print(workout)

#with open('TodaysWorkout.txt','w') as f:
	#for exercise in workout:
		#f.write(workout)
try:
	description=soup.find_all('h3')[0].get_text()
	print(description)

	#with open('TodaysWorkout.txt','w') as f:
		#for detail in description:
			#f.write(detail)
except:
	pass

with open('TodaysWorkout.txt','w') as f:
	try:
		f.write(name+'\n')
		f.write(time+'\n')
		f.write(workout+'\n')
		f.write(description+'\n')
	except:
		pass