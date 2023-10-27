from django.db import models


class Level(models.Model):
    title = models.CharField(
        'Уровень',
        max_length=25, 
        db_index=True)
    
    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = ' Levels'

    
    def __str__(self):
        return f'{self.title}'
    

class Student(models.Model):
    name = models.CharField(
        'Имя студента',
        max_length=50, 
        db_index=True)
        
    telegram_id = models.CharField(
        'Telegram id',
        max_length=50,
        db_index=True)
    
    email = models.EmailField('email ученика')
    
    level = models.ForeignKey(Level, verbose_name='Уровень ученика',
                              on_delete=models.CASCADE)

    
    project_week = models.CharField(
        'Неделя проекта',
        max_length=50,
        db_index=True,
        blank=True)
    
    call_time = models.CharField(
        'Удобное время для созвона',
        max_length=50,
        db_index=True,
        blank=True)

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


class Project(models.Model):
    title = models.CharField(
        'Название проекта',
        max_length=50, 
        db_index=True)
    level = models.ForeignKey(Level, verbose_name='Уровень проекта',
                              on_delete=models.CASCADE)
    brief = models.FileField(upload_to=None, max_length=254) 

    def __str__(self):
        return f'{self.title}'


class Call_time(models.Model):
    call_time = models.TimeField('Время созвона')
    def __str__(self):
        return f'{self.call_time}'
    
class Project_week(models.Model):
    project_week = models.CharField('Неделя проекта', max_length=50)
    def __str__(self):
        return f'{self.project_week}'


class PM(models.Model):
    name = models.CharField(
        'Имя PM',
        max_length=50,
        db_index=True)
    telegram_id = models.CharField(
        'Telegram id',
        max_length=50,
        db_index=True)
    call_time = models.ManyToManyField(Call_time)

    def __str__(self):
        return f'{self.name}' 
    

class Group(models.Model):
    title = models.CharField(max_length=25,verbose_name='Группа')
    pm = models.ForeignKey(PM, on_delete=models.CASCADE, verbose_name='PM проекта')
    students = models.ManyToManyField(Student)
    call_time = models.CharField(max_length=25,verbose_name='Время созвона группы', blank=True)
    project_week = models.CharField(max_length=25,verbose_name='Неделя проекта', blank=True)

    def __str__(self):
        return f'{self.title}'
 



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

