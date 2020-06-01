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
     division_territorial = models.ForeignKey(Division_Territorial, null=True,on_delete=models.SET_NULL)
     nombre= models.CharField(max_length=255)

     def __str__(self):
	     return u'{}-{}'.format(self.division_territorial.nombre, self.nombre)

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
	 centro = models.ForeignKey(Centro, null=True,on_delete=models.SET_NULL)
	 nombre= models.CharField(max_length=255)
	 plaza= models.CharField(max_length=255)
	 cargo= models.CharField(max_length=255)
	 categoria= models.CharField(max_length=255, choices=(('Oper', 'Operaciones'), ('Admon', 'Administración'), ('Serv', 'Servicios'), ('Tecn', 'Técnicos'), ('Func', 'Funcionario')))
	 anexo= models.ForeignKey(Anexo, null=True,on_delete=models.SET_NULL)
	 superior=models.ForeignKey('self', blank=True, null=True,on_delete=models.SET_NULL)
	 usuario=models.OneToOneField(User,unique=True, blank=True,null=True,on_delete=models.SET_NULL)
	 subordinados= models.CharField(max_length=2, choices=(('si', 'Si'), ('no', 'No')))
	 evaluar= models.CharField(max_length=255, choices=(('si', 'Si'), ('no', 'No')))
     
	 def __str__(self):
	     return u'{}'.format(self.nombre)

class Criterio(models.Model):
     id= models.AutoField(primary_key=True)
     aspecto=models.ForeignKey(Aspecto, null=True,on_delete=models.SET_NULL)	       	
     descripcion=models.TextField()
     peso=models.IntegerField()
     valoracion= models.CharField(max_length=255, choices=(('positivo', 'Positivo'), ('negativo', 'Negativo')))        		         

     def __str__(self):
	     return u'{}'.format(self.descripcion)

class Evaluacion(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     nota= models.FloatField()
     fecha= models.DateField()
     categoria= models.CharField(max_length=255, choices=(('muy-bien', 'Muy Bien'), ('bien', 'Bien'), ('regular', 'Regular'), ('mal', 'Mal')))        		         


class Criterio_Trabajador(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     criterio= models.ForeignKey(Criterio, null=True,on_delete=models.SET_NULL)
     fecha= models.DateField()

class Logros_Fortaleza(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     descripcion= models.TextField()
     fecha= models.DateField()

class Deficiencias_Debilidades(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     descripcion= models.TextField()
     fecha= models.DateField()

class Recomendaciones(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     descripcion= models.TextField()
     evidencia=models.TextField()
     fecha= models.DateField()

class Tareas(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     descripcion= models.TextField()
     fecha_cumplimiento= models.DateField()
     estado= models.CharField(max_length=255, choices=(('cumplido', 'Cumplido'), ('incumplido-imputable', 'Incumplido Imputable'), ('incumplido-no-imputable', 'Incumplido no Imputable')))

class Plan_Formacion(models.Model):
     id= models.AutoField(primary_key=True)
     trabajador= models.ForeignKey(Trabajador, null=True,on_delete=models.SET_NULL)
     descripcion= models.TextField()
     fecha_cumplimiento= models.DateField()
     estado= models.CharField(max_length=255, choices=(('cumplido', 'Cumplido'), ('incumplido-imputable', 'Incumplido Imputable'), ('incumplido-no-imputable', 'Incumplido no Imputable')))     