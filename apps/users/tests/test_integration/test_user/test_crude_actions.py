import pytest
from rest_framework import status
from restdoctor.rest_framework.reverse import reverse

from apps.users.logic.selectors.user import users__all


@pytest.mark.django_db()
def test__user_list__success_case(
        api_client__super_user_factory__auth, user_factory
):
    """
    В данном кейсе получаем 2 пользователя, т.к.
    один пользователь - это супер админ, который имеет доступ к ручке,
    второй - пользователь который мы создаем

    """

    reverse_path = 'user-list'

    user_factory(email='test@test.ru', login='test_login')

    response = api_client__super_user_factory__auth.get(path=reverse(reverse_path))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db()
def test__user_detail_success_case(
        api_client__super_user_factory__auth, user_factory
):
    user = user_factory(email='test@test.ru')
    reverse_path = 'user-detail'
    response = api_client__super_user_factory__auth.get(
        path=reverse(reverse_path, kwargs={'pk': user.pk})
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == user.pk


@pytest.mark.django_db()
def test__user_detail_case_wrong_pk(
        api_client__super_user_factory__auth, user_factory
):
    user_factory(email='test@test.ru')
    reverse_path = 'user-detail'
    response = api_client__super_user_factory__auth.get(
        path=reverse(reverse_path, kwargs={'pk': 100500})
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
