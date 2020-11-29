import utils

class Route:
	def __init__(self, ip, mask, outputport):
		self.ip = ip
		self.mask = mask
		self.outputport = outputport
		self._binip = utils.ip_to_bin(ip) 

	def subnet(self):
		return f'{self.ip}/{self.mask}'

	def bin_prefix(self):
		return self._binip[0:self.mask]

	def to_string(self):
		print(f'Subnet: {self.subnet()} | Prefix: {self.bin_prefix()} | OutputPort: {self.outputport}', end='')

	def prefix_match(self, ip):
		binip = utils.ip_to_bin(ip)
		return binip[0:self.mask] == self._binip[0:self.mask]