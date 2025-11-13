from django.contrib import admin
from .models import Post #Post is the name of table(model) we created in models.py, we were inserting data in that table by using shell but we can do that here also but first we need to type python manage.py createsuperuser in terminal to create admin user
# Register your models here.
admin.site.register(Post) #we are registering Post model so that we can see it in admin panel
#createsuperuser krna issliye zaroori hai kyuki jb browser mei port/admin/ aisa search karoge toh sqllite username & password maangega toh wahi hamlog yaha save krte hain, baar baar krne ka koi zaroorat nhi hai.