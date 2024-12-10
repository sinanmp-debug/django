from django.db import models

# Create your models here.
class departments(models.Model):
    dep_name = models.CharField(max_length = 100)
    dep_decription = models.TextField()

    def __str__(self):
          return self.dep_name


   
     
class doctors (models. Model):
  doc_name = models. CharField(max_length=255)
  doc_spec = models. CharField(max_length=255)
  dep_name = models. ForeignKey (departments, on_delete=models.CASCADE)
  doc_image = models.ImageField(upload_to='doctors')
  