# Topydo - A todo.txt client written in Python.
# Copyright (C) 2014 Bram Schoenmakers <me@bramschoenmakers.nl>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from Config import config

class ConfigTest(unittest.TestCase):
    def test_config1(self):
        self.assertEquals(config("data/config1").default_action(), 'do')

    def test_config2(self):
        self.assertNotEquals(config("").default_action(), 'do')

    def test_config3(self):
        self.assertTrue(config("data/config2").ignore_weekends())