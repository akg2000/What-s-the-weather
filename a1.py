import urllib.request
import datetime
ddt=datetime.date.today()

# function to get weather response
def weather_response(location, API_key):
	url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key)
	json = str(url.read())#to convert the returned data into string.
	return json
#to find if the city entered exists or not.
def has_error(location,json):
	length=len(json)
	k1 = json.rfind('name',0,length)#we find name as it will be only present in the string if the city name is correct.
	k2 = json.rfind('coord',0,length)
	k3 = json[k1+7:k2-2]
	if k3!=location:
		return True
	return False

# function to get attributes on nth day

#this functions searches for the temp of the day on a specific date and time input by the user
def get_temperature(json,n,t='21:00:00'):
	date = str(ddt + datetime.timedelta(days=n))
	k2=str(t)
	k1=json.find(date + " " + k2)
	k4=int(k1)
	k3 = json.rfind('temp_min',0,k4)
	k5 = json.rfind('temp',0,k3)
	temp1=json[k5+6:k3-2]
	temp = float(temp1)
	return temp

# this functions helps in finding the the humidity for the specified date and time
def get_humidity(json,n,t):
	date = str(ddt + datetime.timedelta(days=n))
	k2=str(t)
	k1=json.find(date + " " + k2)
	k4=int(k1)
	k3 = json.rfind('humidity',0,k4)
	k5 = json.rfind('temp_kf',0,k4)
	humidity1=json[k3+10:k5-2]
	humidity2=int(humidity1)
	return humidity2

# this functions the value of pressure of the specified time and date for a place
def get_pressure(json,n,t):
	date = str(ddt + datetime.timedelta(days=n))
	k2=str(t)
	k1=json.find(date + " " + k2)
	k4=int(k1)
	k3 = json.rfind('pressure',0,k4)
	k5 = json.rfind('sea_level',0,k4)
	pressure1=json[k3+10:k5-2]
	pressure = float(pressure1)
	return pressure

#this functions returns the value of the wind speed for the specified time and date
def get_wind(json,n,t):
	date = str(ddt + datetime.timedelta(days=n))
	k2=str(t)
	k1=json.find(date + " " + k2)
	k4=int(k1)
	k3 = json.rfind('speed',0,k4)
	k5 = json.rfind('deg',0,k4)
	wind_speed1=json[k3+7:k5-2]
	wind_speed = float(wind_speed1)
	return wind_speed

# this function returns the sea level of a particular place
def get_sealevel(json,n,t):
	date = str(ddt + datetime.timedelta(days=n))
	k2=str(t)
	k1=json.find(date + " " + k2)
	k4=int(k1)
	k3 = json.rfind('sea_level',0,k4)
	k5 = json.rfind('grnd_level',0,k4)
	sea_level1=json[k3+11:k5-2]
	sea_level = float(sea_level1)
	return sea_level

# GENERAL FUNCTION LOGIC
# Since we have the required string with us we need to find the required keyword of the data we need to acquire the data of
#since some of the keywords like temp repeat too many times which may gives us wrong results as the function may find find any other location of the word than what is required
#so we find a keyword in the string that only appears once then we find the required related keyword by using relative indexing.
#by defining appropriate varibales to define the index of the different variables ,we can esily find the data in the string.
#Also as each function requires us to find the details for the specific date and time for the date we use the datetime library to find the appropriate date
#we also use rfind() function to find the required keyword in the string in the reverse function , we need to use this as the date and time is printed after the data for that specific date and time so this functions saves us from multiple if else statements that maybe some exception cases.
 

