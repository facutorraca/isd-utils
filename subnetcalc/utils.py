def dec_to_bin(dec):
	return format(dec,'08b')

def ip_to_bin(decip):
	binip = ''

	ip_octets = decip.split('.')
	for octets in ip_octets:
		binip += dec_to_bin(int(octets))

	return binip