from bs4 import BeautifulSoup
import requests

def get_tickets(build_num, base_url, branch):
	homepage = base_url + branch

	#scrape the cruise control homepage
	page = requests.get(homepage)
	soup = BeautifulSoup(page.content, 'html.parser')

	#get the link of the target build
	for links in soup.select(".link-success-true"): 
		if build_num in links.get_text():
			link = links["href"]
			break

	target_build_url = base_url + link

	#scrape the target build page
	page = requests.get(target_build_url)
	soup = BeautifulSoup(page.content, 'html.parser')

	#get the list of affected tickets
	tickets = [data.get_text()[:9] for data in soup.select(".modifications-data") if data.get_text().startswith("LSF")]
	#remove duplicates
	tickets = list(set(tickets))

	print(tickets)

#parameters which makes the function flexible
build_num = "1889"
base_url = "http://chiron2.infor.com:7058"
branch = "/buildresults/lsf-REL_10-MASTER"

get_tickets(build_num, base_url, branch)