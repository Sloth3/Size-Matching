import csv

highest_true = int(0)


with open('weightage.txt') as weightage_file, open('final.csv', mode='w') as final_file:
	weightage_reader = csv.reader(weightage_file, delimiter=',')


	for weightage_row in weightage_reader:
		chest_weightage = float(weightage_row[0])
		waist_weightage = float(weightage_row[1])
		hip_weightage = float(weightage_row[2])
		#print(weightage_row[0],weightage_row[1],weightage_row[2])
		true = int(0)
		with open('size.txt') as size_file:
			size_reader = csv.reader(size_file, delimiter=',')
			for size_row in size_reader:

				chest_size = float(size_row[0])
				waist_size = float(size_row[1])
				hip_size = float(size_row[2])

				#print(chest_size)

				if chest_size < 98.5:
					chest_size = 1
				elif chest_size < 103.5:
					chest_size = 2
				elif chest_size < 108.5:
					chest_size = 3
				elif chest_size < 113.5:
					chest_size = 4
				elif chest_size < 118.5:
					chest_size = 5
				elif chest_size < 123.5:
					chest_size = 6
				elif chest_size < 128.5:
					chest_size = 7
				elif chest_size < 133.5:
					chest_size = 8
				elif chest_size < 138.5:
					chest_size = 9
				else:
					chest_size = 10

				#print(waist_size)

				if waist_size < 91.1:
					waist_size = 1
				elif waist_size < 96.1:
					waist_size = 2
				elif waist_size < 101.1:
					waist_size = 3
				elif waist_size < 106.1:
					waist_size = 4
				elif waist_size < 111.1:
					waist_size = 5
				elif waist_size < 116.1:
					waist_size = 6
				elif waist_size < 121.1:
					waist_size = 7
				elif waist_size < 126.1:
					waist_size = 8
				elif waist_size < 131.1:
					waist_size = 9
				else:
					waist_size = 10

				#print(hip_size)

				if hip_size < 95.5:
					hip_size = 1
				elif hip_size < 100.5:
					hip_size = 2
				elif hip_size < 105.5:
					hip_size = 3
				elif hip_size < 110.5:
					hip_size = 4
				elif hip_size < 115.5:
					hip_size = 5
				elif hip_size < 120.5:
					hip_size = 6
				elif hip_size < 125.5:
					hip_size = 7
				elif hip_size < 130.5:
					hip_size = 8
				elif hip_size < 135.5:
					hip_size = 9
				else:
					hip_size = 10

				#print(chest_size, waist_size, hip_size)

				chest_final = chest_size * (chest_weightage/100)
				waist_final = waist_size * (waist_weightage/100)
				hip_final = hip_size * (hip_weightage/100)
				final = chest_final + waist_final + hip_final
			
				if round(final) == int(size_row[3]):
					true += 1

		percent = float(true)/24		
		final123 = (chest_weightage/100,waist_weightage/100,hip_weightage/100, percent)
  		final_writer = csv.writer(final_file)
  		final_writer.writerow(final123)

		if (true > highest_true):
			highest_true = true
			percent = float(true)/24
			print(chest_weightage/100,waist_weightage/100,hip_weightage/100, true, percent)


print(highest_true)



