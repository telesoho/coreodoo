# -*- coding: utf-8 -*-

""" Addons module.

This module serves to contain all Odoo addons, across all configured addons
paths. For the code to manage those addons, see odoo.modules.

Addons are made available under `odoo.addons` after
odoo.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from odoo.modules.
Importing them from here is deprecated.

"""
import pkgutil
import os.path

__path__ = [os.path.abspath(path) for path in pkgutil.extend_path(__path__, __name__)]
