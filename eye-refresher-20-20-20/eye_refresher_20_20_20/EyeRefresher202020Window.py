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
from gi.repository import Gtk, GLib # pylint: disable=E0611
import logging
logger = logging.getLogger('eye_refresher_20_20_20')

from eye_refresher_20_20_20_lib import Window
from eye_refresher_20_20_20.AboutEyeRefresher202020Dialog import AboutEyeRefresher202020Dialog
from eye_refresher_20_20_20.PreferencesEyeRefresher202020Dialog import PreferencesEyeRefresher202020Dialog
# See eye_refresher_20_20_20_lib.Window.py for more details about how this class works


class EyeRefresher202020Window(Window):
    __gtype_name__ = "EyeRefresher202020Window"

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(EyeRefresher202020Window, self).finish_initializing(builder)
        self.builder = builder
        self.builder.connect_signals(self)

        self.AboutDialog = AboutEyeRefresher202020Dialog
        self.PreferencesDialog = PreferencesEyeRefresher202020Dialog
        self.timer_label = builder.get_object('20_20_20')
        # Code for other initialization actions should be added here.

    def activate_by_default(self):
        self.visiblewindow = self.builder.get_object('visiblewindow')
        self.visiblewindow.show()

    def timer(self):
        for sec in range(21):
            # calling setlabel function with 'sec' time delayed
            second = '0'+ str(sec) if sec < 10 else str(sec)
            GLib.timeout_add_seconds(sec, self.timer_label.set_label, '20 : 20 : '+ second)
                 
    def close_all(self):
         self.visiblewindow.hide()
         Gtk.main_quit()






