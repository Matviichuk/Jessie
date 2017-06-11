import os.path
import json
from .session import _Session
from .session import open_session

_max_records_in_session_history_file = 20
session_history_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sessionsHistory.json"))

class SessionManager:
    _sessions_info = []

    def __init__(self):
        session_file = None
        try:
            session_file = open(session_history_file_path, 'r')
            session_file_str = session_file.read()
            self._sessions_info = json.loads(session_file_str)

        except FileNotFoundError:
            session_file = open(session_history_file_path, 'w')
            session_file.write("[]")


        session_file.close()
    pass

    def open_session(self, sessionPath):
        print("open {}".format(sessionPath))
        if sessionPath == None:
            return
        session = None
        if([sessionPath for item in self._sessions_info if item["Filepath"] == sessionPath]):
            # session in list
            session = open_session(sessionPath)
        else:
            # session not in list
            try:
                file = open(sessionPath, 'r')
                file.close()
            except FileNotFoundError:
                print("File not found")
                return
            session = open_session(sessionPath)
            self._sessions_info.insert(0, {"Filepath": session.path,
                                           "PatientName": "",
                                           "SessionName": session.name})
            session_file = open(session_history_file_path, 'w')
            if len(self._sessions_info) > _max_records_in_session_history_file:
                number_sessions = len(self._sessions_info)
                jsonData = json.dumps(self._sessions_info[number_sessions - _max_records_in_session_history_file : number_sessions])
            else:
                jsonData = json.dumps(self._sessions_info)
            session_file.write(jsonData)
            session_file.close()
        return session

    def sessions_info(self):
        return self._sessions_info

session_manager = SessionManager()