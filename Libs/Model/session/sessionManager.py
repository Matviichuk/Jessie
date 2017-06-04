import os.path

session_history_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sessionsHistory.json"))



class SessionManager:
    def __init__(self):
        session_file = None
        try:
            session_file = open(session_history_file_path, 'r')
        except FileNotFoundError:
            session_file = open(session_history_file_path, 'w')

        session_file.close()
    pass

session_manager = SessionManager()