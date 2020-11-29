import utils
from route import Route

class RoutingTable:
	def __init__(self):
		self.routes = []

	def add_route(self, route):
		self.routes.append(route)

	def to_string(self):
		print('#-----------Subnets----------#')
		for route in self.routes:
			route.to_string()
		print('')
		print('#----------------------------#')

	def route_ip(self, ip):
		binip =	 utils.ip_to_bin(ip)

		lpm = None
		longest_mask = 0

		for route in self.routes:
			if route.prefix_match(ip):
				if longest_mask < route.mask:
					lpm = route
					longest_mask = route.mask

		return lpm