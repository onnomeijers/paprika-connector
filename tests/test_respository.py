import unittest
from paprika_connector.connectors.DatasourceBuilder import DatasourceBuilder
from paprika_connector.connectors.ConnectorFactory import ConnectorFactory
from paprika_connector.connectors.Repository import Repository
from paprika_connector.connectors.Helper import Helper


class PropertyRepository(Repository):
    APPLICATION_PROPERTIES_S="application_properties_s"

    def __init__(self, connector):
        Repository.__init__(self, connector)
        self.set_sequence(PropertyRepository.APPLICATION_PROPERTIES_S)

    def get_property(self, key):
        connection = self.get_connection()
        cursor = connection.cursor()
        params = {"name": key}
        statement = "select value from application_properties where name=:name"
        statement, parameters = self.statement(statement, params)
        cursor.execute(statement, parameters)
        results = Helper.cursor_to_json(cursor)
        if len(results) == 0:
            return None
        return results[0]['value']


class TestRepository(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mysql_property_repository(self):
        paprika_ds = DatasourceBuilder.build("paprika-mysql-ds.json")
        connector = ConnectorFactory.create_connector(paprika_ds)
        property_repository = PropertyRepository(connector)
        version = property_repository.get_property('application.version')
        print type(version)
        expected = "1.0.6"
        self.assertEqual(version, expected, "expected " + expected + " got " + str(version))
        connector.close()


if __name__ == '__main__':
    unittest.main()
