def test_validate_phone():
    assert validate_phone("+7 999 123-45-67") is True
    assert validate_phone("8 999 123 45 67") is True
    assert validate_phone("123") is False