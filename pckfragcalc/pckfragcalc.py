import math
import config
import argparse as ap
from link import Link
from packet import Packet

BOLD = '\033[1m'
ENDC = '\033[0m'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
UNDERLINE = '\033[4m'

#---------------------AUXILIARY----------------------#
def _parse_args():
	parser = ap.ArgumentParser()

	parser.add_argument("-r",
						"--routers",
						required=True,
						help="Set number of routers")

	parser.add_argument("-p",
						"--payload",
						required=True,
						help="Payload size")

	return parser.parse_args()


def _create_links(numrouters):
	# number of links = routers + 1

	links = []
	for i in range(numrouters + 1):
		capacity = int(input(f'Link {i} capacity: '))
		link = Link(i, capacity)
		links.append(link)

	return links
#----------------------------------------------------#


#-----------------------LOGIC------------------------#
def send_packet(packets, links, ipheaders, k):	
	if len(links) == k:
		return 
	
	fragpackets = []

	for packet in packets:
		fragpackets += links[k].send_packet(packet)
		
	ipheaders.append((k, fragpackets))
	send_packet(fragpackets, links, ipheaders, k + 1)
#----------------------------------------------------#


#----------------------MAIN--------------------------#
def main():
	args = _parse_args()

	numrouters = int(args.routers)
	payloadsize = int(args.payload)

	links = _create_links(numrouters)
	ipacket = Packet(payloadsize, 0, False, '1')

	# ip headers generated
	ipheaders = []

	send_packet([ipacket], links, ipheaders, 0)

	# sort by order of fragmentatio
	ipheaders.sort(key=lambda x: x[0])

	print(f'{HEADER}{BOLD}Initial Packet: {0}{ENDC}')
	ipacket.to_string()
	print('')

	for k, packets in ipheaders:
		
		print(f'{HEADER}{BOLD}Link: {k + 1}{ENDC}')

		for packet in packets:
			packet.to_string()
			print('')
#----------------------------------------------------#

main()
