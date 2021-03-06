# author: WatchDogOblivion
# description: TODO
# WatchDogs Request Fuzzer

from watchdogs.base.models import Common
from watchdogs.web.models.Requests import Request
from watchdogs.web.models.Locators import VariantLocator
from watchdogs.utils.Constants import EMPTY


class RequestFuzzer(Common):

  def __init__(self, request=Request(), variantLocators=None, fuzzSubstitutes=EMPTY):
    #type: (Request, list[VariantLocator], str) -> None

    super(RequestFuzzer, self).__init__()
    self.__request = request
    self.__variantLocators = variantLocators
    self.__fuzzSubstitutes = fuzzSubstitutes

  def getRequest(self):  #type: () -> Request
    return self.__request

  def setRequest(self, request):  #type: (Request) -> None
    self.__request = request

  def getVariantLocators(self):  #type: () -> list[VariantLocator]
    if (not self.__variantLocators):
      return []
    return list(self.__variantLocators)

  def setVariantLocators(self, variantLocators):  #type: (list[VariantLocator]) -> None
    self.__variantLocators = variantLocators

  def getFuzzSubstitutes(self):  #type: () -> list[str]
    return self.__fuzzSubstitutes

  def setFuzzSubstitutes(self, substitutes):  #type: (list[str]) -> None
    self.__fuzzSubstitutes = substitutes

  def rebaseLocators(self):  #type: () -> list[VariantLocator]
    if (not self.__variantLocators):
      self.__variantLocators = []
    self.__variantLocators.append(VariantLocator(isInfo=True))
    self.__variantLocators.append(VariantLocator(isHeaders=True))
    self.__variantLocators.append(VariantLocator(isBody=True))
    return self.__variantLocators