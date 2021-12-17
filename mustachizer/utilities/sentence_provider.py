import random

from mustachizer import PATH
from mustachizer.utilities import JSONFilepathError, LoadJSON
from mustachizer.utilities.errors import SentenceProviderError


class SentenceProvider:
    """
    Provides sentences for responses.
    """

    def __init__(self):
        """
        Load all sentences.

        :raises SentenceProviderError: something wrong happened during sentences loading
        """
        try:
            sentences_filepath = PATH / "mustachizer" / "utilities" / "sentences.json"
            self.sentences = LoadJSON(filepath=sentences_filepath)["sentences"]
        except JSONFilepathError as error:
            raise SentenceProviderError(error) from error

    def provide(self) -> str:
        """
        Provide a random sentence.
        """
        return random.choice(self.sentences)
