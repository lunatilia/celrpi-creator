#
# Copyright (C) 2019 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# --
# Origin: Red Hat, Inc.
# Modified by: Mitsuki Shirase <https://github.com/lunatilia>

import os

from pyanaconda.modules.storage.bootloader.base import BootLoader, BootLoaderArguments,\
    BootLoaderError
from pyanaconda.core import util
from pyanaconda.core.configuration.anaconda import conf
from pyanaconda.product import productName

from pyanaconda.anaconda_loggers import get_module_logger
log = get_module_logger(__name__)

__all__ = ["Aarch64RPI"]


class Aarch64RPI(BootLoader):
    name = "Aarch64RPI"

    stage2_format_types = ["vfat"]
    stage2_device_types = ["partition"]
#    packages = ["raspi-firmware"]

    @property
    def config_file(self):
        return None

    @property
    def boot_prefix(self):
        return None

    def write_config_console(self, config):
        return NotImplemented

    def write_config_images(self, config):
        return NotImplemented

    def install(self, args=None):
        return NotImplemented

