# Francisco A. B. Sampaio, Portugal, 2021
import pytest
from src.mssql_pyodbc_wrapper.mssqlwrapper import MSSQLWrapper, build_simple_query_string, QueryTypeError

SELECT_QUERY = '''SELECT [col1], [col2], [col3] FROM [dbo].[pyetl_TestTable];'''
INSERT_QUERY = '''INSERT INTO [dbo].[pyetl_TestTable] ([col1], [col2], [col3]) VALUES (?, ?, ?);'''


@pytest.fixture
def wrapper_fixture() -> MSSQLWrapper:
    _server_name = 'FSAMPAIO\\SQLEXPRESS'
    _database = 'DWDiagnostics'

    return MSSQLWrapper.from_localdb(_server_name, _database)


class TestMSSQLWrapper:
    def test_constructor(self, wrapper_fixture):
        assert wrapper_fixture.server == 'FSAMPAIO\\SQLEXPRESS'
        assert wrapper_fixture.database == 'DWDiagnostics'

    def test_build_select_query_string(self, wrapper_fixture):
        _query_type = 'SELECT'
        _table_name = '[dbo].[pyetl_TestTable]'

        _columns = ['[col1]', '[col2]', '[col3]']

        _sql_query = SELECT_QUERY

        assert build_simple_query_string(_query_type,
                                         _table_name,
                                         _columns) == _sql_query

    def test_build_insert_query_string(self, wrapper_fixture):
        _query_type = 'INSERT'
        _table_name = '[dbo].[pyetl_TestTable]'

        _columns = ['[col1]', '[col2]', '[col3]']

        _sql_query = INSERT_QUERY

        assert build_simple_query_string(_query_type,
                                         _table_name,
                                         _columns) == _sql_query

    def test_build_query_string_exception(self, wrapper_fixture):
        _query_type = "NONEXISTENT_QUERY_TYPE"
        _table_name = ""
        _columns = [""]

        with pytest.raises(QueryTypeError) as exception_info:
            build_simple_query_string(_query_type, _table_name, _columns)

    def test_unsafe_select(self, wrapper_fixture):
        pass

    def test_unsafe_insert(self, wrapper_fixture):
        pass

    def test_safe_select(self, wrapper_fixture):
        pass

    def test_safe_insert(self, wrapper_fixture):
        pass

    def test_sql_query_rejection(self, wrapper_fixture):
        pass
