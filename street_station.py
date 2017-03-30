import csv

with open('moscow_trans_stops.csv', 'r', encoding='utf-8') as f:
	fields = ['Name_station', 'Street', 'AdmArea', 'District', 'RouteNumbers', 'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'geoData', 'global_id']
	reader = csv.DictReader(f, fields, delimiter=';')
	#создадим словарь: улица - кол-во остановок
	dict_street = {}
	#максимальное кол-во остановок
	max_station_street = 0
	max_station_street_name = ''
	#смотрим построчно
	for row in reader:
		dict_street.setdefault(row['Street'], 0)
		#если улица есть в словаре, то увеличваем счетчик остановок на 1
		dict_street[row['Street']] += 1
	for x in dict_street:
	#	print( 'Улица: ' + x + ' ' + 'Количество остановок: ' +  str(dict_street[x]))
		#ищем улицу с макс. кол-вом остановок
		if dict_street[x] > max_station_street:
			max_station_street_name = x
			max_station_street = dict_street[x]

	print( 'Улица с макс. кол-вом остановок: ' + max_station_street_name + ' ' + 'Количество остановок: ' +  str(max_station_street))	

