from gi.repository import Gtk, Adw
from .constants import rootdir
@Gtk.Template(resource_path=f"{rootdir}/ui/show_row.ui")
class DesktopCreatorShowRow(Adw.ActionRow):
    __gtype_name__ = "DesktopCreatorShowRow"
    
    
    suffix_button = Gtk.Template.Child()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.suffix_button.connect("clicked", self.on_suffix_button_clicked)
        
    def on_suffix_button_clicked(self, widget, _):
        self.destroy()