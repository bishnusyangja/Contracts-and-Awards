from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.dom import minidom


def prettify(elem):
	rough_string = ElementTree.tostring(elem)
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml()


def write_xml(filename, element):
	output_file = open( filename, 'w' )
	if isinstance(element, list):
		output_file.write(prettify_multiple(element))
	else:
		output_file.write(prettify(element))
	output_file.close()


# format_xml('contracts',  'contract', final_contracts)
def format_xml(root, elem, item_list):
	root = Element(root)
	for item in item_list:
		sub_elem = SubElement(root, elem)
		for key, value in item.items():
			if not value:
				value = '---'
			SubElement(sub_elem, key).text = value
	return root

