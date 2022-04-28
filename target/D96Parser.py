# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u022d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3r\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4y\n\4\3\4\3\4\3\4\5\4~\n\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u0086\n\5\3\6\3\6\5\6\u008a\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0095\n\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a3\n\b")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00a9\n\t\3\t\3\t\3\t\3\t\5\t\u00af")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00b6\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00bd\n\13\3\f\3\f\3\f\3\f\5\f\u00c3\n")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00d2\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00dc\n\20\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e3\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00ea\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\7\23\u00f2\n\23\f\23\16\23")
        buf.write("\u00f5\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00fd")
        buf.write("\n\24\f\24\16\24\u0100\13\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u0108\n\25\f\25\16\25\u010b\13\25\3\26\3\26")
        buf.write("\3\26\5\26\u0110\n\26\3\27\3\27\3\27\5\27\u0115\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\7\30\u011c\n\30\f\30\16\30\u011f")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u012a\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0138\n\32\3\32\7\32\u013b\n")
        buf.write("\32\f\32\16\32\u013e\13\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u0149\n\33\3\33\3\33\5\33\u014d")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u0154\n\34\3\34\3")
        buf.write("\34\5\34\u0158\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0162\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u016d\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0178\n\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \5 \u0186\n \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\5!\u0193\n!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01aa\n")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01b6\n$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\5$\u01bf\n$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\5\'\u01cd\n\'\3\'\3\'\3(\3(\3(\3(\3(\3(\5(\u01d7")
        buf.write("\n(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01e2\n(\3(\3(\5(\u01e6")
        buf.write("\n(\3)\3)\3)\5)\u01eb\n)\3)\3)\3*\3*\3*\3*\5*\u01f3\n")
        buf.write("*\3+\3+\3+\5+\u01f8\n+\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\5.\u0205\n.\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u020f\n\60\3\61\3\61\5\61\u0213\n\61\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u0219\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\5\64\u0227\n\64\3\65\3\65\5")
        buf.write("\65\u022b\n\65\3\65\2\7$&(.\62\66\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfh\2\n\3\2\37 \3\2\678\3\2\64\65\4\2--/\63\3")
        buf.write("\2+,\3\2%&\3\2\')\3\2\30\33\2\u0241\2j\3\2\2\2\4q\3\2")
        buf.write("\2\2\6s\3\2\2\2\b\u0085\3\2\2\2\n\u0089\3\2\2\2\f\u008b")
        buf.write("\3\2\2\2\16\u00a2\3\2\2\2\20\u00ae\3\2\2\2\22\u00b5\3")
        buf.write("\2\2\2\24\u00bc\3\2\2\2\26\u00be\3\2\2\2\30\u00c7\3\2")
        buf.write("\2\2\32\u00d1\3\2\2\2\34\u00d3\3\2\2\2\36\u00db\3\2\2")
        buf.write("\2 \u00e2\3\2\2\2\"\u00e9\3\2\2\2$\u00eb\3\2\2\2&\u00f6")
        buf.write("\3\2\2\2(\u0101\3\2\2\2*\u010f\3\2\2\2,\u0114\3\2\2\2")
        buf.write(".\u0116\3\2\2\2\60\u0129\3\2\2\2\62\u012b\3\2\2\2\64\u014c")
        buf.write("\3\2\2\2\66\u0157\3\2\2\28\u0161\3\2\2\2:\u016c\3\2\2")
        buf.write("\2<\u016e\3\2\2\2>\u0185\3\2\2\2@\u0192\3\2\2\2B\u0198")
        buf.write("\3\2\2\2D\u01a9\3\2\2\2F\u01ab\3\2\2\2H\u01c3\3\2\2\2")
        buf.write("J\u01c6\3\2\2\2L\u01c9\3\2\2\2N\u01e5\3\2\2\2P\u01e7\3")
        buf.write("\2\2\2R\u01f2\3\2\2\2T\u01f7\3\2\2\2V\u01f9\3\2\2\2X\u01fb")
        buf.write("\3\2\2\2Z\u0204\3\2\2\2\\\u0206\3\2\2\2^\u020e\3\2\2\2")
        buf.write("`\u0212\3\2\2\2b\u0214\3\2\2\2d\u021c\3\2\2\2f\u0226\3")
        buf.write("\2\2\2h\u022a\3\2\2\2jk\5\4\3\2kl\7\2\2\3l\3\3\2\2\2m")
        buf.write("n\5\6\4\2no\5\4\3\2or\3\2\2\2pr\5\6\4\2qm\3\2\2\2qp\3")
        buf.write("\2\2\2r\5\3\2\2\2st\7\36\2\2tx\7\67\2\2uv\7C\2\2vy\7\67")
        buf.write("\2\2wy\3\2\2\2xu\3\2\2\2xw\3\2\2\2yz\3\2\2\2z}\7;\2\2")
        buf.write("{~\5\b\5\2|~\3\2\2\2}{\3\2\2\2}|\3\2\2\2~\177\3\2\2\2")
        buf.write("\177\u0080\7<\2\2\u0080\7\3\2\2\2\u0081\u0082\5\n\6\2")
        buf.write("\u0082\u0083\5\b\5\2\u0083\u0086\3\2\2\2\u0084\u0086\5")
        buf.write("\n\6\2\u0085\u0081\3\2\2\2\u0085\u0084\3\2\2\2\u0086\t")
        buf.write("\3\2\2\2\u0087\u008a\5\f\7\2\u0088\u008a\5\20\t\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\13\3\2\2\2\u008b")
        buf.write("\u0094\t\2\2\2\u008c\u008d\t\3\2\2\u008d\u008e\5\16\b")
        buf.write("\2\u008e\u008f\5 \21\2\u008f\u0095\3\2\2\2\u0090\u0091")
        buf.write("\5\24\13\2\u0091\u0092\7C\2\2\u0092\u0093\5T+\2\u0093")
        buf.write("\u0095\3\2\2\2\u0094\u008c\3\2\2\2\u0094\u0090\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0097\7=\2\2\u0097\r\3\2\2")
        buf.write("\2\u0098\u0099\7B\2\2\u0099\u009a\t\3\2\2\u009a\u009b")
        buf.write("\5\16\b\2\u009b\u009c\5 \21\2\u009c\u009d\7B\2\2\u009d")
        buf.write("\u00a3\3\2\2\2\u009e\u009f\7C\2\2\u009f\u00a0\5T+\2\u00a0")
        buf.write("\u00a1\7.\2\2\u00a1\u00a3\3\2\2\2\u00a2\u0098\3\2\2\2")
        buf.write("\u00a2\u009e\3\2\2\2\u00a3\17\3\2\2\2\u00a4\u00a5\t\3")
        buf.write("\2\2\u00a5\u00a8\79\2\2\u00a6\u00a9\5\32\16\2\u00a7\u00a9")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ab\7:\2\2\u00ab\u00af\5P)\2\u00ac")
        buf.write("\u00af\5\26\f\2\u00ad\u00af\5\30\r\2\u00ae\u00a4\3\2\2")
        buf.write("\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\21\3")
        buf.write("\2\2\2\u00b0\u00b1\5 \21\2\u00b1\u00b2\7B\2\2\u00b2\u00b3")
        buf.write("\5\22\n\2\u00b3\u00b6\3\2\2\2\u00b4\u00b6\5 \21\2\u00b5")
        buf.write("\u00b0\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\23\3\2\2\2\u00b7")
        buf.write("\u00b8\t\3\2\2\u00b8\u00b9\7B\2\2\u00b9\u00bd\5\24\13")
        buf.write("\2\u00ba\u00bd\7\67\2\2\u00bb\u00bd\78\2\2\u00bc\u00b7")
        buf.write("\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\25\3\2\2\2\u00be\u00bf\7!\2\2\u00bf\u00c2\79\2\2\u00c0")
        buf.write("\u00c3\5\32\16\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2")
        buf.write("\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5")
        buf.write("\7:\2\2\u00c5\u00c6\5P)\2\u00c6\27\3\2\2\2\u00c7\u00c8")
        buf.write("\7\"\2\2\u00c8\u00c9\79\2\2\u00c9\u00ca\7:\2\2\u00ca\u00cb")
        buf.write("\5P)\2\u00cb\31\3\2\2\2\u00cc\u00cd\5\34\17\2\u00cd\u00ce")
        buf.write("\7=\2\2\u00ce\u00cf\5\32\16\2\u00cf\u00d2\3\2\2\2\u00d0")
        buf.write("\u00d2\5\34\17\2\u00d1\u00cc\3\2\2\2\u00d1\u00d0\3\2\2")
        buf.write("\2\u00d2\33\3\2\2\2\u00d3\u00d4\5\36\20\2\u00d4\u00d5")
        buf.write("\7C\2\2\u00d5\u00d6\5T+\2\u00d6\35\3\2\2\2\u00d7\u00d8")
        buf.write("\7\67\2\2\u00d8\u00d9\7B\2\2\u00d9\u00dc\5\36\20\2\u00da")
        buf.write("\u00dc\7\67\2\2\u00db\u00d7\3\2\2\2\u00db\u00da\3\2\2")
        buf.write("\2\u00dc\37\3\2\2\2\u00dd\u00de\5\"\22\2\u00de\u00df\t")
        buf.write("\4\2\2\u00df\u00e0\5\"\22\2\u00e0\u00e3\3\2\2\2\u00e1")
        buf.write("\u00e3\5\"\22\2\u00e2\u00dd\3\2\2\2\u00e2\u00e1\3\2\2")
        buf.write("\2\u00e3!\3\2\2\2\u00e4\u00e5\5$\23\2\u00e5\u00e6\t\5")
        buf.write("\2\2\u00e6\u00e7\5$\23\2\u00e7\u00ea\3\2\2\2\u00e8\u00ea")
        buf.write("\5$\23\2\u00e9\u00e4\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write("#\3\2\2\2\u00eb\u00ec\b\23\1\2\u00ec\u00ed\5&\24\2\u00ed")
        buf.write("\u00f3\3\2\2\2\u00ee\u00ef\f\4\2\2\u00ef\u00f0\t\6\2\2")
        buf.write("\u00f0\u00f2\5&\24\2\u00f1\u00ee\3\2\2\2\u00f2\u00f5\3")
        buf.write("\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4%")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\b\24\1\2\u00f7")
        buf.write("\u00f8\5(\25\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa\f\4\2\2")
        buf.write("\u00fa\u00fb\t\7\2\2\u00fb\u00fd\5(\25\2\u00fc\u00f9\3")
        buf.write("\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\'\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102")
        buf.write("\b\25\1\2\u0102\u0103\5*\26\2\u0103\u0109\3\2\2\2\u0104")
        buf.write("\u0105\f\4\2\2\u0105\u0106\t\b\2\2\u0106\u0108\5*\26\2")
        buf.write("\u0107\u0104\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u010a\3\2\2\2\u010a)\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010d\7*\2\2\u010d\u0110\5*\26\2\u010e")
        buf.write("\u0110\5,\27\2\u010f\u010c\3\2\2\2\u010f\u010e\3\2\2\2")
        buf.write("\u0110+\3\2\2\2\u0111\u0112\7&\2\2\u0112\u0115\5,\27\2")
        buf.write("\u0113\u0115\5.\30\2\u0114\u0111\3\2\2\2\u0114\u0113\3")
        buf.write("\2\2\2\u0115-\3\2\2\2\u0116\u0117\b\30\1\2\u0117\u0118")
        buf.write("\5\62\32\2\u0118\u011d\3\2\2\2\u0119\u011a\f\4\2\2\u011a")
        buf.write("\u011c\5\60\31\2\u011b\u0119\3\2\2\2\u011c\u011f\3\2\2")
        buf.write("\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e/\3\2")
        buf.write("\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7>\2\2\u0121\u0122")
        buf.write("\5 \21\2\u0122\u0123\7?\2\2\u0123\u012a\3\2\2\2\u0124")
        buf.write("\u0125\7>\2\2\u0125\u0126\5 \21\2\u0126\u0127\7?\2\2\u0127")
        buf.write("\u0128\5\60\31\2\u0128\u012a\3\2\2\2\u0129\u0120\3\2\2")
        buf.write("\2\u0129\u0124\3\2\2\2\u012a\61\3\2\2\2\u012b\u012c\b")
        buf.write("\32\1\2\u012c\u012d\5\64\33\2\u012d\u013c\3\2\2\2\u012e")
        buf.write("\u012f\f\5\2\2\u012f\u0130\7A\2\2\u0130\u013b\7\67\2\2")
        buf.write("\u0131\u0132\f\4\2\2\u0132\u0133\7A\2\2\u0133\u0134\7")
        buf.write("\67\2\2\u0134\u0137\79\2\2\u0135\u0138\5\22\n\2\u0136")
        buf.write("\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013b\7:\2\2\u013a\u012e\3")
        buf.write("\2\2\2\u013a\u0131\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\63\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0140\7\67\2\2\u0140\u0141\7\66\2\2\u0141")
        buf.write("\u014d\78\2\2\u0142\u0143\7\67\2\2\u0143\u0144\7\66\2")
        buf.write("\2\u0144\u0145\78\2\2\u0145\u0148\79\2\2\u0146\u0149\5")
        buf.write("\22\n\2\u0147\u0149\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014d\7:\2\2")
        buf.write("\u014b\u014d\5\66\34\2\u014c\u013f\3\2\2\2\u014c\u0142")
        buf.write("\3\2\2\2\u014c\u014b\3\2\2\2\u014d\65\3\2\2\2\u014e\u014f")
        buf.write("\7#\2\2\u014f\u0150\7\67\2\2\u0150\u0153\79\2\2\u0151")
        buf.write("\u0154\5\22\n\2\u0152\u0154\3\2\2\2\u0153\u0151\3\2\2")
        buf.write("\2\u0153\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0158")
        buf.write("\7:\2\2\u0156\u0158\58\35\2\u0157\u014e\3\2\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158\67\3\2\2\2\u0159\u015a\79\2\2\u015a")
        buf.write("\u015b\5 \21\2\u015b\u015c\7:\2\2\u015c\u0162\3\2\2\2")
        buf.write("\u015d\u0162\5^\60\2\u015e\u0162\7\67\2\2\u015f\u0162")
        buf.write("\7\r\2\2\u0160\u0162\7\35\2\2\u0161\u0159\3\2\2\2\u0161")
        buf.write("\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u01629\3\2\2\2\u0163\u016d\5@!\2")
        buf.write("\u0164\u016d\5B\"\2\u0165\u016d\5F$\2\u0166\u016d\5H%")
        buf.write("\2\u0167\u016d\5J&\2\u0168\u016d\5L\'\2\u0169\u016d\5")
        buf.write("N(\2\u016a\u016d\5<\37\2\u016b\u016d\5P)\2\u016c\u0163")
        buf.write("\3\2\2\2\u016c\u0164\3\2\2\2\u016c\u0165\3\2\2\2\u016c")
        buf.write("\u0166\3\2\2\2\u016c\u0167\3\2\2\2\u016c\u0168\3\2\2\2")
        buf.write("\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3")
        buf.write("\2\2\2\u016d;\3\2\2\2\u016e\u0177\t\2\2\2\u016f\u0170")
        buf.write("\7\67\2\2\u0170\u0171\5> \2\u0171\u0172\5 \21\2\u0172")
        buf.write("\u0178\3\2\2\2\u0173\u0174\5\36\20\2\u0174\u0175\7C\2")
        buf.write("\2\u0175\u0176\5T+\2\u0176\u0178\3\2\2\2\u0177\u016f\3")
        buf.write("\2\2\2\u0177\u0173\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a")
        buf.write("\7=\2\2\u017a=\3\2\2\2\u017b\u017c\7B\2\2\u017c\u017d")
        buf.write("\7\67\2\2\u017d\u017e\5> \2\u017e\u017f\5 \21\2\u017f")
        buf.write("\u0180\7B\2\2\u0180\u0186\3\2\2\2\u0181\u0182\7C\2\2\u0182")
        buf.write("\u0183\5T+\2\u0183\u0184\7.\2\2\u0184\u0186\3\2\2\2\u0185")
        buf.write("\u017b\3\2\2\2\u0185\u0181\3\2\2\2\u0186?\3\2\2\2\u0187")
        buf.write("\u0193\7\67\2\2\u0188\u0189\5 \21\2\u0189\u018a\7A\2\2")
        buf.write("\u018a\u018b\7\67\2\2\u018b\u0193\3\2\2\2\u018c\u018d")
        buf.write("\7\67\2\2\u018d\u018e\7\66\2\2\u018e\u0193\78\2\2\u018f")
        buf.write("\u0190\5 \21\2\u0190\u0191\5\60\31\2\u0191\u0193\3\2\2")
        buf.write("\2\u0192\u0187\3\2\2\2\u0192\u0188\3\2\2\2\u0192\u018c")
        buf.write("\3\2\2\2\u0192\u018f\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\7.\2\2\u0195\u0196\5 \21\2\u0196\u0197\7=\2\2\u0197")
        buf.write("A\3\2\2\2\u0198\u0199\7\20\2\2\u0199\u019a\79\2\2\u019a")
        buf.write("\u019b\5 \21\2\u019b\u019c\7:\2\2\u019c\u019d\5P)\2\u019d")
        buf.write("\u019e\5D#\2\u019eC\3\2\2\2\u019f\u01a0\7\21\2\2\u01a0")
        buf.write("\u01a1\79\2\2\u01a1\u01a2\5 \21\2\u01a2\u01a3\7:\2\2\u01a3")
        buf.write("\u01a4\5P)\2\u01a4\u01a5\5D#\2\u01a5\u01aa\3\2\2\2\u01a6")
        buf.write("\u01a7\7\22\2\2\u01a7\u01aa\5P)\2\u01a8\u01aa\3\2\2\2")
        buf.write("\u01a9\u019f\3\2\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a8\3")
        buf.write("\2\2\2\u01aaE\3\2\2\2\u01ab\u01ac\7\23\2\2\u01ac\u01b5")
        buf.write("\79\2\2\u01ad\u01b6\7\67\2\2\u01ae\u01af\5 \21\2\u01af")
        buf.write("\u01b0\7A\2\2\u01b0\u01b1\7\67\2\2\u01b1\u01b6\3\2\2\2")
        buf.write("\u01b2\u01b3\7\67\2\2\u01b3\u01b4\7\66\2\2\u01b4\u01b6")
        buf.write("\78\2\2\u01b5\u01ad\3\2\2\2\u01b5\u01ae\3\2\2\2\u01b5")
        buf.write("\u01b2\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\7\27\2")
        buf.write("\2\u01b8\u01b9\5 \21\2\u01b9\u01ba\7@\2\2\u01ba\u01be")
        buf.write("\5 \21\2\u01bb\u01bc\7$\2\2\u01bc\u01bf\5 \21\2\u01bd")
        buf.write("\u01bf\3\2\2\2\u01be\u01bb\3\2\2\2\u01be\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c1\7:\2\2\u01c1\u01c2\5")
        buf.write("P)\2\u01c2G\3\2\2\2\u01c3\u01c4\7\16\2\2\u01c4\u01c5\7")
        buf.write("=\2\2\u01c5I\3\2\2\2\u01c6\u01c7\7\17\2\2\u01c7\u01c8")
        buf.write("\7=\2\2\u01c8K\3\2\2\2\u01c9\u01cc\7\34\2\2\u01ca\u01cd")
        buf.write("\5 \21\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\7=\2\2")
        buf.write("\u01cfM\3\2\2\2\u01d0\u01d1\5 \21\2\u01d1\u01d2\7A\2\2")
        buf.write("\u01d2\u01d3\7\67\2\2\u01d3\u01d6\79\2\2\u01d4\u01d7\5")
        buf.write("\22\n\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\7:\2\2")
        buf.write("\u01d9\u01da\7=\2\2\u01da\u01e6\3\2\2\2\u01db\u01dc\7")
        buf.write("\67\2\2\u01dc\u01dd\7\66\2\2\u01dd\u01de\78\2\2\u01de")
        buf.write("\u01e1\79\2\2\u01df\u01e2\5\22\n\2\u01e0\u01e2\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3")
        buf.write("\2\2\2\u01e3\u01e4\7:\2\2\u01e4\u01e6\7=\2\2\u01e5\u01d0")
        buf.write("\3\2\2\2\u01e5\u01db\3\2\2\2\u01e6O\3\2\2\2\u01e7\u01ea")
        buf.write("\7;\2\2\u01e8\u01eb\5R*\2\u01e9\u01eb\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ed\7<\2\2\u01edQ\3\2\2\2\u01ee\u01ef\5:\36\2\u01ef")
        buf.write("\u01f0\5R*\2\u01f0\u01f3\3\2\2\2\u01f1\u01f3\5:\36\2\u01f2")
        buf.write("\u01ee\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3S\3\2\2\2\u01f4")
        buf.write("\u01f8\5V,\2\u01f5\u01f8\5X-\2\u01f6\u01f8\5\\/\2\u01f7")
        buf.write("\u01f4\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2")
        buf.write("\u01f8U\3\2\2\2\u01f9\u01fa\t\t\2\2\u01faW\3\2\2\2\u01fb")
        buf.write("\u01fc\7\26\2\2\u01fc\u01fd\7>\2\2\u01fd\u01fe\5Z.\2\u01fe")
        buf.write("\u01ff\7B\2\2\u01ff\u0200\7\7\2\2\u0200\u0201\7?\2\2\u0201")
        buf.write("Y\3\2\2\2\u0202\u0205\5V,\2\u0203\u0205\5X-\2\u0204\u0202")
        buf.write("\3\2\2\2\u0204\u0203\3\2\2\2\u0205[\3\2\2\2\u0206\u0207")
        buf.write("\7\67\2\2\u0207]\3\2\2\2\u0208\u020f\7\5\2\2\u0209\u020f")
        buf.write("\7\7\2\2\u020a\u020f\7\6\2\2\u020b\u020f\7\4\2\2\u020c")
        buf.write("\u020f\7\3\2\2\u020d\u020f\5`\61\2\u020e\u0208\3\2\2\2")
        buf.write("\u020e\u0209\3\2\2\2\u020e\u020a\3\2\2\2\u020e\u020b\3")
        buf.write("\2\2\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020f_")
        buf.write("\3\2\2\2\u0210\u0213\5b\62\2\u0211\u0213\5d\63\2\u0212")
        buf.write("\u0210\3\2\2\2\u0212\u0211\3\2\2\2\u0213a\3\2\2\2\u0214")
        buf.write("\u0215\7\26\2\2\u0215\u0218\79\2\2\u0216\u0219\5\22\n")
        buf.write("\2\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0217")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b\7:\2\2\u021b")
        buf.write("c\3\2\2\2\u021c\u021d\7\26\2\2\u021d\u021e\79\2\2\u021e")
        buf.write("\u021f\5f\64\2\u021f\u0220\7:\2\2\u0220e\3\2\2\2\u0221")
        buf.write("\u0222\5h\65\2\u0222\u0223\7B\2\2\u0223\u0224\5f\64\2")
        buf.write("\u0224\u0227\3\2\2\2\u0225\u0227\5h\65\2\u0226\u0221\3")
        buf.write("\2\2\2\u0226\u0225\3\2\2\2\u0227g\3\2\2\2\u0228\u022b")
        buf.write("\5b\62\2\u0229\u022b\5d\63\2\u022a\u0228\3\2\2\2\u022a")
        buf.write("\u0229\3\2\2\2\u022bi\3\2\2\2\65qx}\u0085\u0089\u0094")
        buf.write("\u00a2\u00a8\u00ae\u00b5\u00bc\u00c2\u00d1\u00db\u00e2")
        buf.write("\u00e9\u00f3\u00fe\u0109\u010f\u0114\u011d\u0129\u0137")
        buf.write("\u013a\u013c\u0148\u014c\u0153\u0157\u0161\u016c\u0177")
        buf.write("\u0185\u0192\u01a9\u01b5\u01be\u01cc\u01d6\u01e1\u01e5")
        buf.write("\u01ea\u01f2\u01f7\u0204\u020e\u0212\u0218\u0226\u022a")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Self'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
                     "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'+.'", "'==.'", "'::'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'['", 
                     "']'", "'..'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "STR", "FLOAT", "INT_ZERO", "INT_GT", 
                      "DEC_GT", "HEX_GT", "OCTAL_GT", "BINARY_GT", "COMMENT", 
                      "SELF", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                      "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INTTYPE", 
                      "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "RM", "NOT", 
                      "AND", "OR", "EQ", "ASSG", "NEQ", "LT", "GT", "LTE", 
                      "GTE", "STR_CONCAT", "STR_COMPARE", "ACCESS", "ID", 
                      "SID", "LB", "RB", "LP", "RP", "SEMI", "LS", "RS", 
                      "DOTDOT", "DOT", "COMMA", "IS", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_class_declaration = 2
    RULE_class_members = 3
    RULE_cl_member = 4
    RULE_attr_decl = 5
    RULE_decl_part = 6
    RULE_method_decl = 7
    RULE_exprlist = 8
    RULE_idlist = 9
    RULE_constructor = 10
    RULE_destructor = 11
    RULE_paramslist = 12
    RULE_params = 13
    RULE_non_st_idlist = 14
    RULE_expr = 15
    RULE_expr1 = 16
    RULE_expr2 = 17
    RULE_expr3 = 18
    RULE_expr4 = 19
    RULE_expr5 = 20
    RULE_expr6 = 21
    RULE_expr7 = 22
    RULE_index_op = 23
    RULE_expr8 = 24
    RULE_expr9 = 25
    RULE_expr10 = 26
    RULE_operands = 27
    RULE_stmt = 28
    RULE_decl_stm = 29
    RULE_decl_stm_part = 30
    RULE_assg_stm = 31
    RULE_if_stm = 32
    RULE_else_if_stm = 33
    RULE_for_stm = 34
    RULE_break_stm = 35
    RULE_continue_stm = 36
    RULE_return_stm = 37
    RULE_invocatoin_stm = 38
    RULE_blk_stmt = 39
    RULE_stmtlist = 40
    RULE_type_name = 41
    RULE_primitive_typ = 42
    RULE_array_typ = 43
    RULE_typ = 44
    RULE_class_typ = 45
    RULE_literals = 46
    RULE_array_literal = 47
    RULE_idxlit = 48
    RULE_mullit = 49
    RULE_arrlist = 50
    RULE_arr = 51

    ruleNames =  [ "program", "decls", "class_declaration", "class_members", 
                   "cl_member", "attr_decl", "decl_part", "method_decl", 
                   "exprlist", "idlist", "constructor", "destructor", "paramslist", 
                   "params", "non_st_idlist", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "index_op", 
                   "expr8", "expr9", "expr10", "operands", "stmt", "decl_stm", 
                   "decl_stm_part", "assg_stm", "if_stm", "else_if_stm", 
                   "for_stm", "break_stm", "continue_stm", "return_stm", 
                   "invocatoin_stm", "blk_stmt", "stmtlist", "type_name", 
                   "primitive_typ", "array_typ", "typ", "class_typ", "literals", 
                   "array_literal", "idxlit", "mullit", "arrlist", "arr" ]

    EOF = Token.EOF
    BOOL=1
    STR=2
    FLOAT=3
    INT_ZERO=4
    INT_GT=5
    DEC_GT=6
    HEX_GT=7
    OCTAL_GT=8
    BINARY_GT=9
    COMMENT=10
    SELF=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSEIF=15
    ELSE=16
    FOREACH=17
    TRUE=18
    FALSE=19
    ARRAY=20
    IN=21
    INTTYPE=22
    FLOATTYPE=23
    BOOLTYPE=24
    STRINGTYPE=25
    RETURN=26
    NULL=27
    CLASS=28
    VAL=29
    VAR=30
    CONSTRUCTOR=31
    DESTRUCTOR=32
    NEW=33
    BY=34
    ADD=35
    SUB=36
    MUL=37
    DIV=38
    RM=39
    NOT=40
    AND=41
    OR=42
    EQ=43
    ASSG=44
    NEQ=45
    LT=46
    GT=47
    LTE=48
    GTE=49
    STR_CONCAT=50
    STR_COMPARE=51
    ACCESS=52
    ID=53
    SID=54
    LB=55
    RB=56
    LP=57
    RP=58
    SEMI=59
    LS=60
    RS=61
    DOTDOT=62
    DOT=63
    COMMA=64
    IS=65
    WS=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68
    ERROR_TOKEN=69

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(D96Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.decls()
            self.state = 105
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declaration(self):
            return self.getTypedRuleContext(D96Parser.Class_declarationContext,0)


        def decls(self):
            return self.getTypedRuleContext(D96Parser.DeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = D96Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.class_declaration()
                self.state = 108
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.class_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def IS(self):
            return self.getToken(D96Parser.IS, 0)

        def class_members(self):
            return self.getTypedRuleContext(D96Parser.Class_membersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.CLASS)
            self.state = 114
            self.match(D96Parser.ID)
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IS]:
                self.state = 115
                self.match(D96Parser.IS)
                self.state = 116
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 120
            self.match(D96Parser.LP)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.SID]:
                self.state = 121
                self.class_members()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cl_member(self):
            return self.getTypedRuleContext(D96Parser.Cl_memberContext,0)


        def class_members(self):
            return self.getTypedRuleContext(D96Parser.Class_membersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_members" ):
                return visitor.visitClass_members(self)
            else:
                return visitor.visitChildren(self)




    def class_members(self):

        localctx = D96Parser.Class_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_members)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.cl_member()
                self.state = 128
                self.class_members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.cl_member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cl_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_cl_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCl_member" ):
                return visitor.visitCl_member(self)
            else:
                return visitor.visitChildren(self)




    def cl_member(self):

        localctx = D96Parser.Cl_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cl_member)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.attr_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.SID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.method_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def decl_part(self):
            return self.getTypedRuleContext(D96Parser.Decl_partContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def IS(self):
            return self.getToken(D96Parser.IS, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.SID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.decl_part()
                self.state = 140
                self.expr()
                pass

            elif la_ == 2:
                self.state = 142
                self.idlist()
                self.state = 143
                self.match(D96Parser.IS)
                self.state = 144
                self.type_name()
                pass


            self.state = 148
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def decl_part(self):
            return self.getTypedRuleContext(D96Parser.Decl_partContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def IS(self):
            return self.getToken(D96Parser.IS, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def ASSG(self):
            return self.getToken(D96Parser.ASSG, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_part" ):
                return visitor.visitDecl_part(self)
            else:
                return visitor.visitChildren(self)




    def decl_part(self):

        localctx = D96Parser.Decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_part)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(D96Parser.COMMA)
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.SID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.decl_part()
                self.state = 153
                self.expr()
                self.state = 154
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.IS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(D96Parser.IS)
                self.state = 157
                self.type_name()
                self.state = 158
                self.match(D96Parser.ASSG)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramslist(self):
            return self.getTypedRuleContext(D96Parser.ParamslistContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.SID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.SID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.match(D96Parser.LB)
                self.state = 166
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.ID]:
                    self.state = 164
                    self.paramslist()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 168
                self.match(D96Parser.RB)
                self.state = 169
                self.blk_stmt()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = D96Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprlist)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expr()
                self.state = 175
                self.match(D96Parser.COMMA)
                self.state = 176
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.SID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
                self.match(D96Parser.COMMA)
                self.state = 183
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(D96Parser.SID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def paramslist(self):
            return self.getTypedRuleContext(D96Parser.ParamslistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 189
            self.match(D96Parser.LB)
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.state = 190
                self.paramslist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 194
            self.match(D96Parser.RB)
            self.state = 195
            self.blk_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(D96Parser.DESTRUCTOR)
            self.state = 198
            self.match(D96Parser.LB)
            self.state = 199
            self.match(D96Parser.RB)
            self.state = 200
            self.blk_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def paramslist(self):
            return self.getTypedRuleContext(D96Parser.ParamslistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamslist" ):
                return visitor.visitParamslist(self)
            else:
                return visitor.visitChildren(self)




    def paramslist(self):

        localctx = D96Parser.ParamslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramslist)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.params()
                self.state = 203
                self.match(D96Parser.SEMI)
                self.state = 204
                self.paramslist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_st_idlist(self):
            return self.getTypedRuleContext(D96Parser.Non_st_idlistContext,0)


        def IS(self):
            return self.getToken(D96Parser.IS, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.non_st_idlist()
            self.state = 210
            self.match(D96Parser.IS)
            self.state = 211
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_st_idlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def non_st_idlist(self):
            return self.getTypedRuleContext(D96Parser.Non_st_idlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_non_st_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_st_idlist" ):
                return visitor.visitNon_st_idlist(self)
            else:
                return visitor.visitChildren(self)




    def non_st_idlist(self):

        localctx = D96Parser.Non_st_idlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_non_st_idlist)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(D96Parser.ID)
                self.state = 214
                self.match(D96Parser.COMMA)
                self.state = 215
                self.non_st_idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def STR_COMPARE(self):
            return self.getToken(D96Parser.STR_COMPARE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.expr1()
                self.state = 220
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_CONCAT or _la==D96Parser.STR_COMPARE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 221
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D96Parser.NEQ, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.expr2(0)
                self.state = 227
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NEQ) | (1 << D96Parser.LT) | (1 << D96Parser.GT) | (1 << D96Parser.LTE) | (1 << D96Parser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.expr3(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.expr4(0) 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def RM(self):
            return self.getToken(D96Parser.RM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.RM))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 260
                    self.expr5() 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr5)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.NOT)
                self.state = 267
                self.expr5()
                pass
            elif token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.ID, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(D96Parser.SUB)
                self.state = 272
                self.expr6()
                pass
            elif token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 279
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 280
                    self.index_op() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = D96Parser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_index_op)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(D96Parser.LS)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(D96Parser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(D96Parser.LS)
                self.state = 291
                self.expr()
                self.state = 292
                self.match(D96Parser.RS)
                self.state = 293
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 312
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 300
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 301
                        self.match(D96Parser.DOT)
                        self.state = 302
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 303
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 304
                        self.match(D96Parser.DOT)
                        self.state = 305
                        self.match(D96Parser.ID)
                        self.state = 306
                        self.match(D96Parser.LB)
                        self.state = 309
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                            self.state = 307
                            self.exprlist()
                            pass
                        elif token in [D96Parser.RB]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 311
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr9)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(D96Parser.ID)
                self.state = 318
                self.match(D96Parser.ACCESS)
                self.state = 319
                self.match(D96Parser.SID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(D96Parser.ID)
                self.state = 321
                self.match(D96Parser.ACCESS)
                self.state = 322
                self.match(D96Parser.SID)
                self.state = 323
                self.match(D96Parser.LB)
                self.state = 326
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                    self.state = 324
                    self.exprlist()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 328
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 329
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr10)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(D96Parser.NEW)
                self.state = 333
                self.match(D96Parser.ID)
                self.state = 334
                self.match(D96Parser.LB)
                self.state = 337
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                    self.state = 335
                    self.exprlist()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 339
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.ID, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_operands)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(D96Parser.LB)
                self.state = 344
                self.expr()
                self.state = 345
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.literals()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 350
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assg_stm(self):
            return self.getTypedRuleContext(D96Parser.Assg_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(D96Parser.If_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(D96Parser.For_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(D96Parser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(D96Parser.Return_stmContext,0)


        def invocatoin_stm(self):
            return self.getTypedRuleContext(D96Parser.Invocatoin_stmContext,0)


        def decl_stm(self):
            return self.getTypedRuleContext(D96Parser.Decl_stmContext,0)


        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.assg_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.if_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.for_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.break_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 357
                self.continue_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 358
                self.return_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 359
                self.invocatoin_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 360
                self.decl_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 361
                self.blk_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def decl_stm_part(self):
            return self.getTypedRuleContext(D96Parser.Decl_stm_partContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def non_st_idlist(self):
            return self.getTypedRuleContext(D96Parser.Non_st_idlistContext,0)


        def IS(self):
            return self.getToken(D96Parser.IS, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decl_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stm" ):
                return visitor.visitDecl_stm(self)
            else:
                return visitor.visitChildren(self)




    def decl_stm(self):

        localctx = D96Parser.Decl_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_decl_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 365
                self.match(D96Parser.ID)
                self.state = 366
                self.decl_stm_part()
                self.state = 367
                self.expr()
                pass

            elif la_ == 2:
                self.state = 369
                self.non_st_idlist()
                self.state = 370
                self.match(D96Parser.IS)
                self.state = 371
                self.type_name()
                pass


            self.state = 375
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stm_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def decl_stm_part(self):
            return self.getTypedRuleContext(D96Parser.Decl_stm_partContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def IS(self):
            return self.getToken(D96Parser.IS, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def ASSG(self):
            return self.getToken(D96Parser.ASSG, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_decl_stm_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stm_part" ):
                return visitor.visitDecl_stm_part(self)
            else:
                return visitor.visitChildren(self)




    def decl_stm_part(self):

        localctx = D96Parser.Decl_stm_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_decl_stm_part)
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(D96Parser.COMMA)
                self.state = 378
                self.match(D96Parser.ID)
                self.state = 379
                self.decl_stm_part()
                self.state = 380
                self.expr()
                self.state = 381
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.IS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(D96Parser.IS)
                self.state = 384
                self.type_name()
                self.state = 385
                self.match(D96Parser.ASSG)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assg_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSG(self):
            return self.getToken(D96Parser.ASSG, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def index_op(self):
            return self.getTypedRuleContext(D96Parser.Index_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assg_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssg_stm" ):
                return visitor.visitAssg_stm(self)
            else:
                return visitor.visitChildren(self)




    def assg_stm(self):

        localctx = D96Parser.Assg_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assg_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 389
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 390
                self.expr()
                self.state = 391
                self.match(D96Parser.DOT)
                self.state = 392
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 394
                self.match(D96Parser.ID)
                self.state = 395
                self.match(D96Parser.ACCESS)
                self.state = 396
                self.match(D96Parser.SID)
                pass

            elif la_ == 4:
                self.state = 397
                self.expr()
                self.state = 398
                self.index_op()
                pass


            self.state = 402
            self.match(D96Parser.ASSG)
            self.state = 403
            self.expr()
            self.state = 404
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def else_if_stm(self):
            return self.getTypedRuleContext(D96Parser.Else_if_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = D96Parser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(D96Parser.IF)
            self.state = 407
            self.match(D96Parser.LB)
            self.state = 408
            self.expr()
            self.state = 409
            self.match(D96Parser.RB)
            self.state = 410
            self.blk_stmt()
            self.state = 411
            self.else_if_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def else_if_stm(self):
            return self.getTypedRuleContext(D96Parser.Else_if_stmContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_else_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_stm" ):
                return visitor.visitElse_if_stm(self)
            else:
                return visitor.visitChildren(self)




    def else_if_stm(self):

        localctx = D96Parser.Else_if_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_else_if_stm)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(D96Parser.ELSEIF)
                self.state = 414
                self.match(D96Parser.LB)
                self.state = 415
                self.expr()
                self.state = 416
                self.match(D96Parser.RB)
                self.state = 417
                self.blk_stmt()
                self.state = 418
                self.else_if_stm()
                pass
            elif token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(D96Parser.ELSE)
                self.state = 421
                self.blk_stmt()
                pass
            elif token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.RP]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blk_stmt(self):
            return self.getTypedRuleContext(D96Parser.Blk_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = D96Parser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(D96Parser.FOREACH)
            self.state = 426
            self.match(D96Parser.LB)
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 427
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 428
                self.expr()
                self.state = 429
                self.match(D96Parser.DOT)
                self.state = 430
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 432
                self.match(D96Parser.ID)
                self.state = 433
                self.match(D96Parser.ACCESS)
                self.state = 434
                self.match(D96Parser.SID)
                pass


            self.state = 437
            self.match(D96Parser.IN)
            self.state = 438
            self.expr()
            self.state = 439
            self.match(D96Parser.DOTDOT)
            self.state = 440
            self.expr()
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.state = 441
                self.match(D96Parser.BY)
                self.state = 442
                self.expr()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 446
            self.match(D96Parser.RB)
            self.state = 447
            self.blk_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = D96Parser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(D96Parser.BREAK)
            self.state = 450
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = D96Parser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(D96Parser.CONTINUE)
            self.state = 453
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = D96Parser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(D96Parser.RETURN)
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                self.state = 456
                self.expr()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 460
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocatoin_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_invocatoin_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocatoin_stm" ):
                return visitor.visitInvocatoin_stm(self)
            else:
                return visitor.visitChildren(self)




    def invocatoin_stm(self):

        localctx = D96Parser.Invocatoin_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_invocatoin_stm)
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.expr()
                self.state = 463
                self.match(D96Parser.DOT)
                self.state = 464
                self.match(D96Parser.ID)
                self.state = 465
                self.match(D96Parser.LB)
                self.state = 468
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                    self.state = 466
                    self.exprlist()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 470
                self.match(D96Parser.RB)
                self.state = 471
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.match(D96Parser.ID)
                self.state = 474
                self.match(D96Parser.ACCESS)
                self.state = 475
                self.match(D96Parser.SID)
                self.state = 476
                self.match(D96Parser.LB)
                self.state = 479
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                    self.state = 477
                    self.exprlist()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 481
                self.match(D96Parser.RB)
                self.state = 482
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Blk_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(D96Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_blk_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlk_stmt" ):
                return visitor.visitBlk_stmt(self)
            else:
                return visitor.visitChildren(self)




    def blk_stmt(self):

        localctx = D96Parser.Blk_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_blk_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(D96Parser.LP)
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB, D96Parser.LP]:
                self.state = 486
                self.stmtlist()
                pass
            elif token in [D96Parser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 490
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(D96Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = D96Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmtlist)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.stmt()
                self.state = 493
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_typ(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typContext,0)


        def array_typ(self):
            return self.getTypedRuleContext(D96Parser.Array_typContext,0)


        def class_typ(self):
            return self.getTypedRuleContext(D96Parser.Class_typContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_type_name)
        try:
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE, D96Parser.FLOATTYPE, D96Parser.BOOLTYPE, D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.primitive_typ()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.array_typ()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 500
                self.class_typ()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(D96Parser.BOOLTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_typ" ):
                return visitor.visitPrimitive_typ(self)
            else:
                return visitor.visitChildren(self)




    def primitive_typ(self):

        localctx = D96Parser.Primitive_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_primitive_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTTYPE) | (1 << D96Parser.FLOATTYPE) | (1 << D96Parser.BOOLTYPE) | (1 << D96Parser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INT_GT(self):
            return self.getToken(D96Parser.INT_GT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_typ" ):
                return visitor.visitArray_typ(self)
            else:
                return visitor.visitChildren(self)




    def array_typ(self):

        localctx = D96Parser.Array_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_typ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(D96Parser.ARRAY)
            self.state = 506
            self.match(D96Parser.LS)
            self.state = 507
            self.typ()
            self.state = 508
            self.match(D96Parser.COMMA)
            self.state = 509
            self.match(D96Parser.INT_GT)
            self.state = 510
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_typ(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typContext,0)


        def array_typ(self):
            return self.getTypedRuleContext(D96Parser.Array_typContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typ)
        try:
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE, D96Parser.FLOATTYPE, D96Parser.BOOLTYPE, D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.primitive_typ()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.array_typ()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_typ" ):
                return visitor.visitClass_typ(self)
            else:
                return visitor.visitChildren(self)




    def class_typ(self):

        localctx = D96Parser.Class_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_class_typ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def INT_GT(self):
            return self.getToken(D96Parser.INT_GT, 0)

        def INT_ZERO(self):
            return self.getToken(D96Parser.INT_ZERO, 0)

        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def BOOL(self):
            return self.getToken(D96Parser.BOOL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literals)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.INT_GT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(D96Parser.INT_GT)
                pass
            elif token in [D96Parser.INT_ZERO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 520
                self.match(D96Parser.INT_ZERO)
                pass
            elif token in [D96Parser.STR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 521
                self.match(D96Parser.STR)
                pass
            elif token in [D96Parser.BOOL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 522
                self.match(D96Parser.BOOL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 523
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idxlit(self):
            return self.getTypedRuleContext(D96Parser.IdxlitContext,0)


        def mullit(self):
            return self.getTypedRuleContext(D96Parser.MullitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_literal)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.idxlit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.mullit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(D96Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idxlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxlit" ):
                return visitor.visitIdxlit(self)
            else:
                return visitor.visitChildren(self)




    def idxlit(self):

        localctx = D96Parser.IdxlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_idxlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(D96Parser.ARRAY)
            self.state = 531
            self.match(D96Parser.LB)
            self.state = 534
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOL, D96Parser.STR, D96Parser.FLOAT, D96Parser.INT_ZERO, D96Parser.INT_GT, D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.ID, D96Parser.LB]:
                self.state = 532
                self.exprlist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 536
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MullitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def arrlist(self):
            return self.getTypedRuleContext(D96Parser.ArrlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mullit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMullit" ):
                return visitor.visitMullit(self)
            else:
                return visitor.visitChildren(self)




    def mullit(self):

        localctx = D96Parser.MullitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_mullit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(D96Parser.ARRAY)
            self.state = 539
            self.match(D96Parser.LB)
            self.state = 540
            self.arrlist()
            self.state = 541
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr(self):
            return self.getTypedRuleContext(D96Parser.ArrContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def arrlist(self):
            return self.getTypedRuleContext(D96Parser.ArrlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlist" ):
                return visitor.visitArrlist(self)
            else:
                return visitor.visitChildren(self)




    def arrlist(self):

        localctx = D96Parser.ArrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arrlist)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.arr()
                self.state = 544
                self.match(D96Parser.COMMA)
                self.state = 545
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
                self.arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idxlit(self):
            return self.getTypedRuleContext(D96Parser.IdxlitContext,0)


        def mullit(self):
            return self.getTypedRuleContext(D96Parser.MullitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr" ):
                return visitor.visitArr(self)
            else:
                return visitor.visitChildren(self)




    def arr(self):

        localctx = D96Parser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arr)
        try:
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.idxlit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.mullit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr2_sempred
        self._predicates[18] = self.expr3_sempred
        self._predicates[19] = self.expr4_sempred
        self._predicates[22] = self.expr7_sempred
        self._predicates[24] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




