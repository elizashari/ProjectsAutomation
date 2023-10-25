from django import forms
from datetime import datetime, timedelta
from datetime import time
from pr_auto.models import Student


# available_time = ['10:00-12:00', '20:00-22:00', ]   #PM.objects.values_list('available_time', flat=True)
# timings_list = []

# def count_timings(available_time, timings_list):
#     timings_list = []
#     for t in available_time:
#         timings = []
#         start_time, end_time = t.split('-')
#         start = datetime.strptime(start_time, "%H:%M")
#         print(start.strftime("%H:%M"))
#         end = datetime.strptime(end_time, "%H:%M")
#         result = end - start
#         print(result)
#         result2 = result / timedelta(minutes=30)
#         print(result2)
#         for _ in range(int(result2)):
#             if not timings:
#                 tm = start + timedelta(minutes=30)
#                 time_str = str(tm.strftime("%H:%M"))
#                 timings.append(f"{start.strftime('%H:%M')}-{time_str}")
#             else:    
#                 previous_time = timings[-1].split('-')[1]
#                 start = datetime.strptime(previous_time, "%H:%M")
                
#                 tm = start + timedelta(minutes=30) 
#                 time_str = str(tm.strftime("%H:%M"))
#                 timings.append(f"{previous_time}-{time_str}")
#         timings_list.append(timings)    
#     return timings_list
#     # return timings


# print(count_timings(available_time, timings_list)) 



class Project_Registration_Form(forms.ModelForm):
    # available_time = PM.objects.values_list('available_time', flat=True)

    class Meta:
        model = Student
        fields = ('email', )