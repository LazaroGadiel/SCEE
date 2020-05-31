from django.db import models

# Create your models here.
class Persona(models.Model):
	 id= models.AutoField(primary_key=True)
	 name= models.CharField(max_length=255)
	 plaza= models.CharField(max_length=255)
	 fijo= models.CharField(max_length=255)
	 celular= models.CharField(max_length=255)
	 uo= models.CharField(max_length=255)
	 cargo= models.CharField(max_length=255)

	 def __str__(self):
	     return u'{}{}'.format(self.name,self.cargo)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, blank=True,on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    
    def __str__(self):
         return '{}'.format(self.persona.name)

class Centro(models.Model):
	nombre=models.CharField(max_length=255)
	persona=models.ManyToManyField(Persona,blank=True)
	def __str__(self):
           return u'{}'.format(self.nombre)       	
         		         