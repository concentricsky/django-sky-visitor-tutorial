from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import CustomInvitationStartView, CustomInvitationCompleteView, MembersOnlyView
from sky_visitor.urls import TOKEN_REGEX

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exampleapp.views.home', name='home'),
    # url(r'^exampleapp/', include('exampleapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


    url(r'^members/$', MembersOnlyView.as_view(), name='members_only'),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    # These URLS come before include()-ing the sky_visitor URLs so they override the defaults.
    url(r'user/invitation/$', CustomInvitationStartView.as_view(), name='invitation_start'),
    url(r'user/invitation/%s/$' % TOKEN_REGEX, CustomInvitationCompleteView.as_view(), name='invitation_complete'),

    # The default sky_visitor URLs
    url(r'^user/', include('sky_visitor.urls')),
)
