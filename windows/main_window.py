from dearpygui.dearpygui import window, menu_bar, add_menu_item, menu, configure_item


def create_main_window(width: int, height: int):
    with window(id=1, label="main"):
        # core.add_checkbox(name="test123", label="Radio Button", default_value=False, callback=debug_callback)

        with menu_bar(parent=1):
            with menu(label="File"):
                add_menu_item(label="Options",
                              callback=lambda: configure_item(2, show=True))
            with menu(label="Options"):
                add_menu_item(label="Bla",
                              callback=lambda: configure_item(2, show=True))
