from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    name = models.CharField(
        'Имя студента',
        max_length=50, 
        db_index=True)
        
    telegram_id = models.CharField(
        'Telegram id',
        max_length=50,
        db_index=True)
    
    email = models.CharField(
        'email',
        max_length=50,
        db_index=True)
    
    level = models.CharField(
        'Уровень ученика',
        max_length=50, 
        db_index=True)
    
    project_week = models.CharField(
        'Неделя проекта',
        max_length=50,
        db_index=True,
        blank=True)
    
    call_time = models.CharField(
        'Удобное время для созвона',
        max_length=50,
        db_index=True,
        blank=True)#переименовать в 'удобное время'

    is_dv = models.BooleanField('Ученик с Дальнего Востока', default=None,
                                null=True, blank=True)

    registration_status = models.BooleanField('Статус регистрации в проекте', default=False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = ' Students'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'email', 'telegram_id'],
                name='unique_name_email_telegram_id'
            )]

    def __str__(self):
        return f'{self.name}'


# class Call_time(models.Model):
#     time = models.TimeField(auto_now=False, auto_now_add=False)
#     participants_number = models.PositiveIntegerField(
#         'Время созвона',
#         validators=[
#             MaxValueValidator(
#                 5)]
#         )
#     product_manager = models.ForeignKey("PM", verbose_name=("менеджер проекта"), on_delete=models.CASCADE)
#     group = models.ForeignKey('Group', verbose_name=("Группа"), on_delete=models.CASCADE)



class Group(models.Model):
    pass

    




# class PM(models.Model):
#     name = models.CharField(
#         'ФИО продукт менеджера',
#         max_length=50,
#         db_index=True)
#     available_time = models.TimeField()#переименовать в 'удобное время'


# class Enrolled_student(models.Model):
#     name = models.CharField(
#         'ФИО студента',
#         max_length=50,
#         db_index=True)
    
#     email = models.CharField(
#         'email',
#         max_length=50,
#         db_index=True)
    
#     telegram_id = models.CharField(
#         'Telegram id',
#         max_length=50,
#         db_index=True)
    
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['name', 'email', 'telegram_id'],
#                 name='user_author'
#             )]    
