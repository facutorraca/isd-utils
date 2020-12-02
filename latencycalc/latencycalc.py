import argparse as ap
from link import Link

BOLD = '\033[1m'
ENDC = '\033[0m'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
UNDERLINE = '\033[4m'

#---------------------AUXILIARY----------------------#
def _parse_args():
	parser = ap.ArgumentParser()

	parser.add_argument("-l",
						"--links",
						required=True,
						help="Set number of links")

	parser.add_argument("-f",
						"--filesize",
						required=True,
						help="Set the file size")

	return parser.parse_args()


def _create_links(numlinks):
	# number of links = routers + 1

	links = []
	for i in range(numlinks):
		link_length = float(input(f'Link {i} length (km): '))
		propagation_speed = float(input(f'Link {i} propagation speed (km/s): '))
		serialization_speed = float(input(f'Link {i} transfer speed (Mbps): '))
		link = Link(link_length, propagation_speed, serialization_speed)
		links.append(link)
		print('')

	return links
#----------------------------------------------------#


#-----------------------LOGIC------------------------#
def calc_rtt(filesize, links):	
	time = 0
	for link in links:
		time += link.send_bytes(filesize)

	return 2 * time

#----------------------------------------------------#


#----------------------MAIN--------------------------#
def main():
	args = _parse_args()

	numlinks = int(args.links)
	filesize = int(args.filesize)

	links = _create_links(numlinks)
		
	rtt = calc_rtt(filesize, links)

	print(f'{HEADER}{BOLD}Latency: {rtt} ms{ENDC}')
#----------------------------------------------------#

main()
