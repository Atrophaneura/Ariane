from gi.repository import Gtk, Adw

from .constants import (
    rootdir,
    app_id,
    rel_ver,
    version,
    bugtracker_url,
    help_url,
    project_url,
)
class AboutDialog(Adw.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.application_name = _('Desktop Creator')
        self.props.version = version
        self.props.application_icon=app_id,
        self.props.developer_name=_("Desktop Creator Team"),
        self.props.website=project_url,
        self.props.support_url=help_url,
        self.props.issue_url=bugtracker_url,
        self.props.developers=[
            "0xMRTT https://github.com/0xMRTT",
        ],
        self.props.artists=["Angelo Verlain https://gitlab.gnome.org/vixalien"],
        self.props.designers=["Angelo Verlain https://gitlab.gnome.org/vixalien"],
        # Translators: This is a place to put your credits (formats: "Name
        # https://example.com" or "Name <email@example.com>", no quotes)
        # and is not meant to be translated literally.
        # TODO: Automate this process using CI, because not everyone knows
        # about this
        self.props.translator_credits="""
            0xMRTT https://github.com/0xMRTT
            """,
        self.props.copyright="© 2022 Gradience Team",
        self.props.license_type=Gtk.License.GPL_3_0,
        self.props.version=version,
        self.props.release_notes_version=rel_ver,
        
        
        self.props.logo_icon_name = app_id
        self.props.modal = True
        self.set_transient_for(parent)
