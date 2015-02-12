# reading data from the files and processing them
from googleAPI import get_long_lat


def get_no_award(award_header):
	empty_award = {}
	for header in award_header:
		empty_award[header] = ''
	return empty_award


def add_location(key, location):
	if location:
		return {key: get_long_lat(location)}
	else:
		return {key: ''}


# processing the data from file to finalize
def process(contract_rows, award_rows, award_header):
	print "processing the data and getting the result....."
	final_contracts = []
	empty_award = get_no_award(award_header)
	for contract_row in contract_rows:
		row = False
		for award_row in award_rows:
			location = award_row.get('awardeeLocation', '')
			if contract_row['contractName'] == award_row['contractName']:
				if location:
					loc_dic = add_location('latLon', location)
				else:
					loc_dic = add_location('latLon', '')
				final_contracts.append(dict(contract_row.items() + award_row.items() + loc_dic.items() ))
				row = True
				break
		if not row:
			loc_dic = add_location('latLon', '')
			final_contracts.append(dict(contract_row.items() + empty_award.items() + loc_dic.items() ))
	return final_contracts


# get total amount
def get_total_amount(final_contracts):
	total_amount = 0
	for item in final_contracts:
		status = item.get('status', '')
		amount = item.get('amount', '')
		if status == 'Closed' and amount:
			total_amount += int(amount)
	return total_amount				



