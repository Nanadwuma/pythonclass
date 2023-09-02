import requests

try:

    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.6762&lon=139.6503&appid=49699780b388e665cf3617a1157b3b7a")
  
except:
    print("No internet access:")

respose_json = response.json()

temp = respose_json["main"]["temp"]
temp_min = respose_json["main"]["temp_min"]
temp_max = respose_json["main"]["temp_max"]

print(f"In Tokyo, it is currently {temp}° C")
print(f"Today's High: {temp_max}° C")
print(f"Today's Low: {temp_min}° C")

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:

            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=49699780b388e665cf3617a1157b3b7a")
  
        except:
            print("No internet access:")

    respose_json = response.json()
    
    self.temp = respose_json["main"]["temp"]
    self.temp_min = respose_json["main"]["temp_min"]
    self.temp_max = respose_json["main"]["temp_max"]

def temp_print(self):
    print(f"In Tokyo, it is currently {self.temp}° C")
    print(f"Today's High: {self.temp_max}° C")
    print(f"Today's Low: {self.temp_min}° C")

my_city = City("Tokyo", 35.6762, 139.6503)

my_city.temp_print()
