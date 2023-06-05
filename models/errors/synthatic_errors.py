class SynthaticParseErrors(Exception):
    """Raised when have any syntactic error"""

    def __init__(self, production_name: str, expected_list: list[str], token):
        self.production_name = production_name
        self.expected_list = expected_list
        self.token = token

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
