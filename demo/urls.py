from django.conf.urls import patterns, include, url

# Moving wow specific context processors here
from django.conf import global_settings, settings
settings.TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "demo.context_processors.events",
    "demo.context_processors.gow",
    "demo.context_processors.roster",
    "demo.context_processors.attending",
    "demo.context_processors.bosses",
    "demo.context_processors.raid"
)

 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('demo.views',
    # Examples:
    # url(r'^$', 'newmjidemo.views.home', name='home'),
    # url(r'^newmjidemo/', include('newmjidemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #
    # \/
    # (________>

    url(r'^$', 'index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/events.json', 'eventsJson', name='eventsjson'),
    url(r'^event/(?P<event_id>\d+)', 'event', name='events'),
    url(r'^about/', 'about', name='about'),
    url(r'^chat/', 'chat', name='chat'),
    url(r'^archive/', 'archive', name='archive'),
    url(r'^article/(?P<article_id>\d+)', 'article', name='article'),

    url(r'^new_article/', 'new_article_page', name='new_article'),
    url(r'^save_article/', 'save_article', name='save_article'),
    url(r'^new_g_o_w/', 'new_g_o_w', name='new_gow'),
    url(r'^save_g_o_w/', 'save_g_o_w', name='save_gow'),
    url(r'^gow/(?P<gow_id>\d+)', 'gow', name='gow'),
    url(r'^remove_attendance/(?P<att_id>\d+)', 'remove_attendance', name='remove_attendance'),

    # user stuff
    url(r'^logout/', 'logout_view', name='logout'),
    url(r'^profile/', 'profile', name='profile'),
    url(r'^login/', 'login_view', name='login'),
    url(r'^register/', 'register', name='register'),
    url(r'register_view/', 'register_view', name='register_view'),
)	

