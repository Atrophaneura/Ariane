# main.py
#
# Copyright 2022 0xMRTT
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

from .constants import (
    rootdir,
    app_id,
    rel_ver,
    version,
    bugtracker_url,
    help_url,
    project_url,
)
from .window import ArianeWindow
from gi.repository import Gtk, Gio, Adw
import sys
import gi

from desktop_parser import DesktopFile


from .welcome import WelcomeWindow

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')


class ArianeApplication(Adw.Application):
    """The main application singleton class."""

    settings = Gio.Settings.new(app_id)
    desktop = DesktopFile()

    def __init__(self):
        super().__init__(application_id=app_id,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action('about', self.show_about_window)
        self.create_action('preferences', self.on_preferences_action)
        self.create_action('new', self.on_new_action)
        self.create_action('save', self.on_save_action)
        self.create_action('open', self.on_open_action)
        
        self.first_run = self.settings.get_boolean("first-run")
        self.last_opened_version = self.settings.get_string(
            "last-opened-version")

    def on_new_action(self, widget, _):
        print('app.new action activated')

    def on_save_action(self, widget, _):
        """Callback for the app.save action."""
        self.desktop.data["Desktop Entry"] = {}
        if self.win.generic_name.get_text():
            self.desktop.data["Desktop Entry"]["GenericName"] = self.win.generic_name.get_text(
            )
        if self.win.name.get_text():
            self.desktop.data["Desktop Entry"]["Name"] = self.win.name.get_text()
        else:
            self.win.name.set_css_classes(["error"])
            return
        if self.win.comment.get_text():
            self.desktop.data["Desktop Entry"]["Comment"] = self.win.comment.get_text(
            )
        if self.win.exec_entry.get_text():
            self.desktop.data["Desktop Entry"]["Exec"] = self.win.exec_entry.get_text(
            )
        if self.win.icon.get_text():
            self.desktop.data["Desktop Entry"]["Icon"] = self.win.icon.get_text()
        if self.win.try_exec.get_text():
            self.desktop.data["Desktop Entry"]["TryExec"] = self.win.try_exec.get_text(
            )
        if self.win.working_dir.get_text():
            self.desktop.data["Desktop Entry"]["WorkingDir"] = self.win.working_dir.get_text(
            )
        self.desktop.data["Desktop Entry"]["Hidden"] = self.win.hidden_switch.get_active(
        )
        self.desktop.data["Desktop Entry"]["Terminal"] = self.win.run_in_terminal_switch.get_active()
        self.desktop.data["Desktop Entry"]["StartupNotify"] = self.win.use_startup_notification_switch.get_active()
        self.desktop.data["Desktop Entry"]["DBusActivatable"] = self.win.dbus_activatable_switch.get_active()
        self.desktop.data["Desktop Entry"]["NoDisplay"] = self.win.hide_from_menus_switch.get_active()

        self.desktop.dump('test.desktop')

    def on_open_action(self, widget, _):
        pass

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        self.win = self.props.active_window
        if not self.win:
            self.win = ArianeWindow(application=self,
                                   default_height=self.settings.get_int(
                                       "window-height"),
                                   default_width=self.settings.get_int(
                                       "window-width"),
                                   fullscreened=self.settings.get_boolean(
                                       "window-fullscreen"),
                                   maximized=self.settings.get_boolean("window-maximized"),)
        win.present()
        if version != self.last_opened_version:
            welcome = WelcomeWindow(self.win, update=True)
            welcome.present()
        elif self.first_run:
            welcome = WelcomeWindow(self.win)
            welcome.present()
        else:
            self.win.present()
        self.win.present()

    def show_about_window(self, *_args):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name=_("Ariane"),
            application_icon=app_id,
            developer_name=_("Ariane Team"),
            website=project_url,
            support_url=help_url,
            issue_url=bugtracker_url,
            developers=["0xMRTT https://github.com/0xMRTT", ],
            artists=[""],
            designers=["Angelo Verlain  https://gitlab.gnome.org/vixalien"],
            # Translators: This is a place to put your credits (formats: "Name
            # https://example.com" or "Name <email@example.com>", no quotes)
            # and is not meant to be translated literally.
            # TODO: Automate this process using CI, because not everyone knows
            # about this
            translator_credits=["0xMRTT https://github.com/0xMRTT"],
            copyright="© 2022 Ariane Team",
            license_type=Gtk.License.GPL_3_0,
            version=version,
            release_notes_version=rel_ver,
            # release_notes=_(
            #     """
            # """
            # )
        )
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main():
    """The application's entry point."""
    app = ArianeApplication()
    return app.run(sys.argv)
