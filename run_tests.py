import unittest
suite = unittest.defaultTestLoader.loadTestsFromName('tests.test_browser_profile_selection')
result = unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():
    raise SystemExit(1)
