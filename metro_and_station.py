import csv
import datetime
from geopy.distance import vincenty

with open('moscow_metro_info.csv', 'r', encoding='utf-8') as f:
	fields = ['Local id', 'Name','longitude WGS84','latitude WGS-84','Station','Line','Mode work even day','Mode work odd day','Quantity fullfunction BPA','Quantity smallfunction BPA','Quantity all BPA','Repair escalator','global_id','Geodata']
	moscow_metro_reader = csv.DictReader(f, fields, delimiter=';')
	#словарь станция - координаты
	dict_metro_geo = {}
	#цикл для создания словаря станция - координаты
	for metro_station in moscow_metro_reader:
		#пропускаем первую строчку
		if metro_station['Station'] == 'Станция метрополитена':
			continue
		metro_name = metro_station['Station']
		metro_geo  = (float(metro_station['longitude WGS84']), float(metro_station['latitude WGS-84']))
		dict_metro_geo[metro_name] = metro_geo
		#print(dict_metro_geo.items())

with open('moscow_trans_stops.csv', 'r', encoding='utf-8') as f:
	fields = ['Name_station', 'Street', 'AdmArea', 'District', 'RouteNumbers', 'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'geoData', 'global_id']
	moscow_trans_reader = csv.DictReader(f, fields, delimiter=';')
	#создадим словарь:  остановка наземная - координаты
	dict_trans_station_geo = {}
	#цикл для создания словаря остановка наземная - координаты
	for trans_station in moscow_trans_reader:
		#пропускаем первую строчку
		if trans_station['Name_station'] == 'Name':
			continue
		trans_name = trans_station['Name_station']
		#trans_geo = (trans_station['geoData'],trans_station['geoData'])
		trans_geo = trans_station['geoData'].replace("\n"," ").replace(",","").split()
		dict_trans_station_geo[trans_name] = (float(trans_geo[6]),float(trans_geo[7]))
		#print(dict_trans_station_geo.items())
		#exit()

#Словарь станция метро - кол-во остановок вблизи 500 м
dict_metro_data = {}
#начинаем считать кол-во остановок в радиусе 500 м
for i in dict_metro_geo:
	dict_metro_data[i] = 0
	for j in dict_trans_station_geo:
		if vincenty(dict_metro_geo[i],dict_trans_station_geo[j]).meters <= 500.0:
			dict_metro_data[i] += 1
	#print(i + ' ' + str(dict_metro_data[i]))
#максимальное кол-во остановок вблизи 500 м
station_max_trans = 0
#станция с макс. кол-вом остановок
station_max_name = ''
#поиск
for x in dict_metro_data:
		#ищем станцию с макс. кол-вом остановок вблизи 500 м
		if dict_metro_data[x] > station_max_trans:
			station_max_name  = x
			station_max_trans = dict_metro_data[x]
print( 'Станция с макс. кол-вом остановок вблизи 500 м: ' + station_max_name + ' ' + 'Количество остановок: ' +  str(station_max_trans))	
