# # from datetime import datetime
# # from playsound import playsound

# # alarma_tiempo = input(" Introduce el tiempo de la alarma en: H:M:S\n ")

# # hora = alarma_tiempo [0:2]
# # minuto = alarma_tiempo[3:5]
# # segundo = alarma_tiempo [6:8]

# # periodo_alarma = alarma_tiempo[9:0].upper()

# # print(" alarma configurado  ")

# # while True :
# #     ahora = datetime.now()
# #     ahora_hora = datetime.strftime("%H")
# #     ahora_minuto = datetime.strftime("%M")
# #     ahora_segundo = datetime.strftime("%S")

# #     ahora_periodo = datetime.strftime("%P")

# #     if (periodo_alarma == ahora_hora):
# #         if(hora == ahora_hora):
# #             if (minuto == ahora_minuto):
# #                 if(segundo == ahora_segundo):
# #                     print("despiertate !")

# #                     break


# from datetime import datetime   
# from playsound import playsound
# playsound('./audio.mp3')
# alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
# alarm_hour=alarm_time[0:2]
# alarm_minute=alarm_time[3:5]
# alarm_seconds=alarm_time[6:8]
# alarm_period = alarm_time[9:11].upper()
# print("Setting up alarm..")
# while True:
#     now = datetime.now()
#     current_hour = now.strftime("%I")
#     current_minute = now.strftime("%M")
#     current_seconds = now.strftime("%S")
#     current_period = now.strftime("%p")
#     if(alarm_period==current_period):
#         if(alarm_hour==current_hour):
#             if(alarm_minute==current_minute):
#                 if(alarm_seconds==current_seconds):
#                     print("Wake Up!")
#                     break


# # ahora = datetime.now()
# # x = datetime.strftime
# # print(ahora)


from datetime import date, datetime
from playsound import playsound

hour = int(input ("Que horas quieres despertar ? "))
minute= int(input ("Que horas quieres despertar ? "))

sistema_AmPm = input(" Es Am or Pm ?")

ampm = sistema_AmPm.lower()

if ampm == "pm:" :
    hour += 12

i = 1 
while i<=5:
    if (hour == datetime.now().hour and 
        minute == datetime.now().minute ):
            print(f" Despiertate {hour} : {minute}")
            playsound('./audio.mp3')
            i+=1
print("Buenos dias")