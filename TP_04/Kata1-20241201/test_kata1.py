"""
KATA 1 TESTS
"""

import pytest

kt1 = pytest.importorskip("kata1")


class TestPart1:
    """
    Tests part 1
    """

    def test_name1(self):
        """Test name1"""
        assert kt1.name1 == 21
        assert isinstance(kt1.name1, int)

    def test_name2(self):
        """Test name2"""
        assert kt1.name2 == pytest.approx(10.5)
        assert isinstance(kt1.name2, float)

    def test_name3(self):
        """Test name3"""
        assert kt1.name3
        assert isinstance(kt1.name3, bool)

    def test_name4(self):
        """Test name4"""
        assert kt1.name4 == "42"
        assert isinstance(kt1.name4, str)


class TestPart2:
    """
    Tests part 2
    """

    def test_name5(self):
        """Test name5"""
        assert kt1.name5 == 42
        assert isinstance(kt1.name5, int)

    def test_name6(self):
        """Test name6"""
        assert kt1.name6 == pytest.approx(12.5)
        assert isinstance(kt1.name6, float)

    def test_name7(self):
        """Test name7"""
        assert kt1.name7 == 19
        assert isinstance(kt1.name7, int)

    def test_name8(self):
        """Test name8"""
        assert kt1.name8 == 10
        assert isinstance(kt1.name8, int)

    def test_name9(self):
        """Test name9"""
        assert kt1.name9 == pytest.approx(31.5)
        assert isinstance(kt1.name9, float)

    def test_name10(self):
        """Test name10"""
        assert kt1.name10 == 441
        assert isinstance(kt1.name10, int)

    def test_name11(self):
        """Test name11"""
        assert kt1.name11 == 1
        assert isinstance(kt1.name11, int)

    def test_name12(self):
        """Test name12"""
        assert kt1.name12 == pytest.approx(10.5)
        assert isinstance(kt1.name12, float)


class TestPart3:
    """
    Tests part 3
    """

    def test_name13(self):
        """Test name13"""
        assert kt1.name13
        assert isinstance(kt1.name13, bool)

    def test_name14(self):
        """Test name14"""
        assert not kt1.name14
        assert isinstance(kt1.name14, bool)

    def test_name15(self):
        """Test name15"""
        assert kt1.name15
        assert isinstance(kt1.name15, bool)

    def test_name16(self):
        """Test name16"""
        assert not kt1.name16
        assert isinstance(kt1.name16, bool)

    def test_name17(self):
        """Test name17"""
        assert kt1.name17
        assert isinstance(kt1.name17, bool)

    def test_name18(self):
        """Test name18"""
        assert not kt1.name18
        assert isinstance(kt1.name18, bool)


class TestPart4:
    """
    Tests part 4
    """

    def test_name19(self):
        """Test name19"""
        assert kt1.name19 == 42
        assert isinstance(kt1.name19, int)

    def test_name20(self):
        """Test name20"""
        assert kt1.name20 == "19"
        assert isinstance(kt1.name20, str)

    def test_name21(self):
        """Test name21"""
        assert kt1.name21 == 2
        assert isinstance(kt1.name21, int)

    def test_name22(self):
        """Test name22"""
        assert kt1.name22 == 144
        assert isinstance(kt1.name22, int)


class TestPart51:
    """
    Tests is_even
    """

    def test_is_even_0(self):
        """Test is_even(0)"""
        value = kt1.is_even(0)
        assert value
        assert isinstance(value, bool)

    def test_is_even_2(self):
        """Test is_even(2)"""
        value = kt1.is_even(2)
        assert value
        assert isinstance(value, bool)

    def test_is_even_5(self):
        """Test is_even(5)"""
        value = kt1.is_even(5)
        assert not value
        assert isinstance(value, bool)

    def test_is_even_m15(self):
        """Test is_even(-15)"""
        value = kt1.is_even(-15)
        assert not value
        assert isinstance(value, bool)


class TestPart52:
    """
    Tests : Fonction lesser
    """

    def test_lesser_0_4(self):
        """Test lesser(0, 4)"""
        value = kt1.lesser(0, 4)
        assert value == 1
        assert isinstance(value, int)

    def test_lesser_m12_3(self):
        """Test lesser(-12, 3)"""
        value = kt1.lesser(-12, 3)
        assert value == 1
        assert isinstance(value, int)

    def test_lesser_m15_m33(self):
        """Test lesser(-15, -33)"""
        value = kt1.lesser(-15, -33)
        assert value == 0
        assert isinstance(value, int)

    def test_lesser_42_42(self):
        """Test lesser(42, 42)"""
        value = kt1.lesser(42, 42)
        assert value == 0
        assert isinstance(value, int)


class TestPart53:
    """
    Tests decide
    """

    def test_decide_0_4_3(self):
        """Test decide(0, 4, 3)"""
        with pytest.raises(ValueError):
            kt1.decide(0, 4, 3)

    def test_decide_2_1_3(self):
        """Test decide(2, 1, 3)"""
        value = kt1.decide(2, 1, 3)
        assert value == 0
        assert isinstance(value, int)

    def test_decide_m12_3_m15(self):
        """Test decide(-2, -15, -12)"""
        value = kt1.decide(-2, -15, -12)
        assert value == 1
        assert isinstance(value, int)

    def test_decide_m15_m33_m12(self):
        """Test decide(-15, -12, 2)"""
        value = kt1.decide(-15, -12, 2)
        assert value == -1
        assert isinstance(value, int)


class TestPart54:
    """
    Tests celsius
    """

    def test_celsius_86_9(self):
        """Test celsius(86.9)"""
        value = kt1.to_celsius(86.9)
        assert value == pytest.approx(30.5)
        assert isinstance(value, float)

    def test_celsius_53_96(self):
        """Test celsius(53.96)"""
        value = kt1.to_celsius(53.96)
        assert value == pytest.approx(12.2)
        assert isinstance(value, float)

    def test_celsius_26_276(self):
        """Test celsius(26.276)"""
        value = kt1.to_celsius(26.276)
        assert value == pytest.approx(-3.18)
        assert isinstance(value, float)


class TestPart55:
    """
    Tests farenheit
    """

    def test_farenheit_30_5(self):
        """Test farenheit(30.5)"""
        value = kt1.to_farenheit(30.5)
        assert value == pytest.approx(86.9)
        assert isinstance(value, float)

    def test_farenheit_12_2(self):
        """Test farenheit(12.2)"""
        value = kt1.to_farenheit(12.2)
        assert value == pytest.approx(53.96)
        assert isinstance(value, float)

    def test_farenheit_m3_18(self):
        """Test farenheit(-3.18)"""
        value = kt1.to_farenheit(-3.18)
        assert value == pytest.approx(26.276)
        assert isinstance(value, float)
