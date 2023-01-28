with open('Day4.txt') as data:
	assignments = data.readlines()


class Assignments:
	def __init__(self,data):
		self.overlapping_at_all_pairs_counter = 0
		self.overlapping = 0
		for pairs in assignments:
			person1, person2 = pairs.split(',')
			p1_start, p1_end = person1.split('-')
			p2_start, p2_end = person2.split('-')
			p1_start = int(p1_start)
			p2_start = int(p2_start)
			p1_end = int(p1_end)
			p2_end = int(p2_end)
			if p1_start in range(p2_start,p2_end+1) and p1_end in range(p2_start,p2_end+1) or p2_start in range(p1_start,p1_end+1) and p2_end in range(p1_start,p1_end+1):
				self.overlapping_at_all_pairs_counter += 1
			if p1_start in range(p2_start,p2_end+1) or p1_end in range(p2_start,p2_end+1) or p2_start in range(p1_start,p1_end+1) or p2_end in range(p1_start,p1_end+1):
				self.overlapping += 1
	def print_at_all_overlapping_counter(self):
		print(self.overlapping_at_all_pairs_counter)
	def print_overlapping_counter(self):
		print(self.overlapping)


assignment_list_one = Assignments(assignments)
assignment_list_one.print_at_all_overlapping_counter()
assignment_list_one.print_overlapping_counter()