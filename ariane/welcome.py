import sys
import time

from gi.repository import Gtk, Adw, Gio

from .constants import rootdir, app_id, version


@Gtk.Template(resource_path=f"{rootdir}/ui/welcome.ui")
class WelcomeWindow(Adw.Window):
    __gtype_name__ = "WelcomeWindow"

    settings = Gtk.Settings.get_default()

    carousel = Gtk.Template.Child()

    btn_close = Gtk.Template.Child()
    btn_back = Gtk.Template.Child()
    btn_next = Gtk.Template.Child()
    
    img_welcome = Gtk.Template.Child()

    images = [
        f"{rootdir}/images/welcome.svg",
        f"{rootdir}/images/welcome-dark.svg",
    ]

    carousel_pages = [
        "welcome",  # 0
        "release",  # 1
        "ariane",  # 2
        "finish",  # 4
    ]

    page_welcome = Gtk.Template.Child()
    page_release = Gtk.Template.Child()

    def __init__(self, window, update=False, **kwargs) -> None:
        super().__init__(**kwargs)
        self.set_transient_for(window)
        self.update = update

        # common variables and references
        self.window = window

        self.gio_settings = Gio.Settings(app_id)

        # connect signals
        self.connect("close-request", self.quit)
        self.carousel.connect("page-changed", self.page_changed)
        self.btn_close.connect("clicked", self.close_window)
        self.btn_back.connect("clicked", self.previous_page)
        self.btn_next.connect("clicked", self.next_page)

        self.settings.connect(
            "notify::gtk-application-prefer-dark-theme", self.theme_changed
        )

        if self.update:
            self.page_welcome.set_title(_("Thanks for updating Ariane!"))

        self.page_release.set_title(f"Ariane {version}")

        if self.settings.get_property("gtk-application-prefer-dark-theme"):
            self.img_welcome.set_from_resource(self.images[1])

        self.page_changed()

    def theme_changed(self, settings, key):
        self.img_welcome.set_from_resource(
            self.images[settings.get_property(
                "gtk-application-prefer-dark-theme")]
        )

    def get_page(self, index):
        return self.carousel_pages[index]

    def page_changed(self, widget=False, index=0, *_args):
        """
        This function is called on first load and when the user require
        to change the page. It sets the widgets' status according to
        the step of the onboard progress.
        """
        page = self.get_page(index)

        if page == "finish":
            self.btn_back.set_visible(False)
            self.btn_next.set_visible(False)
        elif page == "welcome":
            self.btn_back.set_visible(False)
            self.btn_next.set_visible(True)
        else:
            self.btn_back.set_visible(True)
            self.btn_next.set_visible(True)

    @staticmethod
    def quit(widget=False):
        sys.exit()

    def previous_page(self, widget=False, index=None):
        if index is None:
            index = int(self.carousel.get_position())
        previous_page = self.carousel.get_nth_page(index - 1)
        self.carousel.scroll_to(previous_page, True)

    def next_page(self, widget=False, index=None):
        if index is None:
            index = int(self.carousel.get_position())
        next_page = self.carousel.get_nth_page(index + 1)
        self.carousel.scroll_to(next_page, True)

    def close_window(self, widget):
        self.destroy()
        self.window.present()
