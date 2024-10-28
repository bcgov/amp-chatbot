"""
    BC-ISDBI.unittests.test_module

    Unittests for the BC-ISDBI Database Package
"""
import unittest

from helloworld.main import main


# pylint: disable=missing-docstring
class TestApps(unittest.TestCase):
    """Test BC-ISDBI LDAP support"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main(self):
        self.assertIsNone(main())
