from dearpygui.dearpygui import window, menu_bar, add_menu_item, menu, configure_item, add_button, add_input_text, \
    add_input_int, add_same_line, add_separator

from windows.option_window import debug_callback


def create_main_window():
    with window(id=1, label="main"):
        # core.add_checkbox(name="test123", label="Radio Button", default_value=False, callback=debug_callback)
        add_input_text(id=10, label="key", hint='Please enter a key word', width=200)
        add_same_line()
        add_input_int(id=11, label="Strings up", width=100)
        add_same_line()
        add_input_int(id=12, label="Strings down",  width=100)
        add_separator(parent=1)
        #add_button(label="Apply filter", callback=debug_callback, user_data=lambda a=str: a)

        with menu_bar(parent=1):
            with menu(label="File"):
                add_menu_item(label="Options",
                              callback=lambda: configure_item(2, show=True))
            with menu(label="Options"):
                add_menu_item(label="Bla",
                              callback=lambda: configure_item(2, show=True))
