from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


def get_server(city):
	f = open('key.txt','r')
	text = f.read()
	f.close()
	owm = OWM(text)
	mgr = owm.weather_manager()
	try:
		observation = mgr.weather_at_place(city)
		w = observation.weather
		return w
	except Exception:
		print('Exception')
