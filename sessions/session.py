import uuid
import time

# Dictionary to store session data
sessions = {}

# Session expiry in seconds (3600 sec = 1 hour)
SESSION_EXPIRY = 3600


def set_session(session_data, resp_obj):
    """
    Creates a session ID, sets session data, assigns an expiry time,
    and sets the session ID in the response's cookies.
    """
    # Generate a unique session ID
    session_id = str(uuid.uuid4())
    # Calculate expiry time (current time: number of sec since epoch)
    expiry_time = (
        time.time() + SESSION_EXPIRY
    )  
    sessions[session_id] = {"data": session_data, "expiry": expiry_time}
    # Set session id in cookies.
    resp_obj.set_cookie("session_id", session_id)


def get_session(session_id):
    """
    Retrieves the session object for the given session ID.
    Checks if the session exists and if it has expired.
    """
    if not session_id or session_id not in sessions:
        return None

    session_obj = sessions[session_id]
    # Check if the session is expired
    if session_obj["expiry"] < time.time():  
        del sessions[session_id]
        return None

    return session_obj["data"]
