# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2014 <Arulalan.T>  <arulalant@gmail.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from locale import gettext as _

import logging
logger = logging.getLogger('eye_refresher_20_20_20')

from eye_refresher_20_20_20_lib.AboutDialog import AboutDialog

# See eye_refresher_20_20_20_lib.AboutDialog.py for more details about how this class works.
class AboutEyeRefresher202020Dialog(AboutDialog):
    __gtype_name__ = "AboutEyeRefresher202020Dialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutEyeRefresher202020Dialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

