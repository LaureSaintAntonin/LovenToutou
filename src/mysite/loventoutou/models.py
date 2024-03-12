from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator, EmailValidator


class OwnerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail est obligatoire.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
# Je crée le modèle de mon objet Propriétaire
# Lorsque l'on rajoute un champ à un modèle déjà migré, 
# tjs mettre une valeur par défaut (ex:default=None) sinon migration impossible
class Owner(AbstractBaseUser):
	first_name = models.CharField('prénom', max_length=50)
	last_name = models.CharField('nom', max_length=50)
	breeding_name = models.CharField('elevage', max_length=70, default=None)
	siret_number = models.PositiveBigIntegerField('numéro de siret')
	complete_address = models.TextField('adresse', max_length=250)
	# Utilisez un champ CharField pour le numéro de téléphone
	phone_regex = RegexValidator(
		regex=r'^\d{10}$',  # Exemple : 1234567890 (10 chiffres)
		message="Le numéro de téléphone doit contenir 10 chiffres."
	)
	phone_number = models.CharField('numéro de téléphone',
		validators=[phone_regex],
		max_length=10,
		blank=False,  # Le champ doit contenir un numéro
	)
# Champ pour l’adresse mail
	mail_owner = models.CharField('adresse mail',
		max_length=255,
		validators=[EmailValidator()],
		blank=False,
		default=None,
		unique=True
	)
# Champ de mot de passe haché
	password = models.TextField('mot de passe', max_length=128, default=None)

# Permissions 
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

# attribut qui indique à Django d'utiliser OwnerManager pour gérer les objets de ce modèle.
	objects = OwnerManager()

#  indique le champ qui est utilisé pour identifier un utilisateur lors de 
# l'authentification. Dans ce cas, c'est l'adresse e-mail (mail_owner).
	USERNAME_FIELD = 'mail_owner'
#  liste des champs qui sont requis lors de la création d'un utilisateur.
	REQUIRED_FIELDS = ['first_name', 'last_name', 'breeding_name', 'siret_number', 'complete_address ', 'phone_number', 'mail_owner']

# Cette méthode est appelée chaque fois que l'objet est enregistré. 
# Vous pouvez y ajouter des logiques personnalisées, comme le hachage du mot de passe avant la sauvegarde.
	def save(self, *args, **kwargs):
        # Vous pouvez ajouter ici la logique pour hasher le mot de passe avant de le sauvegarder
		super().save(*args, **kwargs)

# Cette méthode retourne une représentation sous forme de chaîne de l'objet Owner. 
# Dans ce cas, c'est l'adresse e-mail du propriétaire.
	def __str__(self):
		return self.mail_owner



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
