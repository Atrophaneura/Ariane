
from gi.repository import Gtk, Adw, Gio

from .constants import rootdir, app_id


@Gtk.Template(resource_path=f'{rootdir}/ui/add_row.ui')
class ArianeAddRow(Adw.PreferencesPage):
    __gtype_name__ = 'ArianeAddRow'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    