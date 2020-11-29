import math
import config
from packet import Packet

class Link:
	def __init__(self, number, capacity):
		self.number = number
		self.capacity = capacity

	def effective_capacity(self):
		capacity_without_header = self.capacity - config.IPHEADERSIZE
		return math.floor(capacity_without_header / 8) * 8

	def send_packet(self, packet):
		fragspackets = []

		parentpckcode = packet.pckcode
		parentfragoffset = packet.fragoffset

		# if original packet is do not fragment,
		# the new fragmets inherites this attribute
		morefrags = packet.morefrags

		if packet.total_length() <= self.capacity:
			return [packet]

		fragcount = math.ceil(packet.payloadsize / self.effective_capacity())
		fragoffset = self.effective_capacity() / 8

		for i in range(fragcount - 1):
			payloadsize = self.effective_capacity() 
			childpckcode = parentpckcode + f'.{i+1}'
			childfragoffset = parentfragoffset + (fragoffset * i)
			fragpacket = Packet(payloadsize, childfragoffset, True, childpckcode)
			fragspackets.append(fragpacket)

		last_frag_payloadsize = packet.payloadsize - (fragcount - 1) * self.effective_capacity()

		if last_frag_payloadsize > 0:
			childpckcode = parentpckcode + f'.{fragcount}'
			childfragoffset = parentfragoffset + ((fragcount - 1) * fragoffset)
			last_fragpacket = Packet(last_frag_payloadsize, childfragoffset, morefrags, childpckcode)
			fragspackets.append(last_fragpacket)

		return fragspackets