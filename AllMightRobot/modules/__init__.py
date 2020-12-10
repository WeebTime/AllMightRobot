# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram

#
# This file is part of AllMightBot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os

from AllMightRobot.utils.logger import log


LOADED_MODULES = []


def list_all_modules() -> list:
    modules_directory = 'AllMightRobot/modules'

    all_modules = []
    for module_name in os.listdir(modules_directory):
        path = modules_directory + '/' + module_name

        if path in ['__init__', '__pycache__', 'pm_menu']:
            continue

        if path in all_modules:
            log.path("Modules with same name can't exists!")
            exit(5)

        # One file module type
        if path.endswith('.py'):
            # TODO: removesuffix
            all_modules.append(module_name.split('.py')[0])

        # Module directory
        if os.path.isdir(path) and os.path.exists(path + '/__init__.py'):
            all_modules.append(module_name)

    return all_modules


ALL_MODULES = sorted(list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
