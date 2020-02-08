from django.contrib import admin

from .models import Activity, Action, Reminder, Due, ActivityList

# admin.site.register(Activity)
# admin.site.register(Action)
# admin.site.register(Activity)
# admin.site.register(Activity)
# admin.site.register(Activity)


from django.apps import apps

models = [Activity, Action, Reminder, Due, ActivityList]

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
