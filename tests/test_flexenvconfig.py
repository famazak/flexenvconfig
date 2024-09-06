# ruff: noqa: PGH003
import pytest

from flexenvconfig import BaseFlexEnvConfig


class TestConfig(BaseFlexEnvConfig):
    def __init__(self):
        self.test_value = TestConfig.get_env("TEST_ENV_VAR", "test value")
        self.no_value = TestConfig.get_env("ENV_VAR_NO_VALUE")

    def validate(self) -> bool:
        return all([self.test_value])


@pytest.fixture
def test_config_class() -> TestConfig:
    """Pytest fixture implementing BaseFlexEnvConfig.

    Fixture which returns a simple test implementation of BaseFlexEnvConfig
    """
    test_config = TestConfig()
    return test_config


def test_config_is_abstract() -> None:
    """Test whether base config object is abstract.

    Attempting to instantiate without implementing abstract methods should raise
    TypeError
    """
    with pytest.raises(TypeError):
        BaseFlexEnvConfig()  # type: ignore


def test_get_env_with_default_value(mocker, test_config_class: TestConfig):
    """Test that a config env var that gets set with a default is retrieved correctly."""
    mocker.patch.dict("os.environ", {"TEST_ENV_VAR": "test_value"}, clear=True)
    assert test_config_class.get_env("TEST_ENV_VAR") == "test_value"


def test_get_env_with_no_default(mocker, test_config_class: TestConfig):
    """Test that a config env var that does not get set is retrieved correctly as None."""
    mocker.patch.dict("os.environ", clear=True)
    assert test_config_class.get_env("ENV_VAR_NO_VALUE") is None


def test_abstract_methods(test_config_class: TestConfig):
    """Assert that test implementation of BaseFlexEnvConfig has abstract methods implemented."""
    assert hasattr(test_config_class, "__init__")
    assert hasattr(test_config_class, "validate")


def test_validate(mocker, test_config_class: TestConfig) -> None:
    mocker.patch.dict("os.environ", {"TEST_ENV_VAR": "test_value"}, clear=True)
    assert test_config_class.validate()


def test_validate_required_config_not_set(mocker, test_config_class: TestConfig) -> None:
    mocker.patch.object(test_config_class, "test_value", None)
    assert not test_config_class.validate()
