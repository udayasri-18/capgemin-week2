class Logger:
    def log(self, message, type="info"):
        if type == "error":
            self._log_error(message)
        elif type == "warning":
            self._log_warning(message)
        else:
            self._log_info(message)

    def _log_error(self, message):
        print(f"[ERROR] {message}")

    def _log_warning(self, message):
        print(f"[WARNING] {message}")

    def _log_info(self, message):
        print(f"[INFO] {message}")


logger = Logger()

logger.log("This is an info message.")  
logger.log("This is a warning message.", "warning")
logger.log("This is an error message.", "error")