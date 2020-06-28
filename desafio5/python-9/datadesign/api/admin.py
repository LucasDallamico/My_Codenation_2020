from django.contrib import admin
#mueus modelos
from .models import User, Agent, Event, Group, GroupUser

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Event)
admin.site.register(Group)
admin.site.register(GroupUser)