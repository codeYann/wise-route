import pytest
from pydantic import ValidationError
from env import Env


class TestEnvRequired:
    def test_missing_rabbitmq_user_raises(self, monkeypatch):
        monkeypatch.delenv("RABBITMQ_USER", raising=False)
        monkeypatch.setenv("RABBITMQ_PASSWORD", "pass123")
        with pytest.raises(ValidationError):
            Env()

    def test_missing_rabbitmq_password_raises(self, monkeypatch):
        monkeypatch.setenv("RABBITMQ_USER", "user123")
        monkeypatch.delenv("RABBITMQ_PASSWORD", raising=False)
        with pytest.raises(ValidationError):
            Env()


class TestEnvDefaults:
    def test_default_host_and_port(self, monkeypatch):
        monkeypatch.setenv("RABBITMQ_USER", "user")
        monkeypatch.setenv("RABBITMQ_PASSWORD", "pass")
        env = Env()
        assert env.rabbitmq_host == "localhost"
        assert env.rabbitmq_port == 5672


class TestRabbitMQURL:
    def test_basic_url_composition(self, monkeypatch):
        monkeypatch.setenv("RABBITMQ_USER", "user")
        monkeypatch.setenv("RABBITMQ_PASSWORD", "pass")
        env = Env()
        assert env.rabbitmq_url == "amqp://user:pass@localhost:5672/"

    def test_url_encoding_special_characters(self, monkeypatch):
        monkeypatch.setenv("RABBITMQ_USER", "user@domain")
        monkeypatch.setenv("RABBITMQ_PASSWORD", "p@ss:w/rd")
        env = Env()
        assert (
            env.rabbitmq_url == "amqp://user%40domain:p%40ss%3Aw%2Frd@localhost:5672/"
        )

    def test_custom_host_and_port(self, monkeypatch):
        monkeypatch.setenv("RABBITMQ_USER", "user")
        monkeypatch.setenv("RABBITMQ_PASSWORD", "pass")
        monkeypatch.setenv("RABBITMQ_HOST", "rabbitmq.example.com")
        monkeypatch.setenv("RABBITMQ_PORT", "5673")
        env = Env()
        assert env.rabbitmq_url == "amqp://user:pass@rabbitmq.example.com:5673/"
