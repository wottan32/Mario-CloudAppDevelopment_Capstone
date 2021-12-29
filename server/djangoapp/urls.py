from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'djangoapp'
urlpatterns = [

                  # path for about view
                    path(route='about', view=views.about, name='about'),
                  # path for contact us view
                    path(route='contact', view=views.contact, name='contact'),
                  # path for registration
                    path(route='registration', view=views.registration_request, name='register'),
                  # path for login
                    path(route='', view=views.login_request, name='login'),
                  # path for logout
                    path(route='', view=views.logout_request, name='logout'),

                    path(route='', view=views.get_dealerships, name='index'),

                  # path for dealer reviews view
                  path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),

                  # path for add a review view

                  path(route='dealer/<int:dealer_id>/', view=views.add_review, name='add_review'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
