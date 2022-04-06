from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    distt = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    @staticmethod
    def get_all_data_register():
        return Register.objects.all()

    def isExists(email_id):
        if email_id:
            return Register.objects.filter(email = email_id)
        return False

    @staticmethod
    def get_email_by_id_email(email_id):
        try:
            return Register.objects.get(email = email_id)
        except:
            return False