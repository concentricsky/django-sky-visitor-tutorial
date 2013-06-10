from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from sky_visitor.views import InvitationStartView, InvitationCompleteView, LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _


class CustomInvitationStartView(InvitationStartView):
    template_name = 'exampleapp/invitation_start.html'
    success_message = _("Invitation successfully delivered. Invite more friends!")

    def get_email_kwargs(self, user):
        kwargs = super(CustomInvitationStartView, self).get_email_kwargs(user)
        # Custom subject line
        kwargs['subject'] = "Your friend invited you to join the community!"
        return kwargs


class CustomInvitationCompleteView(InvitationCompleteView):
    template_name = 'exampleapp/invitation_complete.html'

    def get_success_url(self):
        return reverse('home')


class MembersOnlyView(LoginRequiredMixin, TemplateView):
    template_name = 'exampleapp/members_only.html'
