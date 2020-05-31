from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Division_Territorial(models.Model):
	 id= models.AutoField(primary_key=True)
	 nombre=models.CharField(max_length=255)

	 def __str__(self):
	     return u'{}'.format(self.nombre)

class Centro(models.Model):
     id= models.AutoField(primary_key=True)
     division_territorial = models.ForeignKey(Division_Territorial, blank=True,null=True,on_delete=models.SET_NULL)
     nombre= models.CharField(max_length=255)

     def __str__(self):
	     return u'{}{}'.format(self.division_territorial.nombre, self.nombre)

class Aspecto(models.Model):
     id= models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=255)	       	
     descripcion=models.TextField()

     def __str__(self):
	     return u'{}'.format(self.nombre)	     

class Anexo(models.Model):
     id= models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=255)	       	
     descripcion=models.TextField()
     aspecto=models.ManyToManyField(Aspecto,blank=True)

     def __str__(self):
	     return u'{}'.format(self.nombre)

class Trabajador(models.Model):
	 id= models.AutoField(primary_key=True)
	 centro = models.ForeignKey(Centro, blank=True,null=True,on_delete=models.SET_NULL)
	 nombre= models.CharField(max_length=255)
	 plaza= models.CharField(max_length=255)
	 cargo= models.CharField(max_length=255)
	 categoria= models.CharField(max_length=255, choices=(('Oper', 'Operaciones'), ('Admon', 'Administración'), ('Serv', 'Servicios'), ('Tecn', 'Técnicos'), ('Func', 'Funcionario')))
	 anexo= models.ForeignKey(Anexo, blank=True,null=True,on_delete=models.SET_NULL)
	 superior=models.ForeignKey('self', blank=True, null=True,on_delete=models.SET_NULL)
	 usuario=models.OneToOneField(User,unique=True, blank=True,null=True,on_delete=models.SET_NULL)
	 subordinados= models.CharField(max_length=2, choices=(('si', 'Si'), ('no', 'No')))
	 evaluar= models.CharField(max_length=255, choices=(('si', 'Si'), ('no', 'No')))
     
	 def __str__(self):
	     return u'{}{}'.format(self.nombre,self.plaza)

class Criterio(models.Model):
     id= models.AutoField(primary_key=True)
     aspecto=models.ForeignKey(Aspecto, blank=True,null=True,on_delete=models.SET_NULL)	       	
     descripcion=models.TextField()
     peso=models.IntegerField()
     valoracion= models.CharField(max_length=255, choices=(('positivo', 'Positivo'), ('negativo', 'Negativo')))        		         

     def __str__(self):
	     return u'{}'.format(self.descripcion)