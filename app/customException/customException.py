class CustomException(Exception):
    def __init__(self, message: str | None=None, status_code: int = 500,show_guide=False):
        self.status_code = status_code  or 500
        self.message = message or "something went wrong"
        self.show_guide = show_guide

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, tb):
        print("exc_type", exc_type)
        print("exc", exc)