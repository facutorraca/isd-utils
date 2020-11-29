import utils
from route import Route
from routingtable import RoutingTable

SUBNETS_FILENAME = 'subnets.txt'

#---------------------AUXILIARY----------------------#
def _init_routing_table(subnets_file):
	routingtable = RoutingTable()

	lines = subnets_file.readlines()
	for info in lines:
		
		subnet = info.split(',')[0]
		outputport = info.split(',')[1]

		ip = subnet.split('/')[0]
		mask = int(subnet.split('/')[1])

		route = Route(ip, mask, outputport)
		routingtable.add_route(route)

	return routingtable

def _run_interface(rt):
	while True:
		ip = input('ip: ')
		print('bin: ' + utils.ip_to_bin(ip))

		route = rt.route_ip(ip)
		if route != None:
			route.to_string()
		else:
			print('Not Found Route')

		print(' ')
#----------------------------------------------------#


#----------------------MAIN--------------------------#
def main():
	subnets_file = open(SUBNETS_FILENAME)	
	rt = _init_routing_table(subnets_file)

	rt.to_string()
	print('')

	print('#-------------IPs------------#')
	try:
		_run_interface(rt)
	except KeyboardInterrupt:
		print('')
		print('#----------------------------#')
#----------------------------------------------------#


main()