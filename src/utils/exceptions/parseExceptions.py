class CSVHostsParseException(Exception):
    def __init__(
        self,
        message="Error ocurred while parsing provided CSV file. Check the output.log",
    ):
        super().__init__(message)


class HostsFileNotFoundException(Exception):
    def __init__(
        self,
        file_path: str,
        message="",
    ):
        self.message = f"Provided file '{file_path}' not found"
        super().__init__(message)
