#!C:\Aaditya_ML\Family_tree\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'neo4j==4.1.1','console_scripts','pybolt'
__requires__ = 'neo4j==4.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('neo4j==4.1.1', 'console_scripts', 'pybolt')()
    )
