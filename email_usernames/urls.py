from django.conf.urls.defaults import *

urlpatterns = patterns('email_usernames.views',
    url(r'^login/$', 'email_login', name="email-login"), 
)

try:
    import registration
    from email_usernames.forms import EmailRegistrationForm
    urlpatterns += patterns('registration.views', 
        url(r'^register/$', 'register', { 'form_class':EmailRegistrationForm }, name="email-register"),
    )
except ImportError:
    pass