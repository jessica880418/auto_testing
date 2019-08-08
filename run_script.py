import unittest
import carCompany.simpleAndroidTests
import carCustomer.simpleAndroidTests



if __name__ == '__main__':
    # unittest.TestLoader.loadTestsFromName("SimpleAndroidTests")
    carCompanyTests = unittest.TestLoader().loadTestsFromModule(carCompany.simpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(carCompanyTests)
    carCustomerTests = unittest.TestLoader().loadTestsFromModule(carCustomer.simpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(carCustomerTests)
