import WordRepository.WordFetcher as fetcher
class SpellingBeeModel:

    def __init__(self):
        self.__points = 0 
        self.__totalAnswers = []
        self.__randomLetters = []

    @property
    def points(self):
        return self.__points

    @_points.setter
    def _points(self, value):
        self.__points = value

    @property
    def _totalAnswers(self):
        return self.__totalAnswers

    @_totalAnswers.setter
    def _totalAnswers(self, value):
        self.__totalAnswers = value

    @property
    def _randomLetters(self):
        return self.__randomLetters

    @_randomLetters.setter
    def _randomLetters(self, value):
        self.__randomLetters = value

    









