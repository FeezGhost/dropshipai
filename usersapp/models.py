from django.db import models
from django.contrib.auth.models import User
import uuid

User._meta.get_field('email')._unique = True
