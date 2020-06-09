import logging
import traceback

# module for logging traceback
# instructions on docstring
# example on the testing section at the bottom
__version__ = "1.0.0"


class TracebackLogger:
    """
    Class developed for quickly logging errors to file
    1) create TracebackLogger object;
    2) call the method 'get_traceback' INSIDE the except clause; (this MUST be inside the except)
    3) call the method log_traceback().
    """
    def __init__(self):
        self.logger = logging.getLogger('myapp')
        self.handler = logging.FileHandler('traceback.log')
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.WARNING)
        self.stack = None

    def get_traceback(self) ->None:
        """
        Retrieves the last traceback
        :return None:
        """

        self.stack = traceback.format_exc()

    def log_traceback(self):
        """
        Logs the retrieved traceback to a file
        :return None:
        """
        self.get_traceback()
        if self.stack:
            self.logger.error(self.stack)
        else:
            print(f"Traceback stack not available. Call {self.get_traceback} first.")

    def print_traceback(self):
        """
        Prints the retrieved traceback colored in red
        :return None:
        """
        if self.stack:
            print("\033[91m" + self.stack + "\033[0m")
        else:
            print(f"Traceback stack not available. Call {self.get_traceback} first.")

    def __call__(self, *args, **kwargs):
        """
        Makes the object callable, prints and returns the stack
        :param args: None
        :param kwargs: None
        :return self.stack:
        """
        self.print_traceback()
        return self.stack


# Testing section
if __name__ == "__main__":

    # create the object:
    logger = TracebackLogger()

    try:
        # try some code that may fail to finish
        x = 1/0  # this raises the ZeroDivisionError

    except ZeroDivisionError:
        # log the traceback in the 'traceback.log'
        logger.log_traceback()

        # [optional]
        logger.print_traceback()
    pass
