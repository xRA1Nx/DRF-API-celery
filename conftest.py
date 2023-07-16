from unittest.mock import Mock

import pytest


@pytest.fixture()
def mock_for_module(mocker):
    def with_args(module_name: str, function_name: str, *args, **kwargs) -> Mock:
        return mocker.patch(f'{module_name}.{function_name}', *args, **kwargs)

    return with_args
