class Link:
	def __init__(self, length, propation_speed, serialization_speed):
		self.length = length # km
		self.propation_speed = propation_speed # km/s
		self.serialization_speed = serialization_speed # Mbps

	def send_bytes(self, n):
		nbits = n * 8

		t_serialization = (n * 8) / (self.serialization_speed * 1_000_000)
		t_propagation = self.length / self.propation_speed

		# sec to ms
		return (t_serialization + t_propagation) * 1_000

