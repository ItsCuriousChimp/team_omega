from django.contrib import admin
from book_my_show.authenticate.models import user_model

# admin.site.register(user_model.MyAccountManager)

# admin.site.unregister(User)
admin.site.register(user_model.UserModel)
