import pytest

from versionkit import latest, parse


def test_parse_reads_three_parts():
    assert str(parse("1.2.3")) == "1.2.3"


def test_parse_accepts_a_leading_v_and_two_parts():
    assert str(parse("v2.4")) == "2.4.0"


def test_parse_refuses_what_is_not_a_version():
    with pytest.raises(ValueError):
        parse("1.x.0")


def test_a_higher_patch_is_newer():
    assert parse("1.2.4") > parse("1.2.3")


def test_latest_picks_the_newest():
    assert latest(["1.0.0", "1.2.0", "1.1.5"]) == "1.2.0"


def test_minor_ten_is_newer_than_minor_nine():
    assert latest(["1.9.0", "1.10.0"]) == "1.10.0"
