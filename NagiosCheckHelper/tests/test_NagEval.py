from unittest import TestCase

from NagiosCheckHelper import NagErrors, NagEval

class TestNagEval_evalEnumList(TestCase):

    def test_default(self):
        eo = NagErrors()
        ev = NagEval(eo)

        ev.evalEnumList(['Junk'], unknownValueStatus='OK')
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnumList(['Junk'], unknownValueStatus='WARNING')
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnumList(['Junk'], unknownValueStatus='CRITICAL')
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnumList(['Junk'], unknownValueStatus='UNKNOWN')
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)

    def test_bin_value(self):
        eo = NagErrors()
        ev = NagEval(eo)

        ev.evalEnumList(['OKVal'], okValues=['OKVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnumList(['WarningVal'], warningValues=['WarningVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnumList(['CriticalVal'], criticalValues=['CriticalVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnumList(['UnknownVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)

        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList(['OKVal'], okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnumList(['WarningVal'], okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnumList(['CriticalVal'], okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnumList(['UnknownVal'], okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)
    
    def test_bin_valuelist(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList(['OKVal', 'OKVal', 'WarningVal', 'WarningVal', 'CriticalVal'], okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 2)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
    
    def test_unknownValues(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList(['junkVal'], unknownValueStatus="OK")
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnumList(['junkVal'], unknownValueStatus="WARNING")
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnumList(['junkVal'], unknownValueStatus="CRITICAL")
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnumList(['junkVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)

    def test_emptyList(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList([], emptyStatus="OK")
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)
        ev.evalEnumList([], emptyStatus="WARNING")
        self.assertEqual(eo.warning[0], "list is Empty")
        self.assertEqual(eo.getExitCode(), 1)
    
    def test_string(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList('WarningVal', warningValues=['WarningVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.warning[0], "value is WarningVal")
        self.assertEqual(eo.getExitCode(), 1)

    def test_prefixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList(['Warning'], warningValues=['Warning'], prefixText="Test ")
        self.assertEqual(eo.warning[0], "Test value is Warning")

    def test_postfixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnumList(['Warning'], warningValues=['Warning'], postfixText=" String")
        self.assertEqual(eo.warning[0], "value is Warning String")


class TestNagEval_evalEnum(TestCase):

    def test_default(self):
        eo = NagErrors()
        ev = NagEval(eo)

        ev.evalEnum('Junk', defaultStatus='OK')
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnum('Junk', defaultStatus='WARNING')
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnum('Junk', defaultStatus='CRITICAL')
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnum('Junk', defaultStatus='UNKNOWN')
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)

    def test_bin_value(self):
        eo = NagErrors()
        ev = NagEval(eo)

        ev.evalEnum('OKVal', okValues=['OKVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnum('WarningVal', warningValues=['WarningVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnum('CriticalVal', criticalValues=['CriticalVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnum('UnknownVal', unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)

        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnum('OKVal', okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 0)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 0)

        ev.evalEnum('WarningVal', okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 0)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 1)
        
        ev.evalEnum('CriticalVal', okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 0)
        self.assertEqual(eo.getExitCode(), 2)
        
        ev.evalEnum('UnknownVal', okValues=['OKVal'], warningValues=['WarningVal'], criticalValues=['CriticalVal'], unknownValues=['UnknownVal'])
        self.assertEqual(len(eo.critical), 1)
        self.assertEqual(len(eo.warning), 1)
        self.assertEqual(len(eo.unknown), 1)
        self.assertEqual(eo.getExitCode(), 3)

    def test_prefixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnum('Warning', warningValues=['Warning'], prefixText="Test ")
        self.assertEqual(eo.warning[0], "Test value is Warning")

    def test_postfixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalEnum('Warning', warningValues=['Warning'], postfixText=" String")
        self.assertEqual(eo.warning[0], "value is Warning String")


class TestNagEval_evalNumberAsc(TestCase):

    def test_low(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(20, warningAbove=40, criticalAbove=50)
        self.assertEqual(eo.getExitCode(), 0)
    
    def test_mid(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(45, warningAbove=40, criticalAbove=50)
        self.assertEqual(eo.getExitCode(), 1)

    def test_high(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(55, warningAbove=40, criticalAbove=50)
        self.assertEqual(eo.getExitCode(), 2)

    def test_negative_low(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(-20, warningAbove=-10, criticalAbove=-5)
        self.assertEqual(eo.getExitCode(), 0)
    
    def test_negative_mid(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(-8, warningAbove=-10, criticalAbove=-5)
        self.assertEqual(eo.getExitCode(), 1)
    
    def test_negative_high(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(-3, warningAbove=-10, criticalAbove=-5)
        self.assertEqual(eo.getExitCode(), 2)

    def test_swappedTresholds(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(51, warningAbove=50, criticalAbove=40)
        self.assertEqual(eo.getExitCode(), 2)

    def test_numberUnits(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(45, warningAbove=40, numberUnits="sec")
        self.assertEqual(eo.warning[0], "45sec is > 40sec")

    def test_prefixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(45, warningAbove=40, prefixText="Test ")
        self.assertEqual(eo.warning[0], "Test 45 is > 40")

    def test_prefixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberAsc(45, warningAbove=40, postfixText=" Units")
        self.assertEqual(eo.warning[0], "45 is > 40 Units")


class TestNagEval_evalNumberDesc(TestCase):

    def test_low(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(20, warningBelow=50, criticalBelow=40)
        self.assertEqual(eo.getExitCode(), 2)
    
    def test_mid(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(45, warningBelow=50, criticalBelow=40)
        self.assertEqual(eo.getExitCode(), 1)

    def test_high(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(55, warningBelow=50, criticalBelow=40)
        self.assertEqual(eo.getExitCode(), 0)

    def test_negative_low(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(-20, warningBelow=-5, criticalBelow=-10)
        self.assertEqual(eo.getExitCode(), 2)
    
    def test_negative_mid(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(-8, warningBelow=-5, criticalBelow=-10)
        self.assertEqual(eo.getExitCode(), 1)
    
    def test_negative_high(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(-3, warningBelow=-5, criticalBelow=-10)
        self.assertEqual(eo.getExitCode(), 0)

    def test_swappedTresholds(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(21, warningBelow=50, criticalBelow=40)
        self.assertEqual(eo.getExitCode(), 2)

    def test_numberUnits(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(45, warningBelow=50, numberUnits="sec")
        self.assertEqual(eo.warning[0], "45sec is < 50sec")

    def test_prefixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(45, warningBelow=50, prefixText="Test ")
        self.assertEqual(eo.warning[0], "Test 45 is < 50")

    def test_prefixText(self):
        eo = NagErrors()
        ev = NagEval(eo)
        ev.evalNumberDesc(45, warningBelow=50, postfixText=" Units")
        self.assertEqual(eo.warning[0], "45 is < 50 Units")

















