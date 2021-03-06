# author: WatchDogOblivion
# description: TODO
# WatchDogs FileArgs

from watchdogs.base.models.Args import Args
from watchdogs.utils.Constants import (EMPTY)


class FileArgs(Args):

  def __init__(self, inputFile=EMPTY, outputFile=EMPTY, lines=None):  #type: (str, str, list[str]) -> None
    super(FileArgs, self).__init__()
    self.inputFile = inputFile
    self.outputFile = outputFile
    self.lines = lines

  def getInputFile(self):  #type: () -> str
    return self.inputFile

  def setInputFile(self, inputFile):  #type: (str) -> None
    self.inputFile = inputFile

  def getOutputFile(self):  #type: () -> str
    return self.outputFile

  def setOutputFile(self, outputFile):  #type: (str) -> None
    self.outputFile = outputFile

  def getLines(self):  #type: () -> list[str]
    if(not self.lines):
      return []
    return list(self.lines)

  def setLines(self, lines):  #type: (list[str]) -> None
    self.lines = lines

  def addArguments(self):  #type: () -> FileArgs
    IF_HELP = "Specify the input file to read from."
    OF_HELP = "Specify the output file to write to."

    parser = self.getParser()

    required = parser.add_argument_group("Required file arguments")
    required.add_argument("-if", "--input-file", required=True, help=IF_HELP, type=str, metavar=EMPTY)

    optional = parser.add_argument_group("Optional file arguments")
    optional.add_argument("-of", "--output-file", help=OF_HELP, type=str, metavar=EMPTY)

    return self
