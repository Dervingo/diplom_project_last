from django.db import models


class Diplom(models.Model):
    org_name = models.CharField(verbose_name="Название образовательной организации",
                                help_text="Введите навзвание образовательной организации",
                                max_length=200,
                                )
    qualification = models.CharField(max_length=100,
                                     verbose_name="Квалификация",
                                     help_text="Напишите квалификацию",
                                    )
    ser_number = models.CharField(max_length=15,
                                  verbose_name="Номер серии",
                                  help_text="Введите номер серии",
                                  )
    reg_number = models.CharField(max_length=10,
                                  verbose_name="Регистрационный номер",
                                  help_text="Введите регистрационный номер",
                                  )
    grant_date = models.DateField(verbose_name="Дата выдачи",
                                  help_text='Введите дату выдачи',
                                  )
    student_name = models.CharField(max_length=200,
                                    verbose_name="ФИО",
                                    help_text="ФИО",
                                    )
    speciality = models.CharField(max_length=100,
                                  verbose_name="Специальность",
                                  help_text="Введите специальность",
                                  )
    supervisor = models.CharField(max_length=200,
                                  verbose_name="Руководитель",
                                  help_text="Введите ФИО руководителя",
                                  )
    chairman = models.CharField(max_length=200,
                                verbose_name="Председатель ЭКЗ комиссии",
                                help_text="Введите ФИО председатель",
                                )
    year = models.DateField(verbose_name="Дата решения",
                            help_text="Введите дату решения",
                            )
    copy = models.ImageField(verbose_name="Копия диплома",
                             help_text="Вставьте копию диплома",
                             null=True,
                             blank=True,
                             )

    class Meta:
        ordering = ('year',)
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return f"{self.student_name} - ({self.year})"
