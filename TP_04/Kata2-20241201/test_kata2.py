"""
KATA 2 TESTS
"""

import pytest

kt2 = pytest.importorskip("kata2")


class TestPart1:
    """
    Tests part 1
    """

    def test_name1(self):
        """Test name1"""
        assert kt2.name1 == "happiness"
        assert isinstance(kt2.name1, str)

    def test_name2(self):
        """Test name2"""
        assert kt2.name2
        assert isinstance(kt2.name2, bool)

    def test_name3(self):
        """Test name3"""
        assert kt2.name3
        assert isinstance(kt2.name3, bool)

    def test_name4(self):
        """Test name4"""
        assert kt2.name4 == "ness"
        assert isinstance(kt2.name4, str)

    def test_name5(self):
        """Test name5"""
        assert kt2.name5 == "happi"
        assert isinstance(kt2.name5, str)

    def test_name6(self):
        """Test name6"""
        assert kt2.name6 == "happy"
        assert isinstance(kt2.name6, str)

    def test_name7(self):
        """Test name7"""
        assert kt2.name7 == 9
        assert isinstance(kt2.name7, int)

    def test_name8(self):
        """Test name8"""
        assert kt2.name8 == "pin"
        assert isinstance(kt2.name8, str)

    def test_name9(self):
        """Test name9"""
        assert kt2.name9 == 1
        assert isinstance(kt2.name9, int)

    def test_extraname(self):
        """Test extraname"""
        assert kt2.extraname == "Supercalifragilisticexpialidocious"
        assert isinstance(kt2.extraname, str)

    def test_revextra(self):
        """Test revextra"""
        assert kt2.revextra == "suoicodilaipxecitsiligarfilacrepuS"
        assert isinstance(kt2.revextra, str)

class TestPart2:
    """
    Tests part 2
    """

    def test_name10(self):
        """Test name10"""
        assert kt2.name10 == 10
        assert isinstance(kt2.name10, int)

    def test_name11(self):
        """Test name11"""
        assert kt2.name11 == 56
        assert isinstance(kt2.name11, int)

    def test_name12(self):
        """Test name12"""
        assert kt2.name12 == pytest.approx(2065.5)
        assert isinstance(kt2.name12, float)

    def test_name13(self):
        """Test name13"""
        assert kt2.name13(7) == pytest.approx(52.5)
        assert kt2.name13(12) == pytest.approx(135)
        assert kt2.name13(50) == pytest.approx(1987.5)
        assert callable(kt2.name13)
    
    def test_name14(self):
        """Test name14"""
        assert kt2.name14 == 56
        assert isinstance(kt2.name14, int)
    
    def test_name15(self):
        """Test name15"""
        assert kt2.name15 == 56
        assert isinstance(kt2.name15, int)

    def test_name16(self):
        """Test name16"""
        assert kt2.name16 == 1048576
        assert isinstance(kt2.name16, int)

    def test_name17(self):
        """Test name17"""
        assert kt2.name17 == 1684
        assert isinstance(kt2.name17, int)

class TestPart3:
    """
    Tests part 3
    """

    def test_name18(self):
        """Test name18"""
        assert kt2.name18 == "0123456789"
        assert isinstance(kt2.name18, str)

    def test_name19(self):
        """Test name19"""
        assert kt2.name19 == "0123456789"
        assert isinstance(kt2.name19, str)
    
    def test_name20(self):
        """Test name20"""
        assert kt2.name20 == "0123456789"
        assert isinstance(kt2.name20, str)

    def test_name21(self):
        """Test name21"""
        assert not kt2.name21
        assert isinstance(kt2.name21, bool)
    
    def test_name22(self):
        """Test name22"""
        assert kt2.name22 == "122333444455555"
        assert isinstance(kt2.name22, str)

    def test_name23(self):
        """Test name23"""
        assert kt2.name23 == "12345"
        assert isinstance(kt2.name23, str)
        
    def test_name24(self):
        """Test name24"""
        assert kt2.name24 == 7
        assert isinstance(kt2.name24, int)
    
    def test_name25(self):
        """Test name25"""
        assert kt2.name25 == 7
        assert isinstance(kt2.name25, int)

class TestPart41:
    """
    Tests part 4.1
    """
    def test_isdna_empty(self):
        """Test is_dna("")"""
        answer = kt2.is_dna("")
        assert answer
        assert isinstance(answer, bool)
    def test_isdna_atcg(self):
        """Test is_dna("ATCTCGACTCG")"""
        answer = kt2.is_dna("ATCTCGACTCG")
        assert answer
        assert isinstance(answer, bool)
    def test_isdnas_atng(self):
        """Test is_dna("ATNG")"""
        answer = kt2.is_dna("ATNG")
        assert not answer
        assert isinstance(answer, bool)

class TestPart42:
    """
    Tests part 4.2
    """
    def test_dna2rna_empty(self):
        """test empty seq"""
        assert kt2.dna2rna("") == ""
        assert isinstance(kt2.dna2rna(""), str)
    def test_dna2rna_1(self):
        """test dummy seq"""
        answer = kt2.dna2rna("ATGAGAGTATCCGCAGGTCGGGTA")
        assert answer == "AUGAGAGUAUCCGCAGGUCGGGUA"
        assert isinstance(answer, str)
    def test_dna2rna_2(self):
        """test small seq"""
        assert kt2.dna2rna("TGC") == "UGC"
        assert isinstance(kt2.dna2rna("TGC"), str)


class TestPart43:
    """
    Test part 4.3
    """
    def test_rev_comp_empty(self):
        """test empty seq"""
        assert kt2.rev_comp("") == ""
    def test_rev_comp_1(self):
        """test seq"""
        assert kt2.rev_comp("ATGCTACG") == "CGTAGCAT"
    def test_rev_comp_2(self):
        """test small seq"""
        assert kt2.rev_comp("ATG") == "CAT"
