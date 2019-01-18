import unittest
from paprika_connector.connectors.DatasourceBuilder import DatasourceBuilder


class TestDatasourceBuilder(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mysql_datasource(self):
        paprika_ds = DatasourceBuilder.build("paprika-mysql-ds.json")
        expected = {u'username': u'apps', u'db': u'paprika', u'host': u'localhost', u'password': u'apps', u'type': u'mysql'}
        self.assertEqual(paprika_ds, expected, 'invalid datasource expected ' + str(expected) + " got " + str(paprika_ds))
if __name__ == '__main__':
    unittest.main()
