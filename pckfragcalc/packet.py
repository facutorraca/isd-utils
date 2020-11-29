import config 

class Packet:
	def __init__(self, payloadsize, fragoffset, morefrags, pckcode):
		self.pckcode = pckcode
		self.morefrags = morefrags
		self.fragoffset = fragoffset
		self.payloadsize = payloadsize

	def total_length(self):
		return self.payloadsize + config.IPHEADERSIZE

	def to_string(self):
		print('#------------------------#')
		print(f'PACKET: {self.pckcode}')
		print(f'TOTALLENGTH: {config.IPHEADERSIZE + self.payloadsize}')
		print(f'PAYLOAD: {self.payloadsize}')
		print(f'FRAGOFFSET: {self.fragoffset}')
		print(f'MOREFRAGS: {self.morefrags}')
		print('#------------------------#')