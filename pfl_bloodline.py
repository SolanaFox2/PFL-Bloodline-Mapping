from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from graphviz import Digraph
from PIL import Image
import urllib.request 
import time
import re
import os


def try_xpath(xpath):
	try:
		driver.find_element(By.XPATH, xpath).text
	except NoSuchElementException:
		out = 'N/A'
	else:
		out = driver.find_element(By.XPATH, xpath).text
		# if out == 'View on Solscan':
	return out

def try_rank(xpath):
	try:
		driver.find_element(By.XPATH, xpath).get_attribute('src')
	except NoSuchElementException:
		out = 'N/A'
	else:
		img = driver.find_element(By.XPATH, xpath).get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-19:-11]))
		out = str(img[-19:-11])
	return out


print('Enter Stable ID: ')

stable_ID = input()


options = Options()
options.add_argument('--headless=new')


driver = webdriver.Chrome(options = options)

driver.get('https://photofinish.live/stable/' + stable_ID)

time.sleep(3)

body = driver.find_element(By.CSS_SELECTOR, 'body')
body.click()
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)



horse_links = []

horses = driver.find_elements(By.XPATH, '//a[@href]')
for horse in horses:
	if 'horses' in horse.get_attribute('href'):
		#print(horse.get_attribute('href'))
		horse_links.append(horse.get_attribute('href'))

if len(horse_links) > 15:
	rstep = 6
else:
	rstep = 4

print(str(len(horse_links)) + ' Bloodlines found in stable')

dot = Digraph(strict = True)
dot.attr(rankdir = 'LR', ranksep = str(rstep))
#dot.attr(ranksep = str(rstep))
counter = 1


for horse_link in horse_links:
	driver.get(horse_link)



	time.sleep(1)

	bloodline = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[1]/ul/div[1]/div/li[4]')
	bloodline.click()
	time.sleep(1)

	family = []
	horse_rank = []

	name = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/div[2]/main/div[3]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/h3/div/div/div[1]/div[2]/span').text
	family.append(name)
	

	img = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/div[2]/main/div[3]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/h3/div/div/div[1]/div[1]/div/img').get_attribute('src')
	urllib.request.urlretrieve(img, str(img[-19:-11]))
	horse_rank.append(str(img[-19:-11]))
	

	body = driver.find_element(By.CSS_SELECTOR, 'body')
	body.click()
	body.send_keys(Keys.PAGE_DOWN)

	dad = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/p')
	if dad == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/img')
		horse_rank.append(img)
		family.append(dad)



	dads_dad = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/p')
	if dads_dad == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/img')
		horse_rank.append(img)
		family.append(dads_dad)

	dads_mom = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/p')
	if dads_mom == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/img')
		horse_rank.append(img)
		family.append(dads_mom)


	dads_grandpa1 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/p')
	if dads_grandpa1 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/img')
		horse_rank.append(img)
		family.append(dads_grandpa1)

	dads_grandma1 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/p')
	if dads_grandma1 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/img')
		horse_rank.append(img)
		family.append(dads_grandma1)


	dads_grandpa2 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/p')
	if dads_grandpa2 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/img')
		horse_rank.append(img)
		family.append(dads_grandpa2)


	dads_grandma2 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/p')
	if dads_grandma2 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/img')
		horse_rank.append(img)
		family.append(dads_grandma2)

	mom = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[1]/div/div[1]/p')
	if mom == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[1]/div/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[1]/div/div[1]/div/img')
		horse_rank.append(img)
		family.append(mom)

	moms_dad = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[1]/div/div/div[1]/p')
	if moms_dad == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[1]/div/div/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[1]/div/div/div[1]/div/img')
		horse_rank.append(img)
		family.append(moms_dad)

	moms_mom = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[1]/div/div/div[1]/p')
	if moms_mom == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[1]/div/div/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[1]/div/div/div[1]/div/img')
		horse_rank.append(img)
		family.append(moms_mom)


	moms_grandpa1 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/p')
	if moms_grandpa1 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/img')
		horse_rank.append(img)
		family.append(moms_grandpa1)


	moms_grandma1 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/p')
	if moms_grandma1 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[2]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/img')
		horse_rank.append(img)
		family.append(moms_grandma1)


	moms_grandpa2 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[1]/p')
	if moms_grandpa2 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[1]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/img')
		horse_rank.append(img)
		family.append(moms_grandpa2)


	moms_grandma2 = try_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[2]/div[1]/p')
	if moms_grandma2 == 'View on Solscan':
		img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[2]/img').get_attribute('src')
		urllib.request.urlretrieve(img, str(img[-9:]))
		family.append(str(img[-9:]))
		horse_rank.append('N/A')
	else:
		img = try_rank('/html/body/div[1]/div[1]/div/div[2]/div[2]/main/div[3]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/img')
		horse_rank.append(img)
		family.append(moms_grandma2)



	rank_count = 0

	for member in family:
		if 'jpg' in member:
			dot.node(name = member, label = '', shape = 'none', image=member)
		elif "N/A" in member:
			bool = False
		else:
			dot.node(name = member, label = member, fontsize = "40", shape = 'egg', height = '3', labelloc = 'b', imagepos = 'tc', image = horse_rank[rank_count])

		rank_count = rank_count + 1

	if family[1] != 'N/A':
		dot.edge(family[1],family[0], color = 'blue')
		dot.edge(family[8],family[0], color = 'red')
	if family[2] != 'N/A':
		dot.edge(family[2],family[1], color = 'blue')
		dot.edge(family[3],family[1], color = 'red')
	if family[4] != 'N/A':
		dot.edge(family[4],family[2], color = 'blue')
		dot.edge(family[5],family[2], color = 'red')
	if family[6] != 'N/A':
		dot.edge(family[6],family[3], color = 'blue')
		dot.edge(family[7],family[3], color = 'red')
	if family[9] != 'N/A':
		dot.edge(family[9],family[8], color = 'blue')
		dot.edge(family[10],family[8], color = 'red')
	if family[11] != 'N/A':
		dot.edge(family[11],family[9], color = 'blue')
		dot.edge(family[12],family[9], color = 'red')
	if family[13] != 'N/A':
		dot.edge(family[13],family[10], color = 'blue')
		dot.edge(family[14],family[10], color = 'red')


	print(str(counter) + ' of Bloodlines ' + str(len(horse_links)) + ' documented')

	counter = counter + 1


dot.render('PFL_Bloodline', view=True)


current_direct = os.getcwd()
for file in os.listdir(current_direct):
	if file.endswith('.jpg') or file.endswith('.png'):
		os.remove(file) 




















