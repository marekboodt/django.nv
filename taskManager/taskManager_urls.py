#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#                       INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

from django.urls import re_path
from taskManager.views import *

app_name = "taskManager"

urlpatterns = [
    re_path(r'^$', index, name='index'),

    # File
    re_path(r'^download/(?P<file_id>\d+)/$', download, name='download'),
    re_path(r'^(?P<project_id>\d+)/upload/$', upload, name='upload'),
    re_path(r'^downloadprofilepic/(?P<user_id>\d+)/$', download_profile_pic, name='download_profile_pic'),

    # Authentication & Authorization
    re_path(r'^register/$', register, name='register'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^manage_groups/$', manage_groups, name='manage_groups'),
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^change_password/$', change_password, name='change_password'),
    re_path(r'^forgot_password/$', forgot_password, name='forgot_password'),
    re_path(r'^reset_password/$', reset_password, name='reset_password'),
    re_path(r'^profile/(?P<user_id>\d+)$', profile_by_id, name='profile_by_id'),
    re_path(r'^profile_view/(?P<user_id>\d+)$', profile_view, name='profile_view'),

    # Projects
    re_path(r'^project_create/$', project_create, name='project_create'),
    re_path(r'^(?P<project_id>\d+)/edit_project/$', project_edit, name='project_edit'),
    re_path(r'^manage_projects/$', manage_projects, name='manage_projects'),
    re_path(r'^(?P<project_id>\d+)/project_delete/$', project_delete, name='project_delete'),
    re_path(r'^(?P<project_id>\d+)/$', project_details, name='project_details'),
    re_path(r'^project_list/$', project_list, name='project_list'),

    # Tasks
    re_path(r'^(?P<project_id>\d+)/task_create/$', task_create, name='task_create'),
    re_path(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/$', task_details, name='task_details'),
    re_path(r'^(?P<project_id>\d+)/task_edit/(?P<task_id>\d+)$', task_edit, name='task_edit'),
    re_path(r'^(?P<project_id>\d+)/task_delete/(?P<task_id>\d+)$', task_delete, name='task_delete'),
    re_path(r'^(?P<project_id>\d+)/task_complete/(?P<task_id>\d+)$', task_complete, name='task_complete'),
    re_path(r'^task_list/$', task_list, name='task_list'),
    re_path(r'^(?P<project_id>\d+)/manage_tasks/$', manage_tasks, name='manage_tasks'),

    # Notes
    re_path(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/note_create/$', note_create, name='note_create'),
    re_path(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/note_edit/(?P<note_id>\d+)$', note_edit, name='note_edit'),
    re_path(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/note_delete/(?P<note_id>\d+)$', note_delete, name='note_delete'),

    re_path(r'^dashboard/$', dashboard, name='dashboard'),
    re_path(r'^search/$', search, name='search'),

    # Tutorials
    re_path(r'^tutorials/$', tutorials, name='tutorials'),
    re_path(r'^tutorials/(?P<vuln_id>[a-z\-]+)/$', show_tutorial, name='show_tutorial'),

    # Settings - DEBUG
    re_path(r'^settings/$', tm_settings, name='settings'),
]
