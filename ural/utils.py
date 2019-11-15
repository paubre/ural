# =============================================================================
# Ural Various Utilities
# =============================================================================
#
# Miscellaneous utilities used throughout the library's code.
#

# PY2/PY3 compatible string_type...
string_type = str

try:
    string_type = basestring
except NameError:
    pass