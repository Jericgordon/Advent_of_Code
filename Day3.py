with open('Day3.txt') as data:
	sacks = data.readlines()



def create_key():
	alphabet_lower = list(map(chr,range(97,123)))
	alphabet_upper_and_lower =[]
	dictionary_values = {}

	for x in alphabet_lower:
		alphabet_upper_and_lower.append(x)
	for x in alphabet_lower:
		alphabet_upper_and_lower.append(x.upper())
	for x in range(len(alphabet_upper_and_lower)):
		dictionary_values[alphabet_upper_and_lower[x]] = x + 1

	return dictionary_values



class PackCounter:
	def __init__(self,list):
		self.priority_points = 0
		for string in sacks:
			firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
			print(firstpart,secondpart)
			for letter in firstpart:
				if letter in secondpart:
					self.priority_points += key[letter]
					break
	def print_points(self):
		print(self.priority_points)

class BadgeCounters:
	def __init__(self,list):
		self.priority_points = 0
		for group_number in range(len(sacks)//3):
			group1 = sacks[group_number * 3]
			group2 = sacks[(group_number * 3 + 1)]
			group3 = sacks[(group_number * 3 + 2)]
			
			for letter in group1:
				if letter in group2 and letter in group3:

					self.priority_points += key[letter]
					break
	def print_points(self):
		print(self.priority_points)

key = create_key()

#sack1 = PackCounter(sacks)
#sack1.print_points()

sack2 = BadgeCounters(sacks)
sack2.print_points()

