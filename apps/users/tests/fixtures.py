import pytest


@pytest.fixture()
def super_user_factory(user_factory):
    def _super_user_factory(**kwargs):
        return user_factory(
            is_superuser=True, is_staff=True, **kwargs
        )
    return _super_user_factory