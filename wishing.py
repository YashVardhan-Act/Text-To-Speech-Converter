while True:
    # Making Python Speak Happy 75th Independence Day Of India
    from win32com.client import Dispatch

    t_to_s = input("Enter The Text That you Want To Convert: ")

    def speak(str):
        speak = Dispatch(("SAPI.SpVoice"))
        speak.Speak(str)

    if __name__ == '__main__':
        speak(t_to_s)