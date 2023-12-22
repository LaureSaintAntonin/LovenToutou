from django.db import models
from django.core.validators import RegexValidator, EmailValidator


# Je crée le modèle de mon objet Propriétaire
# Lorsque l'on rajoute un champ à un modèle déjà migré, 
# tjs mettre une valeur par défaut (ex:default=None) sinon migration impossible
class Owner(models.Model):
	first_name = models.CharField('prénom', max_length=50)
	last_name = models.CharField('nom', max_length=50)
	breeding_name = models.CharField('elevage', max_length=70, default=None)
	siret_number = models.PositiveBigIntegerField()
	complete_address = models.TextField(max_length=250)
	# Utilisez un champ CharField pour le numéro de téléphone
	phone_regex = RegexValidator(
		regex=r'^\d{10}$',  # Exemple : 1234567890 (10 chiffres)
		message="Le numéro de téléphone doit contenir 10 chiffres."
	)
	phone_number = models.CharField(
		validators=[phone_regex],
		max_length=10,
		blank=False,  # Le champ doit contenir un numéro
	)
# Champ pour l’adresse mail
	mail_owner = models.CharField(
		max_length=255,
		validators=[EmailValidator()],
		blank=False,
		default=None
	)
# Champ pour les mots de passe ? fonction de hashage ?

# je crée le modèle de mon objet Chien
class Dog(models.Model):
	owner_dog = models.ForeignKey('Owner', on_delete=models.CASCADE, default=None)
	name = models.CharField('nom', max_length=50)
	chip_number = models.PositiveBigIntegerField()
	pic_profile = models.ImageField(
		upload_to="images/",
		max_length=255,
		blank=False,
		null=False,
		width_field="image_width",
		height_field="image_height",
		help_text="Téléchargez une image de profil (format JPEG ou PNG).",
		verbose_name="Photo de profil",
	),
	# Je crée une sous classe de genre pour le chien
	class Gender(models.TextChoices):
		MALE = 'M', 'Male'
		FEMALE = 'F', 'Female'
		OTHER = 'O', 'Other'
	gender = models.CharField(
		max_length=1,
		choices=Gender.choices,
		default=Gender.OTHER,
	)


# Create your models here.
