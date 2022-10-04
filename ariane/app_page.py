
from ast import Gt
from gi.repository import Gtk, Adw, Gio

from .constants import rootdir, app_id


@Gtk.Template(resource_path=f'{rootdir}/ui/app_page.ui')
class ArianeAppPage(Adw.PreferencesPage):
    __gtype_name__ = 'ArianeAppPage'

    generic_name = Gtk.Template.Child()
    name = Gtk.Template.Child()
    comment = Gtk.Template.Child()
    icon = Gtk.Template.Child()
    exec_entry = Gtk.Template.Child("exec")
    try_exec = Gtk.Template.Child()
    working_dir = Gtk.Template.Child()
    
    hidden_switch = Gtk.Template.Child()
    run_in_terminal_switch = Gtk.Template.Child()
    use_startup_notification_switch = Gtk.Template.Child()
    hide_from_menus_switch = Gtk.Template.Child()
    dbus_activatable_switch = Gtk.Template.Child()
    
    categories = Gtk.Template.Child()
    empty_category = Gtk.Template.Child()
    
    actions = Gtk.Template.Child()
    empty_action = Gtk.Template.Child()
    
    only_show_in = Gtk.Template.Child()
    empty_desktop_environment_not = Gtk.Template.Child()
    
    not_show_in = Gtk.Template.Child()
    empty_desktop_environment_only = Gtk.Template.Child()
    
    mimetypes = Gtk.Template.Child()
    empty_mimetypes = Gtk.Template.Child()
    
    keywords = Gtk.Template.Child()
    empty_keywords = Gtk.Template.Child()
    
    implements = Gtk.Template.Child()
    empty_dbus = Gtk.Template.Child()
    
    settings = Gio.Settings(app_id)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

