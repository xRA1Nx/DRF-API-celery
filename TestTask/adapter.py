from allauth.account.adapter import DefaultAccountAdapter

from apps.users.dto.user import UserCreateRequestDto
from apps.users.logic.facades.user import user__create

from allauth.account.utils import user_email, user_field, user_username


class AllauthCustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        if not commit:
            return

        data = form.cleaned_data
        email = data.get("email")
        user_email(user, email)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.login = email
            user.save()
        return user

