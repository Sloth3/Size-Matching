import csv

highest_true = int(0)


with open('weightage2.txt') as weightage_file, open('final.csv', mode='w') as final_file:
	weightage_reader = csv.reader(weightage_file, delimiter=',')


	for weightage_row in weightage_reader:
		waist_body_weightage = float(weightage_row[0])
		hip_body_weightage = float(weightage_row[1])
		true = int(0)
		with open('size.txt') as size_file:
			size_reader = csv.reader(size_file, delimiter=',')
			for size_row in size_reader:

				waist_body_size = float(size_row[0])
				hip_body_size = float(size_row[1])
				# leg_body_size = float(size_row[2])
				height = float(size_row[2])
				height_size = 'nothing'

				if height < 177.5:
					height_size = 'S'
					if waist_body_size < 85.5:
						waist_body_size = 1
					elif waist_body_size < 90.5:
						waist_body_size = 2
					elif waist_body_size < 95.5:
						waist_body_size = 3
					elif waist_body_size < 100.5:
						waist_body_size = 4
					elif waist_body_size < 105.5:
						waist_body_size = 5
					elif waist_body_size < 110.5:
						waist_body_size = 6
					elif waist_body_size < 115.5:
						waist_body_size = 7
					elif waist_body_size < 120.5:
						waist_body_size = 8
					elif waist_body_size < 125.5:
						waist_body_size = 9
					else:
						waist_body_size = 10


					if hip_body_size  < 102.5:
						hip_body_size  = 1
					elif hip_body_size  < 107.5:
						hip_body_size  = 2
					elif hip_body_size  < 112.5:
						hip_body_size  = 3
					elif hip_body_size  < 117.5:
						hip_body_size  = 4
					elif hip_body_size  < 122.5:
						hip_body_size  = 5
					elif hip_body_size  < 127.5:
						hip_body_size  = 6
					elif hip_body_size  < 132.5:
						hip_body_size  = 7
					elif hip_body_size  < 137.5:
						hip_body_size  = 8
					elif hip_body_size  < 142.5:
						hip_body_size  = 9
					else:
						hip_body_size  = 10

					# if leg_body_size  < 76.25:
					# 	leg_body_size  = 1
					# elif leg_body_size  < 76.75:
					# 	leg_body_size  = 2
					# elif leg_body_size  < 77.25:
					# 	leg_body_size  = 3
					# elif leg_body_size  < 77.75:
					# 	leg_body_size  = 4
					# elif leg_body_size  < 78.25:
					# 	leg_body_size  = 5
					# elif leg_body_size  < 78.75:
					# 	leg_body_size  = 6
					# elif leg_body_size  < 79.25:
					# 	leg_body_size  = 7
					# elif leg_body_size  < 79.75:
					# 	leg_body_size  = 8
					# elif leg_body_size  < 80.25:
					# 	leg_body_size  = 9
					# else:
					# 	leg_body_size  = 10

				elif height > 182.5:
					height_size = 'R'
					if waist_body_size < 75.5:
						waist_body_size = 1
					elif waist_body_size < 80.5:
						waist_body_size = 2
					elif waist_body_size < 85.5:
						waist_body_size = 3
					elif waist_body_size < 90.5:
						waist_body_size = 4
					elif waist_body_size < 95.5:
						waist_body_size = 5
					elif waist_body_size < 100.5:
						waist_body_size = 6
					elif waist_body_size < 105.5:
						waist_body_size = 7
					elif waist_body_size < 110.5:
						waist_body_size = 8
					elif waist_body_size < 115.5:
						waist_body_size = 9
					else:
						waist_body_size = 10


					if hip_body_size  < 92.5:
						hip_body_size  = 1
					elif hip_body_size  < 97.5:
						hip_body_size  = 2
					elif hip_body_size  < 102.5:
						hip_body_size  = 3
					elif hip_body_size  < 107.5:
						hip_body_size  = 4
					elif hip_body_size < 112.5:
						hip_body_size  = 5
					elif hip_body_size  < 117.5:
						hip_body_size = 6
					elif hip_body_size < 122.5:
						hip_body_size  = 7
					elif hip_body_size  < 127.5:
						hip_body_size  = 8
					elif hip_body_size  < 132.5:
						hip_body_size  = 9
					else:
						hip_body_size  = 10

					# if leg_body_size  < 79.25:
					# 	leg_body_size  = 1
					# elif leg_body_size  < 79.75:
					# 	leg_body_size  = 2
					# elif leg_body_size  < 80.25:
					# 	leg_body_size  = 3
					# elif leg_body_size  < 80.75:
					# 	leg_body_size  = 4
					# elif hip_body_size  < 81.25:
					# 	leg_body_size  = 5
					# elif leg_body_size  < 81.75:
					# 	leg_body_size  = 6
					# elif leg_body_size  < 82.25:
					# 	leg_body_size  = 7
					# elif leg_body_size  < 82.75:
					# 	leg_body_size  = 8
					# elif leg_body_size  < 83.25:
					# 	leg_body_size  = 9
					# else:
					# 	leg_body_size = 10

				else:
					height_size = 'L'
					if waist_body_size < 75.5:
						waist_body_size = 1
					elif waist_body_size < 80.5:
						waist_body_size = 2
					elif waist_body_size < 85.5:
						waist_body_size = 3
					elif waist_body_size < 90.5:
						waist_body_size = 4
					elif waist_body_size < 95.5:
						waist_body_size = 5
					elif waist_body_size < 100.5:
						waist_body_size = 6
					else:
						waist_body_size = 7

					if hip_body_size  < 92.5:
						hip_body_size  = 1
					elif hip_body_size  < 97.5:
						hip_body_size  = 2
					elif hip_body_size  < 102.5:
						hip_body_size  = 3
					elif hip_body_size  < 107.5:
						hip_body_size  = 4
					elif hip_body_size < 112.5:
						hip_body_size  = 5
					elif hip_body_size  < 117.5:
						hip_body_size = 6
					else:
						hip_body_size  = 7


					# if leg_body_size  < 84.25:
					# 	leg_body_size  = 1
					# elif leg_body_size  < 84.75:
					# 	leg_body_size  = 2
					# elif leg_body_size  < 85.25:
					# 	leg_body_size  = 3
					# elif leg_body_size  < 85.75:
					# 	leg_body_size  = 4
					# elif hip_body_size  < 86.25:
					# 	leg_body_size  = 5
					# elif leg_body_size  < 86.75:
					# 	leg_body_size  = 6
					# else:
					# 	leg_body_size = 7


				#calculation to find the predicted size 
				waist_body_final = waist_body_size * (waist_body_weightage/100)
				hip_body_final = hip_body_size * (hip_body_weightage/100)
				# leg_body_final = leg_body_size * (leg_weightage/100)
				final = waist_body_final + hip_body_final #+ hip_final
			
				#comapare predicted size with taken size
				if round(final) == int(size_row[3]):
					true += 1

		#write into "final.csv" results
		percent = float(true)/24#change this number according to how many data you have		
		# final123 = (waist_body_weightage/100,hip_body_weightage/100,leg_body_weightage/100, percent)
		final123 = (waist_body_weightage/100,hip_body_weightage/100, percent)
		final_writer = csv.writer(final_file)
		final_writer.writerow(final123)


  		#prints when each highest match is found with their weightage
		if (true > highest_true):
			highest_true = true
			percent = float(true)/24#change this number according to how many data you have	
			# print(waist_body_weightage/100,hip_body_weightage/100,leg_body_weightage/100, true, percent)
			print(waist_body_weightage/100,hip_body_weightage/100, true, percent)

#prints the highest percentage match
print(highest_true)



