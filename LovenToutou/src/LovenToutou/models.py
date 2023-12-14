from django.db import models
from django.core.validators import RegexValidator, EmailValidator


# Je crée le modèle de mon objet Propriétaire
class Owner(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	siret_number = models.PositiveBigIntegerField()
	# Champ pour l’adresse mail
	mail_owner = models.CharField(
		max_length=255,
		validators=[EmailValidator()],
		blank=False,
		default=None
	)

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

	complete_address = models.TextField(max_length=250)


# je crée le modèle de mon objet Chien
class Dog(models.Model):
	owner_dog = models.ForeignKey('Owner', on_delete=models.CASCADE, default=None)
	name = models.CharField(max_length=50)
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

	# def __str__(self):
		# return self.name

# Create your models here.
