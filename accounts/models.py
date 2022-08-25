from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email,password=None, is_staff=False, is_active=True, admin=False):
        if not email:
            raise ValueError('users must have a email')

        if not password:
            raise ValueError('users must have a password')
        

        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.shop = is_staff
        user_obj.active = is_active
        user_obj.admin = admin
       

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email,password=password,is_staff=True,)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            admin=True,
        )
        return user

# Create your models here.
class User(AbstractBaseUser):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER , 'Other'),
    )
    username = models.CharField(max_length=25)    
    name = models.CharField(max_length=100)    
    email=models.EmailField(blank=False, null=False, unique=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    shop = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    # location_id=models.ForeignKey(Location, to_fields=['state_id', 'city_id','area_id'], related_name='abc', on_delete=models.CASCADE)

  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.shop

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.admin