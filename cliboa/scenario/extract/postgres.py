#
# Copyright BrainPad Inc. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
from cliboa.adapter.postgres import PostgresqlAdaptor
from cliboa.scenario.rdbms import BaseRdbmsRead


class PostgresqlRead(BaseRdbmsRead):
    def __init__(self):
        super().__init__()

    def get_adaptor(self):
        return PostgresqlAdaptor(self._host, self._user, self._password, self._dbname, self._port)
