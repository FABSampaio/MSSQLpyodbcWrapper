# MSSQLpyWrapper

This package is a wrapper for the pyodbc package intended to
simplify the connection to and querying of local (on the
host machine) MSSQL databases. 

Instead of using the habitual pyodbc classes, the MSSQLWrapper
class limits user input to some extent, in exchange for simplicity
and clarity of use. The user simply instantiates an object by
providing its constructor with the SERVER and the DATABASE.
Queries are performed by calling one of the two types of
methods: safe or unsafe queries, which take as few as one or
two arguments.

This package is highly subject to change. New features may be
added and/or existing ones removed.

Francisco A. B. Sampaio, INEGI, 2021