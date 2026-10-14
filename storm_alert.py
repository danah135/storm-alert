import requests
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
channel = os.environ.get("channel")
url= "https://api.open-meteo.com/v1/forecast?latitude=24.71&longitude=46.68&current=precipitation,wind_speed_10m,temperature_2m"
telegram_url= f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

try:   
    response = requests.get(url, timeout=30)
    data = response.json()

    precip=data['current']['precipitation']
    wind= data['current']['wind_speed_10m']
    temperature = data['current']['temperature_2m']

    print("Precipitation:", precip)
    print("Wind Speed:", wind)
    print("Temperature:", temperature)

    if precip > 5 or wind> 60:
        print(" تحذير! عاصفة قادمة على مدينة الرياض.")  
        print("Warning! A storm is coming.")
        print("precipitation:", precip)
        print("wind speed:", wind)
        print("temperature:", temperature)

      
        message=(f"تنبيه! عاصفة قادمة. \n\nالامطار: {precip} \nسرعة الرياح: {wind} \nدرجة الحرارة: {temperature}"
            f"ينصح بعدم الخروج من المنزل"
            )
        data_msg= {"chat_id": channel, "text": message}
        response = requests.post(telegram_url, json=data_msg, timeout=30)
        print(response.json())
else:
        print("الطقس مستقر.")
        print("The weather is stable.")
except Exception as e:
  print(f"خطأ:{e}")
