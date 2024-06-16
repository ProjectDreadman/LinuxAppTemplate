import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Linux App Template")
        self.set_default_size(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)

        # Create a box container
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        # Create a menu bar
        self.menu_bar = Gtk.MenuBar()
        self.box.pack_start(self.menu_bar, False, False, 0)

        # Add a menu item
        file_menu = Gtk.Menu()
        file_item = Gtk.MenuItem(label="File")
        file_item.set_submenu(file_menu)

        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", Gtk.main_quit)
        file_menu.append(quit_item)

        self.menu_bar.append(file_item)

        # Add an image
        self.image = Gtk.Image()
        self.image.set_from_file("icons/app-icon.png")
        self.box.pack_start(self.image, True, True, 0)

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
