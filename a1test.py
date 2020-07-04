import unittest
from a1 import get_temperature
from a1 import has_error
from a1 import weather_response
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel

a = weather_response('Delhi', 'e6205c85b5958567349335aeb1cee7df')
# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):

	def test_has_error(self):
		self.assertTrue(has_error('Mumbai',weather_response('Delhi','e6205c85b5958567349335aeb1cee7df')),True)
		self.assertTrue(has_error('Lucknow',weather_response('Lucknow','e6205c85b5958567349335aeb1cee7df')),False)
		self.assertTrue(has_error('Jaipur',weather_response('Jaipur','e6205c85b5958567349335aeb1cee7df')),False)
		self.assertTrue(has_error('Allahabad',weather_response('Allahabad','e6205c85b5958567349335aeb1cee7df')),False)

	def test_get_temperature(self):
		self.assertAlmostEqual(get_temperature(weather_response('Delhi','e6205c85b5958567349335aeb1cee7df'),1,'3:00:00'),299.817,delta=10)
		self.assertAlmostEqual(get_temperature(weather_response('Lucknow','e6205c85b5958567349335aeb1cee7df'),2,'6:00:00'),303.939,delta=10)
		self.assertAlmostEqual(get_temperature(weather_response('Jaipur','e6205c85b5958567349335aeb1cee7df'),3,'9:00:00'),299.419,delta=10)
		self.assertAlmostEqual(get_temperature(weather_response('Allahabad','e6205c85b5958567349335aeb1cee7df'),1,'12:00:00'),302.818,delta=10)	
	def test_get_humidity(self):
		self.assertAlmostEqual(get_humidity(weather_response('Delhi','e6205c85b5958567349335aeb1cee7df'),1,'3:00:00'),88,delta=10)
		self.assertAlmostEqual(get_humidity(weather_response('Lucknow','e6205c85b5958567349335aeb1cee7df'),2,'6:00:00'),90,delta=10)
		self.assertAlmostEqual(get_humidity(weather_response('Jaipur','e6205c85b5958567349335aeb1cee7df'),3,'9:00:00'),86,delta=10)
		self.assertAlmostEqual(get_humidity(weather_response('Allahabad','e6205c85b5958567349335aeb1cee7df'),1,'12:00:00'),80,delta=10)

	def test_get_pressure(self):
		self.assertAlmostEqual(get_pressure(weather_response('Delhi','e6205c85b5958567349335aeb1cee7df'),1,'3:00:00'),993.56,delta=10)
		self.assertAlmostEqual(get_pressure(weather_response('Lucknow','e6205c85b5958567349335aeb1cee7df'),2,'6:00:00'),1005.48,delta=10)
		self.assertAlmostEqual(get_pressure(weather_response('Jaipur','e6205c85b5958567349335aeb1cee7df'),3,'9:00:00'),972.43,delta=10)
		self.assertAlmostEqual(get_pressure(weather_response('Allahabad','e6205c85b5958567349335aeb1cee7df'),1,'12:00:00'),1003.59,delta=10)
	
	def test_get_wind(self):
		self.assertAlmostEqual(get_wind(weather_response('Delhi','e6205c85b5958567349335aeb1cee7df'),1,'3:00:00'),4.66,delta=10)
		self.assertAlmostEqual(get_wind(weather_response('Lucknow','e6205c85b5958567349335aeb1cee7df'),2,'6:00:00'),2.67,delta=10)
		self.assertAlmostEqual(get_wind(weather_response('Jaipur','e6205c85b5958567349335aeb1cee7df'),3,'9:00:00'),2.81,delta=10)
		self.assertAlmostEqual(get_wind(weather_response('Allahabad','e6205c85b5958567349335aeb1cee7df'),1,'12:00:00'),1.42,delta=10)

	def test_get_sealevel(self):
		self.assertAlmostEqual(get_sealevel(weather_response('Delhi','e6205c85b5958567349335aeb1cee7df'),1,'3:00:00'),1018.05,delta=10)
		self.assertAlmostEqual(get_sealevel(weather_response('Lucknow','e6205c85b5958567349335aeb1cee7df'),2,'6:00:00'),1019.68,delta=10)
		self.assertAlmostEqual(get_sealevel(weather_response('Jaipur','e6205c85b5958567349335aeb1cee7df'),3,'9:00:00'),1018.42,delta=10)
		self.assertAlmostEqual(get_sealevel(weather_response('Allahabad','e6205c85b5958567349335aeb1cee7df'),1,'12:00:00'),1018.15,delta=10)
	
if __name__=='__main__':
	unittest.main()
