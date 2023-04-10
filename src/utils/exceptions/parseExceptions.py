class CSVHostsParseException(Exception):
    def __init__(
        self,
        message="Error ocurred while parsing provided CSV file. Check the output.log",
    ):
        super().__init__(message)
