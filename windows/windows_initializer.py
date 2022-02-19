class WindowsInitializer:
    @classmethod
    def create_windows(cls, windows_list: list):
        for window in windows_list:
            if hasattr(window, 'create_window'):
                window.create_window()
            else:
                raise NotImplementedError(f'The {window} window must have the "create_window" method')

