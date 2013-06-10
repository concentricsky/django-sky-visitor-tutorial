from sky_visitor.views import InvitationStartView, InvitationCompleteView


class CustomInvitationStartView(InvitationStartView):
    template_name = 'exampleapp/start_invite.html'


class CustomInvitationCompleteView(InvitationCompleteView):
    template_name = 'exampleapp/complete_invite.html'