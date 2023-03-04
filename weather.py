import requests
import datetime as dt 

BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?'
API_KEY = str(open('api_key.txt', 'r').read())

def __init__(self , city , date):
    self._city = city 
    self._date = date 

def getData(self , response):
    """ Die Funktion wird dazu verwendet , die verschiedene Wetter-Datenpunkte 
    einer gegebenen Stadt auszulesen 
        
    Args:
        data (dict): Dictionnary of weather params for the last 5 days 
    """
    data_dict = response['list']
    weather_dict = dict()
    if type(data_dict) is list :
        for i in data_dict :
            temp_dict = dict()
            dt_txt = i['dt_txt']
            temp_min = round(float(i['main']['temp_min']) - 273.15 , 3)
            temp_max = round(float (i['main']['temp_max']) - 273.15 , 3)
            feels_like = round(float(i['main']['feels_like']) - 273.15 ,3 )
            pressure = float(i['main']['pressure']) #--> bar
            humidity = i['main']['humidity'] #--> prozentangabe
            wind = i['wind']['speed'] #--> m/s
            if type(i['weather']) is list and len(i['weather']) >=1 :
                description_set = dict()
                j = 0
                for k in i['weather']:
                    j = j + 1 
                    main_description = k['main']
                    description = k['description']
                    tuple_description = (main_description , description)
                    description_set[j] = tuple_description
            temp_dict['City'] = self._city
            temp_dict['datetime_txt'] = dt_txt
            temp_dict['temp_min'] = temp_min
            temp_dict['temp_max'] = temp_max 
            temp_dict['feels_like'] = feels_like
            temp_dict['pressure'] = pressure
            temp_dict['humidity'] = humidity
            temp_dict['wind'] = wind 
            for key in list(description_set.keys()):
                temp_dict['main_description'] = description_set[key][0]
                temp_dict['description'] = description_set[key][1]
            weather_dict[dt_txt] = temp_dict
            return weather_dict 
    else :
        return None 
            
           
def request(self):
    try :
      url = BASE_URL + "appid=" + API_KEY + "&q=" + self._city + ',de'
      response = requests.get(url).json()
      return response
    except Exception as e :
        print('Error :' + e)
        return None
    
    
