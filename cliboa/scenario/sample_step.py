#
# Copyright 2019 BrainPad Inc. All Rights Reserved.
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
import cliboa
from cliboa.scenario.base import BaseStep
from cliboa.util.lisboa_log import LisboaLog


class SampleStep(BaseStep):
    """
    For unit test
    """

    def __init__(self):
        super().__init__()
        self._retry_count = 3
        self._logger = LisboaLog.get_logger(__name__)

    @property
    def retry_count(self):
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        self._retry_count = retry_count

    def execute(self, *args):
        self._logger.info("Start %s" % self.__class__.__name__)
        self._logger.info("Finish %s" % self.__class__.__name__)


class SampleCustomStep(BaseStep):
    """
    For unit test
    """

    def __init__(self):
        BaseStep.__init__(self)
        self._retry_count = 3

    @property
    def retry_count(self):
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        self._retry_count = retry_count

    def execute(self, *args):
        self._logger.info("Start %s" % self.__class__.__name__)
        self._logger.info("Finish %s" % self.__class__.__name__)
