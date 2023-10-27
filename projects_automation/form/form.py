from django import forms
# from datetime import datetime, timedelta
# from datetime import time
from pr_auto.models import Student, Call_time, PM


# available_time = PM.objects.values_list('call_time', flat=True)
# print(available_time)
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

# print(count_timings(available_time, timings_list)) 

# # def get_timing_for_pm():
# #     for t in count_timings(available_time, timings_list):


# timings = [('10:00-10:30', '10:30-11:00')]


class Project_Registration_Form(forms.ModelForm):
    call_time_ids = PM.objects.values_list('call_time', flat=True)

    call_times = Call_time.objects.filter(id__in=call_time_ids)

    call_time_choices = [
        (call_time.call_time, call_time.call_time) for call_time in call_times]

    available_time = forms.ChoiceField(
        choices=call_time_choices,
        label='Выберите доступное время'
    )

    class Meta:
        model = Student
        fields = ('email', 'available_time', )
