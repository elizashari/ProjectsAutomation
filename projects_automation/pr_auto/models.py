from django.db import models



class Level(models.Model):
    title = models.CharField(
        'Уровень',
        max_length=25, 
        db_index=True)
    
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
    
    email = models.CharField(
        'email',
        max_length=50,
        db_index=True)
    
    level = models.ForeignKey(Level, verbose_name='Уровень ученика',
                              on_delete=models.CASCADE)
    
    is_dv = models.BooleanField('Ученик с Дальнего Востока', default=None,
                                null=True, blank=True)
    

    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = ' Students'


    def __str__(self):
        return f'{self.name}'
