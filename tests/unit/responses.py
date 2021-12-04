class Responses:
    input1 = 'WARNING: test123\nERROR: test123\nWARNING: test123\nERROR: test123'
    response1 = ('''TOTAL MATCHES: 2

--------------------
MATCH: string index 2
--------------------
ERROR: test123
WARNING: test123
------------------------------------------------
-> ERROR: test123
------------------------------------------------
WARNING: test123
ERROR: test123

--------------------
MATCH: string index 4
--------------------
ERROR: test123
WARNING: test123
------------------------------------------------
-> ERROR: test123
------------------------------------------------''')
    input2 = ('WARNING: test123\n'
              'WARNING: test123\n'
              'ERROR: test123\n'
              'WARNING: test123\n'
              'ERROR: test123\n'
              'WARNING: test123\n'
              'WARNING: test123')
    response2 = '''TOTAL MATCHES: 2

--------------------
MATCH: string index 3
--------------------
WARNING: test123
WARNING: test123
------------------------------------------------
-> ERROR: test123
------------------------------------------------
WARNING: test123
ERROR: test123

--------------------
MATCH: string index 5
--------------------
ERROR: test123
WARNING: test123
------------------------------------------------
-> ERROR: test123
------------------------------------------------
WARNING: test123
WARNING: test123'''
