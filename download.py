import os
import urllib2

url_contracts = "https://raw.githubusercontent.com/younginnovations/problem-statements/master/clean-up-contracts-data-xml/contracts.csv"
url_awards = "https://raw.githubusercontent.com/younginnovations/problem-statements/master/clean-up-contracts-data-xml/awards.csv"

directory = os.getcwd()


def check_files(file_contracts, file_awards):
	# create a folder named 'files' if does not exist
	if not os.path.isdir('files'):
		os.system('mkdir files')

	# download files if not exist in the file directory
	if not os.path.exists(file_contracts):
		download_files(url_contracts, file_contracts)
	if not os.path.exists(file_awards):
		download_files(url_awards, file_awards)


# download the file form the given url
def download_files(url, filename):
	print "downloading file {} from git......".format(filename)
	r = urllib2.urlopen(url)
	f = open(filename, 'w')
	f.write(r.read())

