import dearpygui.dearpygui as dpg
from configuration import Config


def font_registration():
    with dpg.font_registry():
        content_folder = getattr(Config, 'content_folder')
        f = f"{content_folder}ARIAL.ttf"
        with dpg.font(file=f, size=16, default_font=True):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Thai)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Vietnamese)