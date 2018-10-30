import unittest


def myadd(x,y):
    return x+y

def mysub(x,y):
    return x-y

class Myrun(unittest.TestCase):
    def testadd(self):
        self.assertEqual(myadd(2,3),5)

    def testasub(self):
        self.assertTrue(print("test sub") == None)
        self.assertTrue(mysub(5, 3) == 3)

    def notest(self):
        print("No test")

    def testnotadd(self):
        return self.assertNotEqual(myadd(4,5),10)

if __name__ == "__main__":
    #unittest.main() # to start testing
    suite = unittest.TestLoader().loadTestsFromTestCase(Myrun)
    unittest.TextTestRunner(verbosity=2).run(suite)
