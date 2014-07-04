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

import optparse
from locale import gettext as _
from gi.repository import Gtk, GLib # pylint: disable=E0611
from eye_refresher_20_20_20 import EyeRefresher202020Window
from eye_refresher_20_20_20_lib import set_up_logging, get_version


def parse_options():
    """Support for command line options"""
    parser = optparse.OptionParser(version="%%prog %s" % get_version())
    parser.add_option(
        "-v", "--verbose", action="count", dest="verbose",
        help=_("Show debug messages (-vv debugs eye_refresher_20_20_20_lib also)"))
    (options, args) = parser.parse_args()

    set_up_logging(options)

def hideWindows(window):    
    window.visiblewindow.hide()
    window.hide()    
    
def run(window):
    screen = window.get_screen()
    no_of_monitors = screen.get_n_monitors()
    # return without running if more than one monitor connected (say projector)
    if no_of_monitors > 1: return 
    # Run the application.
    window.show()  
    window.activate_by_default()
    # initial set 1 sec time delay to start counter/timer
    GLib.timeout_add_seconds(2, window.timer)    
    # hide gui after 22 seconds 
    GLib.timeout_add_seconds(22, hideWindows, window)
    GLib.timeout_add_seconds(23, Gtk.main_quit)
    Gtk.main()
    
    
def main():
    parse_options()
    # return the main window object with full properties
    window = EyeRefresher202020Window.EyeRefresher202020Window()
    screen = window.get_screen()
    # by default takes first monitor size
    monitor = screen.get_monitor_geometry(0)
    # set window screen size 
    window.set_size_request(monitor.width, monitor.height)    
    # make it as maximized or full screen (by default)
    # during full screen mode, user can not access Edit, Help options
    window.fullscreen()    
    return window


    
    
    
    

