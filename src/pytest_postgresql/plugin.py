# Copyright (C) 2016 by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).

# This file is part of pytest-postgresql.

# pytest-dbfixtures is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pytest-postgresql is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with pytest-postgresql.  If not, see <http://www.gnu.org/licenses/>.
"""Plugin module of pytest-postgresql."""
from pytest_postgresql import factories


def pytest_addoption(parser):
    """Configure options for pytest-postgresql."""
    parser.addoption(
        '--pgsql-logsdir',
        action='store',
        default='/tmp',
        metavar='path',
        dest='pgsql_logsdir',
    )


postgresql_proc = factories.postgresql_proc()
postgresql = factories.postgresql('postgresql_proc')
