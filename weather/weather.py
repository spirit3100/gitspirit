class Weather:
	__k = [range(23), range(23, 68), range(68, 113), range(113, 156),
		   range(156, 203), range(203, 248), range(248, 293),
		   range(293, 338), range(338, 361)]
	__string = ['\nтемпература: ','скорость ветра: ','направление ветра: ',
				'влажность воздуха: ',
			    'состояние неба: ']
	__ci = [' C`',' м/с','',' %','']
	__win = ('Север','Северо-Восток','Восток', 'Юго-Восток',
			 'Юг', 'Юго-Запад', 'Запад', 'Северо-Запад', 'Север')
	def __init__(self, w):
		self.__detailed_status = w.detailed_status
		self.__wind_s = w.wind()['speed']
		self.__humidity = w.humidity
		self.__temp = w.temperature('celsius')
		self.__rain = w.rain
		self.__clouds = w.clouds
		self.__wind_d = self.wind_deg(w.wind()['deg'])
		self.q = w.wind()['deg']

	def set(self):
		data = []
		st = ''
		data.append(self.__temp['temp'])
		data.append(str(self.__wind_s))
		data.append(self.__wind_d)
		data.append(self.__humidity)
		data.append(self.__detailed_status)
		for x in range(len(self.__string)):
			st += (self.__string[x] + str(data[x]) + self.__ci[x] + '\n')
		return st

	def wind_deg(self, deg):
		w = ''
		count = 0
		for val in self.__k:
			for y in val:
				if deg == y:
					w = self.__win[count]
			count += 1
		return w
