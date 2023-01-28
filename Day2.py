import pandas as pd

df = pd.read_excel('Rps.xlsx')

strategy_data = df['Data'].tolist()

my_throws = []
opponant_throws=[]


for item in strategy_data:

	split_data = item.split(" ")
	opponant_throws.append(split_data[0])
	my_throws.append(split_data[1])

my_throws = list(map(lambda x:x.lower(), my_throws))
opponant_throws = list(map(lambda x: x.lower(), opponant_throws))


match_history = zip(my_throws,opponant_throws)

class Points:
	def __init__(translation_library):
		pass


class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

class LinkedList:
	def __init__(self):
			self.headval = None
	def nextval(self):
		printval = printval.nextval
		print(printval.dataval)
		

list1 = LinkedList()
list1.headval = Node("Scissors")

e2 = Node("Paper")
e3 = Node("Rock")

list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = list1.headval

class PointsCounter:
	def __init__(self,match_history):
		self.my_points = 0
		for throws in match_history:
			my_throw = throws[0]
			#add throw outcomes
			self.my_points += points_library[my_throw]
			opponant_throw = throws[1]
			# Add match point outcomes
			if translation_library[opponant_throw][1] == translation_library[my_throw][0].nextval.dataval:
				self.my_points += 6
			if translation_library[opponant_throw][1] == translation_library[my_throw][1]:
				self.my_points += 3 
			else:
				self.my_points += 0	
	def printpoints(self):
		print(self.my_points)

class PointsCounterNew:
	def __init__(self,match_history):
		self.my_points = 0
		for throws in match_history:
			#add points for match outcome
			self.my_points += points_library_new[throws[0]]
	

			#add throw outcomes
			opponant_throw = throws[1]

			if throws[0] == 'x':
				my_throw = translation_library[opponant_throw][0].nextval.dataval
				self.my_points += points_library[reverse_translation_library[my_throw]]
			if throws[0] == 'y':
				my_throw = translation_library[opponant_throw][0].dataval
				self.my_points += points_library[reverse_translation_library[my_throw]]
			if throws[0] == 'z':
				my_throw = translation_library[opponant_throw][0].nextval.nextval.dataval
				self.my_points += points_library[reverse_translation_library[my_throw]]
	def printpoints(self):
		print(self.my_points)



translation_library = {'x':(e3,'Rock'), 'y':(e2,'Paper'), 'z':(list1.headval,'Scissors'),'a':(e3,'Rock'), 'b':(e2,'Paper'), 'c':(list1.headval,'Scissors')}
reverse_translation_library = {'Rock': 'a','Paper':'b','Scissors':'c'}
points_library = {'a':1, 'b':2, 'c':3}

points_library_new = {'x':0,'y':3,'z':6}



game_one = PointsCounterNew(match_history)
game_one.printpoints()
