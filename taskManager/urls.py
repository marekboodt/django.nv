#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
# INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

from django.urls import include, re_path
from django.contrib import admin
from taskManager.views import index
from taskManager import taskManager_urls

urlpatterns = [
    re_path(r'^$', index, name='index'),  # Fixed: Added closing quote and proper regex for root URL
    re_path(r'^taskManager/', include((taskManager_urls, "taskManager"), namespace="taskManager")),
    re_path(r'^admin/', admin.site.urls),
]
