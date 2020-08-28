# Copyright (C) 2018 - 2020 MrYacha.
# Copyright (C) 2020 Jeepeo.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of Sophie.

from typing import List

from pathlib import Path

from sophie.utils.config import config
from sophie.utils.logging import log
from .package import Package


def load_modules(to_load: List[str]) -> list:
    from . import LOADED_MODULES

    modules: list = []
    for module_name in to_load:
        module = Package(
            type='module',
            name=module_name,
            path=Path(f"sophie/modules/{module_name}")
        )
        LOADED_MODULES[module_name] = module
        modules.append(module)

    return modules


def load_all_modules() -> list:
    from sophie.modules import ALL_MODULES

    load = config.module.load
    dont_load = config.module.dont_load

    if len(load) > 0:
        to_load = load
    else:
        to_load = ALL_MODULES

    to_load = [x for x in to_load if x not in dont_load]
    log.info("Modules to load: %s", str(to_load))
    load_modules(to_load)

    return to_load