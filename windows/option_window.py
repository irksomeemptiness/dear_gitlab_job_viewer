from dearpygui.dearpygui import window, add_input_text, add_checkbox, add_button, get_value

OPTIONS = {}


def create_option_window():
    with window(id=2, label="Options", on_close=debug_callback, show=False, autosize=True):
        add_input_text(default_value="zzzzz")
        add_input_text(default_value="zzzzz")
        add_input_text(default_value="zzzzz")
        add_input_text(default_value="zzzzz")
        add_checkbox(label="Radio Button", default_value=False,
                     callback=debug_callback)
        add_checkbox(label="Radio Button", default_value=False,
                     callback=debug_callback)
        add_button(callback=save_options)


def debug_callback(sender, data):
    object_data = get_value(sender)
    print("Debug callback {sender} and data {data} and another {data_a}".format(sender=sender, data=object_data,
                                                                                data_a=data))


def checkbox_clicked(object_value):
    output = get_value(object_value)
    print("Checkbox clicked. Status {status}".format(status=output))


def save_options(simple=None):
    def options_window_close_and_save():
        OPTIONS['option1'] = get_value("window_option_1")
        OPTIONS['option2'] = get_value("window_option_2")
        OPTIONS['option3'] = get_value("window_option_3")
        OPTIONS['option4'] = get_value("window_option_4")
        OPTIONS['option5'] = get_value("window_option_5")

    print(OPTIONS)
    options_window_close_and_save()
    window(id=3, show=True)
