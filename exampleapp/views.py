from django.core.urlresolvers import reverse
from sky_visitor.views import InvitationStartView, InvitationCompleteView


class CustomInvitationStartView(InvitationStartView):
    template_name = 'exampleapp/invitation_start.html'


class CustomInvitationCompleteView(InvitationCompleteView):
    template_name = 'exampleapp/invitation_complete.html'

    def get_success_url(self):
        return reverse('home')

