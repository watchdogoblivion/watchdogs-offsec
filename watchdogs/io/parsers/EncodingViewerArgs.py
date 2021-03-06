# author: WatchDogOblivion
# description: TODO
# WatchDogs Encoding Viewer Args

from collections import OrderedDict

from watchdogs.base.models.Args import Args
from watchdogs.utils.Constants import (EMPTY, LFN)


class EncodingViewerArgs(Args):

  VERSION = "Encoding Viewer version: 1.0"

  ENCODINGS = OrderedDict([(1, 'ascii'), (2, 'big5'), (3, 'big5hkscs'), (4, 'cp037'), (5, 'cp424'),
                           (6, 'cp437'), (7, 'cp500'), (8, 'cp737'), (9, 'cp775'),
                           (10, 'cp850'), (11, 'cp852'), (12, 'cp855'), (13, 'cp856'), (14, 'cp857'),
                           (15, 'cp860'), (16, 'cp861'), (17, 'cp862'), (18, 'cp863'), (19, 'cp864'),
                           (20, 'cp865'), (21, 'cp866'), (22, 'cp869'), (23, 'cp874'), (24, 'cp875'),
                           (25, 'cp932'), (26, 'cp949'), (27, 'cp950'), (28, 'cp1006'), (29, 'cp1026'),
                           (30, 'cp1140'), (31, 'cp1250'), (32, 'cp1251'), (33, 'cp1252'), (34, 'cp1253'),
                           (35, 'cp1254'), (36, 'cp1255'), (37, 'cp1256'), (38, 'cp1257'), (39, 'cp1258'),
                           (40, 'euc-jp'), (41, 'euc-jis-2004'), (42, 'euc-jisx0213'), (43, 'euc-kr'),
                           (44, 'gb2312'), (45, 'gbk'), (46, 'gb18030'), (47, 'hz'), (48, 'iso2022-jp'),
                           (49, 'iso2022-jp-1'), (50, 'iso2022-jp-2'), (51, 'iso2022-jp-2004'),
                           (52, 'iso2022-jp-3'), (53, 'iso2022-jp-ext'), (54, 'iso2022-kr'), (55, 'latin-1'),
                           (56, 'iso8859-2'), (57, 'iso8859-3'), (58, 'iso8859-4'), (59, 'iso8859-5'),
                           (60, 'iso8859-6'), (61, 'iso8859-7'), (62, 'iso8859-8'), (63, 'iso8859-9'),
                           (64, 'iso8859-10'), (65, 'iso8859-13'), (66, 'iso8859-14'), (67, 'iso8859-15'),
                           (68, 'johab'), (69, 'koi8-r'), (70, 'koi8-u'), (71, 'mac-cyrillic'),
                           (72, 'mac-greek'), (73, 'mac-iceland'), (74, 'mac-latin2'), (75, 'mac-roman'),
                           (76, 'mac-turkish'), (77, 'ptcp154'), (78, 'shift-jis'), (79, 'shift-jis-2004'),
                           (80, 'shift-jisx0213'), (81, 'utf-16'), (82, 'utf-16-be'), (83, 'utf-16-le'),
                           (84, 'utf-7'), (85, 'utf-8'), (86, 'base64-codec'), (87, 'bz2-codec'),
                           (88, 'hex-codec'), (89, 'idna'), (90, 'mbcs'), (91, 'palmos'), (92, 'punycode'),
                           (93, 'quopri-codec'), (94, 'raw-unicode-escape'), (95, 'rot-13'),
                           (96, 'string-escape'), (97, 'undefined'), (98, 'unicode-escape'),
                           (99, 'unicode-internal'), (100, 'uu-codec'), (101, 'zlib-codec')])

  def __init__(self, encodeFrom=-1, encodeTo=65):  #type: (int, int) -> None
    super(EncodingViewerArgs, self).__init__()
    self.encodeFrom = encodeFrom
    self.encodeTo = encodeTo

  def getEncodeFrom(self):  #type: () -> int
    return self.encodeFrom

  def setEncodeFrom(self, encodeFrom):  #type: (int) -> None
    self.encodeFrom = encodeFrom

  def getEncodeTo(self):  #type: () -> int
    return self.encodeTo

  def setEncodeTo(self, encodeTo):  #type: (int) -> None
    self.encodeTo = encodeTo

  def getEncodings(self):  #type: () -> str
    encodings = EncodingViewerArgs.ENCODINGS
    encodingString = "Encodings:" + LFN
    for encodingsKey, encodingsValue in encodings.items():
      encodingString += "  {}) {}{}".format(encodingsKey, encodingsValue, LFN)
    return encodingString

  def getVersion(self):  #type: () -> str
    return EncodingViewerArgs.VERSION

  def addArguments(self):  #type: () -> EncodingViewerArgs
    EF_HELP = ("The encoding type to encode from."
               "\nThis value must be a numerical value from the encoding list.")
    ET_HELP = ("The encoding type to encode to."
               "\nThis value must be a numerical value from the encoding list."
               "\nThe default is number 85 - utf-8")
    LE_HELP = "Conversion types."
    ENCODINGS = self.getEncodings()

    parser = self.getParser()
    required = parser.add_argument_group("Required arguments")
    required.add_argument("-ef", "--encode-from", required=True, help=EF_HELP, type=int, metavar=EMPTY)
    parser.add_argument("-et", "--encode-to", help=ET_HELP, type=int, metavar=EMPTY, default=85)
    parser.add_argument("-le", "--list-encodings", action="version", help=LE_HELP, version=ENCODINGS)

    return self