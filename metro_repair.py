import csv
import datetime

with open('moscow_metro_info.csv', 'r', encoding='utf-8') as f:
	fields = ['Local id', 'Name','longitude WGS84','latitude WGS-84','Station','Line','Mode work even day','Mode work odd day','Quantity fullfunction BPA','Quantity smallfunction BPA','Quantity all BPA','Repair escalator','global_id','Geodata']
	reader = csv.DictReader(f, fields, delimiter=';')
	#список станций в ремонте
	dict_station_repair = []
	#текущая дата
	date_now = datetime.datetime.now()

	#смотрим построчно
	for row in reader:
		#пропускаем первую строчку
		if row['Repair escalator'] == 'Ремонт эскалаторов':
			continue
		if row['Repair escalator']:
			#день окончания ремонта
			day_end_repair   = row['Repair escalator'][-10:-8]
			#месяц окончания ремонта
			month_end_repair = row['Repair escalator'][-7:-5]
			#год окончания ремонта
			year_end_repair  = row['Repair escalator'][-4:]
			#дата окончания ремонта эскалатора
			date_repair_escalator = datetime.datetime(int(year_end_repair),int(month_end_repair),int(day_end_repair))
			#если дата окончания ремонта больше текущей даты, то выводим станцию и дату 
			if date_repair_escalator > date_now:
				print(row['Name'] + '  ' + row['Repair escalator'][-10:])

		


