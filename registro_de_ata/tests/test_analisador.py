import unittest
from src.domains import AnalisadorDePresenca


class TestAnalisador(unittest.TestCase):

    def test_ColaboradoresQueViram2WorkshopsSeguidos1(self):
        test1 = AnalisadorDePresenca(['hbas ies', 'alco2 hbas', 'pot alco2 hbas'])
        self.assertEqual(test1.ColaboradoresQueViram2WorkshopsSeguidos(), ['alco2', 'hbas'])

    def test_ColaboradoresQueViram2WorkshopsSeguidos2(self):
        test2 = AnalisadorDePresenca(['hbas ies alco', 'alco hbas tst gkmo', 'pot aacs alco aaosc fgrr',
                                      'till ies alco2 tst gkmo hbas'])
        self.assertEqual(test2.ColaboradoresQueViram2WorkshopsSeguidos(), ['alco', 'hbas'])

    def test_ColaboradoresQueViram2WorkshopsSeguidos3(self):
        test3 = AnalisadorDePresenca(['hbas ies', '', 'alco hbas gkmo'])
        self.assertEqual(test3.ColaboradoresQueViram2WorkshopsSeguidos(), [])

    def test_ColaboradoresQueViram2WorkshopsSeguidos4(self):
        test4 = AnalisadorDePresenca([])
        self.assertEqual(test4.ColaboradoresQueViram2WorkshopsSeguidos(), [])

    def test_ColaboradoresQueViram2WorkshopsSeguidos5(self):
        test5 = AnalisadorDePresenca(['hbas ies', 'hbas ies'])
        self.assertEqual(test5.ColaboradoresQueViram2WorkshopsSeguidos(), ['hbas', 'ies'])


if __name__ == '__name__':
    unittest.main()
