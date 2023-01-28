import pandas as pd
import math


df = pd.read_excel('elf_calories.xls')

#using an pandas to read an excel file rather than a .csv because excel likes excel files.

calories_as_list = df['calories'].tolist()

#pandas naturally saves excell data as a list. While there are some options to convert series to Arrays, it was simpler for the iterative purposes of this to use a list

print("New run")
class Elf_caravan:
	def __init__(self,list):
		self.elves_in_caravan = 0
		self.calories_by_elf = {1:0}
		self.temp_elf_calories = 0
		for snacks in list:
			if math.isnan(snacks) == True:
				self.elves_in_caravan += 1
				self.calories_by_elf[self.elves_in_caravan] = self.temp_elf_calories
				self.temp_elf_calories = 0
			else:
				self.temp_elf_calories += snacks
				
		#We use the __init__() function of classes to automatically process our spreadsheet to create a dictionary of elves, and the different numbers of calories they carry. We don't need individual food items, so automatically processing it, is a good idea.


	def max_value(self):
		elf_number_with_most = max(self.calories_by_elf, key = lambda c: self.calories_by_elf[c])

		#TIL about Lamda functios, and the key funtion of max(). This is a particularly eloquent way to do this. Normally max looks at a data set. In this, case, the data set is the dictionary 'calories_by_elf'. Normally, it would look at the keys of the dictionary, and return the greatest key. This is pretty useless for these purposes. Instead, we've told it, 'Don't look at the keys, look at the dictionary.'

		#See, Max allows us to specify the criteria by which it looks at the max, and allows us to feed it functions, in order to determine the greates of something, so long as those functions return a value. In this case we used an annonomous, or lamda function to quickly feed the keys into the dictionary of calories_by_elf, and return a value. Max() then is comparing, not the value of the keys, but the values to those keys. 

		print(elf_number_with_most)
		print(self.calories_by_elf[elf_number_with_most])


	def running_out_of_food(self,elves_out_of_food,top_elves_number):
		new_elf_dictionary = self.calories_by_elf
		new_top_elf_total = 0
		for elf_number in range(elves_out_of_food + top_elves_number):
			current_max = max(new_elf_dictionary, key = lambda c: self.calories_by_elf[c])
			if elf_number + 1 <= elves_out_of_food:
				x = new_elf_dictionary.pop(current_max)
				print('delete',current_max,new_elf_dictionary)
			else:
				print(new_top_elf_total,new_elf_dictionary[current_max],new_top_elf_total + new_elf_dictionary[current_max])
				new_top_elf_total += new_elf_dictionary[current_max]
				new_elf_dictionary.pop(current_max)
				print('add',current_max,new_elf_dictionary)
				
		print (new_top_elf_total)






#Since the max command returned the value of the elf with the most, we just finish the work in our print commmand, and convert that value into a number

caravan_one = Elf_caravan(calories_as_list)
caravan_one.max_value()
caravan_one.running_out_of_food(0,3)











