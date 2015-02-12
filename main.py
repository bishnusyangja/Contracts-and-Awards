import urllib2
import os

# from settings import API_KEY
from download import check_files
from csvFile import read_file
from xmlFile import format_xml, write_xml
from process import process, get_total_amount

directory = os.getcwd()


file_contracts = directory + '/files/contracts.csv'
file_awards = directory + '/files/awards.csv'


def main():
	outfile = directory + '/files/output_contracts.xml'
	check_files(file_contracts, file_awards)
	contract_header, contract_rows = read_file(file_contracts)
	award_header, award_rows = read_file(file_awards)
	final_contracts = process(contract_rows, award_rows, award_header)
	formatted_contracts = format_xml('contracts',  'contract', final_contracts)
	write_xml(outfile, formatted_contracts)

	print "Total Amount of closed contracts: {}\n".format(get_total_amount(final_contracts))


if __name__ == "__main__":
    main()


