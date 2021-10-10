from classes.auto_update import Auto_update_thread


def find_and_terminate_thread(thread_id: int):
    if type(thread_id) is int:
        current_thread = [thread for thread in Auto_update_thread.threads if thread.thread_id == thread_id]
        current_thread[0].stop_thread()
