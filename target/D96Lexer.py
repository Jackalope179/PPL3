# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0240\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\5\2\u009a\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u00ae\n\3\f\3")
        buf.write("\16\3\u00b1\13\3\3\3\3\3\3\3\3\3\3\4\3\4\5\4\u00b9\n\4")
        buf.write("\3\5\3\5\7\5\u00bd\n\5\f\5\16\5\u00c0\13\5\3\6\3\6\5\6")
        buf.write("\u00c4\n\6\3\6\6\6\u00c7\n\6\r\6\16\6\u00c8\3\7\3\7\3")
        buf.write("\7\5\7\u00ce\n\7\3\7\3\7\5\7\u00d2\n\7\3\7\3\7\5\7\u00d6")
        buf.write("\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00e3")
        buf.write("\n\b\3\t\3\t\3\t\3\t\5\t\u00e9\n\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\7\n\u00f1\n\n\f\n\16\n\u00f4\13\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u00fc\n\13\f\13\16\13\u00ff\13\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\7\f\u0106\n\f\f\f\16\f\u0109\13\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0111\n\r\f\r\16\r\u0114")
        buf.write("\13\r\3\16\3\16\3\16\3\16\7\16\u011a\n\16\f\16\16\16\u011d")
        buf.write("\13\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\39\39\79\u01e4")
        buf.write("\n9\f9\169\u01e7\139\3:\3:\6:\u01eb\n:\r:\16:\u01ec\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\3")
        buf.write("C\3D\3D\3E\3E\3F\6F\u0207\nF\rF\16F\u0208\3F\3F\3G\3G")
        buf.write("\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u021e")
        buf.write("\nG\3H\5H\u0221\nH\3I\3I\7I\u0225\nI\fI\16I\u0228\13I")
        buf.write("\3I\3I\3I\3J\3J\7J\u022f\nJ\fJ\16J\u0232\13J\3J\3J\5J")
        buf.write("\u0236\nJ\3J\3J\5J\u023a\nJ\3J\3J\3K\3K\3K\3\u011b\2L")
        buf.write("\3\3\5\4\7\2\t\2\13\2\r\5\17\6\21\7\23\b\25\t\27\n\31")
        buf.write("\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61")
        buf.write("\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M")
        buf.write("%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67")
        buf.write("s8u9w:y;{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089C\u008b")
        buf.write("D\u008d\2\u008f\2\u0091E\u0093F\u0095G\3\2\26\6\2\n\f")
        buf.write("\16\17$$^^\3\2\62;\4\2GGgg\4\2--//\4\2ZZzz\4\2DDdd\3\2")
        buf.write("\63;\3\2aa\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3\2\63")
        buf.write("\63\3\2\62\63\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17")
        buf.write("\"\"\4\3\n\f\16\17\t\2))^^ddhhppttvv\3\2$$\2\u0269\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2")
        buf.write("\2\7\u00b8\3\2\2\2\t\u00ba\3\2\2\2\13\u00c1\3\2\2\2\r")
        buf.write("\u00d5\3\2\2\2\17\u00e2\3\2\2\2\21\u00e8\3\2\2\2\23\u00ec")
        buf.write("\3\2\2\2\25\u00f5\3\2\2\2\27\u0100\3\2\2\2\31\u010a\3")
        buf.write("\2\2\2\33\u0115\3\2\2\2\35\u0123\3\2\2\2\37\u0128\3\2")
        buf.write("\2\2!\u012e\3\2\2\2#\u0137\3\2\2\2%\u013a\3\2\2\2\'\u0141")
        buf.write("\3\2\2\2)\u0146\3\2\2\2+\u014e\3\2\2\2-\u0153\3\2\2\2")
        buf.write("/\u0159\3\2\2\2\61\u015f\3\2\2\2\63\u0162\3\2\2\2\65\u0166")
        buf.write("\3\2\2\2\67\u016c\3\2\2\29\u0174\3\2\2\2;\u017b\3\2\2")
        buf.write("\2=\u0182\3\2\2\2?\u0187\3\2\2\2A\u018d\3\2\2\2C\u0191")
        buf.write("\3\2\2\2E\u0195\3\2\2\2G\u01a1\3\2\2\2I\u01ac\3\2\2\2")
        buf.write("K\u01b0\3\2\2\2M\u01b3\3\2\2\2O\u01b5\3\2\2\2Q\u01b7\3")
        buf.write("\2\2\2S\u01b9\3\2\2\2U\u01bb\3\2\2\2W\u01bd\3\2\2\2Y\u01bf")
        buf.write("\3\2\2\2[\u01c2\3\2\2\2]\u01c5\3\2\2\2_\u01c8\3\2\2\2")
        buf.write("a\u01ca\3\2\2\2c\u01cd\3\2\2\2e\u01cf\3\2\2\2g\u01d1\3")
        buf.write("\2\2\2i\u01d4\3\2\2\2k\u01d7\3\2\2\2m\u01da\3\2\2\2o\u01de")
        buf.write("\3\2\2\2q\u01e1\3\2\2\2s\u01e8\3\2\2\2u\u01ee\3\2\2\2")
        buf.write("w\u01f0\3\2\2\2y\u01f2\3\2\2\2{\u01f4\3\2\2\2}\u01f6\3")
        buf.write("\2\2\2\177\u01f8\3\2\2\2\u0081\u01fa\3\2\2\2\u0083\u01fc")
        buf.write("\3\2\2\2\u0085\u01ff\3\2\2\2\u0087\u0201\3\2\2\2\u0089")
        buf.write("\u0203\3\2\2\2\u008b\u0206\3\2\2\2\u008d\u021d\3\2\2\2")
        buf.write("\u008f\u0220\3\2\2\2\u0091\u0222\3\2\2\2\u0093\u022c\3")
        buf.write("\2\2\2\u0095\u023d\3\2\2\2\u0097\u009a\5+\26\2\u0098\u009a")
        buf.write("\5-\27\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\4\3\2\2\2\u009b\u00af\7$\2\2\u009c\u009d\7^\2\2\u009d")
        buf.write("\u00ae\7d\2\2\u009e\u009f\7^\2\2\u009f\u00ae\7h\2\2\u00a0")
        buf.write("\u00a1\7^\2\2\u00a1\u00ae\7t\2\2\u00a2\u00a3\7^\2\2\u00a3")
        buf.write("\u00ae\7p\2\2\u00a4\u00a5\7^\2\2\u00a5\u00ae\7v\2\2\u00a6")
        buf.write("\u00a7\7^\2\2\u00a7\u00ae\7)\2\2\u00a8\u00a9\7^\2\2\u00a9")
        buf.write("\u00ae\7^\2\2\u00aa\u00ab\7)\2\2\u00ab\u00ae\7$\2\2\u00ac")
        buf.write("\u00ae\n\2\2\2\u00ad\u009c\3\2\2\2\u00ad\u009e\3\2\2\2")
        buf.write("\u00ad\u00a0\3\2\2\2\u00ad\u00a2\3\2\2\2\u00ad\u00a4\3")
        buf.write("\2\2\2\u00ad\u00a6\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00aa")
        buf.write("\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b2\u00b3\7$\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b5\b\3\2\2\u00b5\6\3\2\2\2\u00b6\u00b9")
        buf.write("\7\62\2\2\u00b7\u00b9\5\23\n\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\b\3\2\2\2\u00ba\u00be\7\60\2\2\u00bb")
        buf.write("\u00bd\t\3\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\n\3\2\2")
        buf.write("\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\t\4\2\2\u00c2\u00c4")
        buf.write("\t\5\2\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c6\3\2\2\2\u00c5\u00c7\t\3\2\2\u00c6\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3")
        buf.write("\2\2\2\u00c9\f\3\2\2\2\u00ca\u00cb\5\7\4\2\u00cb\u00cd")
        buf.write("\5\t\5\2\u00cc\u00ce\5\13\6\2\u00cd\u00cc\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00d6\3\2\2\2\u00cf\u00d2\5\7\4\2")
        buf.write("\u00d0\u00d2\5\t\5\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\5\13\6\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00ca\3\2\2\2\u00d5\u00d1\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00d8\b\7\3\2\u00d8\16\3\2")
        buf.write("\2\2\u00d9\u00e3\7\62\2\2\u00da\u00db\7\62\2\2\u00db\u00dc")
        buf.write("\t\6\2\2\u00dc\u00e3\7\62\2\2\u00dd\u00de\7\62\2\2\u00de")
        buf.write("\u00df\t\7\2\2\u00df\u00e3\7\62\2\2\u00e0\u00e1\7\62\2")
        buf.write("\2\u00e1\u00e3\7\62\2\2\u00e2\u00d9\3\2\2\2\u00e2\u00da")
        buf.write("\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3")
        buf.write("\20\3\2\2\2\u00e4\u00e9\5\23\n\2\u00e5\u00e9\5\25\13\2")
        buf.write("\u00e6\u00e9\5\27\f\2\u00e7\u00e9\5\31\r\2\u00e8\u00e4")
        buf.write("\3\2\2\2\u00e8\u00e5\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\b\t\4\2")
        buf.write("\u00eb\22\3\2\2\2\u00ec\u00f2\t\b\2\2\u00ed\u00ee\t\t")
        buf.write("\2\2\u00ee\u00f1\t\3\2\2\u00ef\u00f1\t\3\2\2\u00f0\u00ed")
        buf.write("\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\24\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f6\7\62\2\2\u00f6\u00f7\t\6\2")
        buf.write("\2\u00f7\u00fd\t\n\2\2\u00f8\u00f9\t\t\2\2\u00f9\u00fc")
        buf.write("\t\13\2\2\u00fa\u00fc\t\13\2\2\u00fb\u00f8\3\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\26\3\2\2\2\u00ff\u00fd\3\2")
        buf.write("\2\2\u0100\u0101\7\62\2\2\u0101\u0107\t\f\2\2\u0102\u0103")
        buf.write("\t\t\2\2\u0103\u0106\t\r\2\2\u0104\u0106\t\r\2\2\u0105")
        buf.write("\u0102\3\2\2\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\30\3\2")
        buf.write("\2\2\u0109\u0107\3\2\2\2\u010a\u010b\7\62\2\2\u010b\u010c")
        buf.write("\t\7\2\2\u010c\u0112\t\16\2\2\u010d\u010e\t\t\2\2\u010e")
        buf.write("\u0111\t\17\2\2\u010f\u0111\t\17\2\2\u0110\u010d\3\2\2")
        buf.write("\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\32\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0115\u0116\7%\2\2\u0116\u0117\7%\2\2\u0117\u011b")
        buf.write("\3\2\2\2\u0118\u011a\13\2\2\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u011c\3\2\2\2\u011b\u0119\3\2\2\2")
        buf.write("\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7")
        buf.write("%\2\2\u011f\u0120\7%\2\2\u0120\u0121\3\2\2\2\u0121\u0122")
        buf.write("\b\16\5\2\u0122\34\3\2\2\2\u0123\u0124\7U\2\2\u0124\u0125")
        buf.write("\7g\2\2\u0125\u0126\7n\2\2\u0126\u0127\7h\2\2\u0127\36")
        buf.write("\3\2\2\2\u0128\u0129\7D\2\2\u0129\u012a\7t\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b\u012c\7c\2\2\u012c\u012d\7m\2\2\u012d \3")
        buf.write("\2\2\2\u012e\u012f\7E\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7p\2\2\u0131\u0132\7v\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7p\2\2\u0134\u0135\7w\2\2\u0135\u0136\7g\2\2\u0136\"")
        buf.write("\3\2\2\2\u0137\u0138\7K\2\2\u0138\u0139\7h\2\2\u0139$")
        buf.write("\3\2\2\2\u013a\u013b\7G\2\2\u013b\u013c\7n\2\2\u013c\u013d")
        buf.write("\7u\2\2\u013d\u013e\7g\2\2\u013e\u013f\7k\2\2\u013f\u0140")
        buf.write("\7h\2\2\u0140&\3\2\2\2\u0141\u0142\7G\2\2\u0142\u0143")
        buf.write("\7n\2\2\u0143\u0144\7u\2\2\u0144\u0145\7g\2\2\u0145(\3")
        buf.write("\2\2\2\u0146\u0147\7H\2\2\u0147\u0148\7q\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7g\2\2\u014a\u014b\7c\2\2\u014b\u014c")
        buf.write("\7e\2\2\u014c\u014d\7j\2\2\u014d*\3\2\2\2\u014e\u014f")
        buf.write("\7V\2\2\u014f\u0150\7t\2\2\u0150\u0151\7w\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152,\3\2\2\2\u0153\u0154\7H\2\2\u0154\u0155")
        buf.write("\7c\2\2\u0155\u0156\7n\2\2\u0156\u0157\7u\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158.\3\2\2\2\u0159\u015a\7C\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015b\u015c\7t\2\2\u015c\u015d\7c\2\2\u015d\u015e")
        buf.write("\7{\2\2\u015e\60\3\2\2\2\u015f\u0160\7K\2\2\u0160\u0161")
        buf.write("\7p\2\2\u0161\62\3\2\2\2\u0162\u0163\7K\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164\u0165\7v\2\2\u0165\64\3\2\2\2\u0166\u0167")
        buf.write("\7H\2\2\u0167\u0168\7n\2\2\u0168\u0169\7q\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7v\2\2\u016b\66\3\2\2\2\u016c\u016d")
        buf.write("\7D\2\2\u016d\u016e\7q\2\2\u016e\u016f\7q\2\2\u016f\u0170")
        buf.write("\7n\2\2\u0170\u0171\7g\2\2\u0171\u0172\7c\2\2\u0172\u0173")
        buf.write("\7p\2\2\u01738\3\2\2\2\u0174\u0175\7U\2\2\u0175\u0176")
        buf.write("\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178\7k\2\2\u0178\u0179")
        buf.write("\7p\2\2\u0179\u017a\7i\2\2\u017a:\3\2\2\2\u017b\u017c")
        buf.write("\7T\2\2\u017c\u017d\7g\2\2\u017d\u017e\7v\2\2\u017e\u017f")
        buf.write("\7w\2\2\u017f\u0180\7t\2\2\u0180\u0181\7p\2\2\u0181<\3")
        buf.write("\2\2\2\u0182\u0183\7P\2\2\u0183\u0184\7w\2\2\u0184\u0185")
        buf.write("\7n\2\2\u0185\u0186\7n\2\2\u0186>\3\2\2\2\u0187\u0188")
        buf.write("\7E\2\2\u0188\u0189\7n\2\2\u0189\u018a\7c\2\2\u018a\u018b")
        buf.write("\7u\2\2\u018b\u018c\7u\2\2\u018c@\3\2\2\2\u018d\u018e")
        buf.write("\7X\2\2\u018e\u018f\7c\2\2\u018f\u0190\7n\2\2\u0190B\3")
        buf.write("\2\2\2\u0191\u0192\7X\2\2\u0192\u0193\7c\2\2\u0193\u0194")
        buf.write("\7t\2\2\u0194D\3\2\2\2\u0195\u0196\7E\2\2\u0196\u0197")
        buf.write("\7q\2\2\u0197\u0198\7p\2\2\u0198\u0199\7u\2\2\u0199\u019a")
        buf.write("\7v\2\2\u019a\u019b\7t\2\2\u019b\u019c\7w\2\2\u019c\u019d")
        buf.write("\7e\2\2\u019d\u019e\7v\2\2\u019e\u019f\7q\2\2\u019f\u01a0")
        buf.write("\7t\2\2\u01a0F\3\2\2\2\u01a1\u01a2\7F\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6")
        buf.write("\7t\2\2\u01a6\u01a7\7w\2\2\u01a7\u01a8\7e\2\2\u01a8\u01a9")
        buf.write("\7v\2\2\u01a9\u01aa\7q\2\2\u01aa\u01ab\7t\2\2\u01abH\3")
        buf.write("\2\2\2\u01ac\u01ad\7P\2\2\u01ad\u01ae\7g\2\2\u01ae\u01af")
        buf.write("\7y\2\2\u01afJ\3\2\2\2\u01b0\u01b1\7D\2\2\u01b1\u01b2")
        buf.write("\7{\2\2\u01b2L\3\2\2\2\u01b3\u01b4\7-\2\2\u01b4N\3\2\2")
        buf.write("\2\u01b5\u01b6\7/\2\2\u01b6P\3\2\2\2\u01b7\u01b8\7,\2")
        buf.write("\2\u01b8R\3\2\2\2\u01b9\u01ba\7\61\2\2\u01baT\3\2\2\2")
        buf.write("\u01bb\u01bc\7\'\2\2\u01bcV\3\2\2\2\u01bd\u01be\7#\2\2")
        buf.write("\u01beX\3\2\2\2\u01bf\u01c0\7(\2\2\u01c0\u01c1\7(\2\2")
        buf.write("\u01c1Z\3\2\2\2\u01c2\u01c3\7~\2\2\u01c3\u01c4\7~\2\2")
        buf.write("\u01c4\\\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6\u01c7\7?\2\2")
        buf.write("\u01c7^\3\2\2\2\u01c8\u01c9\7?\2\2\u01c9`\3\2\2\2\u01ca")
        buf.write("\u01cb\7#\2\2\u01cb\u01cc\7?\2\2\u01ccb\3\2\2\2\u01cd")
        buf.write("\u01ce\7>\2\2\u01ced\3\2\2\2\u01cf\u01d0\7@\2\2\u01d0")
        buf.write("f\3\2\2\2\u01d1\u01d2\7>\2\2\u01d2\u01d3\7?\2\2\u01d3")
        buf.write("h\3\2\2\2\u01d4\u01d5\7@\2\2\u01d5\u01d6\7?\2\2\u01d6")
        buf.write("j\3\2\2\2\u01d7\u01d8\7-\2\2\u01d8\u01d9\7\60\2\2\u01d9")
        buf.write("l\3\2\2\2\u01da\u01db\7?\2\2\u01db\u01dc\7?\2\2\u01dc")
        buf.write("\u01dd\7\60\2\2\u01ddn\3\2\2\2\u01de\u01df\7<\2\2\u01df")
        buf.write("\u01e0\7<\2\2\u01e0p\3\2\2\2\u01e1\u01e5\t\20\2\2\u01e2")
        buf.write("\u01e4\t\21\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2")
        buf.write("\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6r\3\2")
        buf.write("\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea\7&\2\2\u01e9\u01eb")
        buf.write("\t\21\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01edt\3\2\2\2\u01ee")
        buf.write("\u01ef\7*\2\2\u01efv\3\2\2\2\u01f0\u01f1\7+\2\2\u01f1")
        buf.write("x\3\2\2\2\u01f2\u01f3\7}\2\2\u01f3z\3\2\2\2\u01f4\u01f5")
        buf.write("\7\177\2\2\u01f5|\3\2\2\2\u01f6\u01f7\7=\2\2\u01f7~\3")
        buf.write("\2\2\2\u01f8\u01f9\7]\2\2\u01f9\u0080\3\2\2\2\u01fa\u01fb")
        buf.write("\7_\2\2\u01fb\u0082\3\2\2\2\u01fc\u01fd\7\60\2\2\u01fd")
        buf.write("\u01fe\7\60\2\2\u01fe\u0084\3\2\2\2\u01ff\u0200\7\60\2")
        buf.write("\2\u0200\u0086\3\2\2\2\u0201\u0202\7.\2\2\u0202\u0088")
        buf.write("\3\2\2\2\u0203\u0204\7<\2\2\u0204\u008a\3\2\2\2\u0205")
        buf.write("\u0207\t\22\2\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2")
        buf.write("\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\bF\5\2\u020b\u008c\3\2\2\2\u020c")
        buf.write("\u020d\7^\2\2\u020d\u021e\7d\2\2\u020e\u020f\7^\2\2\u020f")
        buf.write("\u021e\7h\2\2\u0210\u0211\7^\2\2\u0211\u021e\7t\2\2\u0212")
        buf.write("\u0213\7^\2\2\u0213\u021e\7p\2\2\u0214\u0215\7^\2\2\u0215")
        buf.write("\u021e\7v\2\2\u0216\u0217\7^\2\2\u0217\u021e\7)\2\2\u0218")
        buf.write("\u0219\7^\2\2\u0219\u021e\7^\2\2\u021a\u021b\7)\2\2\u021b")
        buf.write("\u021e\7$\2\2\u021c\u021e\n\2\2\2\u021d\u020c\3\2\2\2")
        buf.write("\u021d\u020e\3\2\2\2\u021d\u0210\3\2\2\2\u021d\u0212\3")
        buf.write("\2\2\2\u021d\u0214\3\2\2\2\u021d\u0216\3\2\2\2\u021d\u0218")
        buf.write("\3\2\2\2\u021d\u021a\3\2\2\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("\u008e\3\2\2\2\u021f\u0221\t\23\2\2\u0220\u021f\3\2\2")
        buf.write("\2\u0221\u0090\3\2\2\2\u0222\u0226\7$\2\2\u0223\u0225")
        buf.write("\5\u008dG\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2")
        buf.write("\u0228\u0226\3\2\2\2\u0229\u022a\5\u008fH\2\u022a\u022b")
        buf.write("\bI\6\2\u022b\u0092\3\2\2\2\u022c\u0230\7$\2\2\u022d\u022f")
        buf.write("\5\u008dG\2\u022e\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230")
        buf.write("\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0239\3\2\2\2")
        buf.write("\u0232\u0230\3\2\2\2\u0233\u0235\7^\2\2\u0234\u0236\n")
        buf.write("\24\2\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write("\u023a\3\2\2\2\u0237\u0238\7)\2\2\u0238\u023a\n\25\2\2")
        buf.write("\u0239\u0233\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\3")
        buf.write("\2\2\2\u023b\u023c\bJ\7\2\u023c\u0094\3\2\2\2\u023d\u023e")
        buf.write("\13\2\2\2\u023e\u023f\bK\b\2\u023f\u0096\3\2\2\2!\2\u0099")
        buf.write("\u00ad\u00af\u00b8\u00be\u00c3\u00c8\u00cd\u00d1\u00d5")
        buf.write("\u00e2\u00e8\u00f0\u00f2\u00fb\u00fd\u0105\u0107\u0110")
        buf.write("\u0112\u011b\u01e5\u01ec\u0208\u021d\u0220\u0226\u0230")
        buf.write("\u0235\u0239\t\3\3\2\3\7\3\3\t\4\b\2\2\3I\5\3J\6\3K\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL = 1
    STR = 2
    FLOAT = 3
    INT_ZERO = 4
    INT_GT = 5
    DEC_GT = 6
    HEX_GT = 7
    OCTAL_GT = 8
    BINARY_GT = 9
    COMMENT = 10
    SELF = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSEIF = 15
    ELSE = 16
    FOREACH = 17
    TRUE = 18
    FALSE = 19
    ARRAY = 20
    IN = 21
    INTTYPE = 22
    FLOATTYPE = 23
    BOOLTYPE = 24
    STRINGTYPE = 25
    RETURN = 26
    NULL = 27
    CLASS = 28
    VAL = 29
    VAR = 30
    CONSTRUCTOR = 31
    DESTRUCTOR = 32
    NEW = 33
    BY = 34
    ADD = 35
    SUB = 36
    MUL = 37
    DIV = 38
    RM = 39
    NOT = 40
    AND = 41
    OR = 42
    EQ = 43
    ASSG = 44
    NEQ = 45
    LT = 46
    GT = 47
    LTE = 48
    GTE = 49
    STR_CONCAT = 50
    STR_COMPARE = 51
    ACCESS = 52
    ID = 53
    SID = 54
    LB = 55
    RB = 56
    LP = 57
    RP = 58
    SEMI = 59
    LS = 60
    RS = 61
    DOTDOT = 62
    DOT = 63
    COMMA = 64
    IS = 65
    WS = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    ERROR_TOKEN = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Self'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+.'", 
            "'==.'", "'::'", "'('", "')'", "'{'", "'}'", "';'", "'['", "']'", 
            "'..'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "STR", "FLOAT", "INT_ZERO", "INT_GT", "DEC_GT", "HEX_GT", 
            "OCTAL_GT", "BINARY_GT", "COMMENT", "SELF", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
            "IN", "INTTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "RETURN", 
            "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "RM", "NOT", "AND", 
            "OR", "EQ", "ASSG", "NEQ", "LT", "GT", "LTE", "GTE", "STR_CONCAT", 
            "STR_COMPARE", "ACCESS", "ID", "SID", "LB", "RB", "LP", "RP", 
            "SEMI", "LS", "RS", "DOTDOT", "DOT", "COMMA", "IS", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "BOOL", "STR", "INTPART", "DECIMALPART", "EXPART", "FLOAT", 
                  "INT_ZERO", "INT_GT", "DEC_GT", "HEX_GT", "OCTAL_GT", 
                  "BINARY_GT", "COMMENT", "SELF", "BREAK", "CONTINUE", "IF", 
                  "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INTTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", 
                  "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", 
                  "RM", "NOT", "AND", "OR", "EQ", "ASSG", "NEQ", "LT", "GT", 
                  "LTE", "GTE", "STR_CONCAT", "STR_COMPARE", "ACCESS", "ID", 
                  "SID", "LB", "RB", "LP", "RP", "SEMI", "LS", "RS", "DOTDOT", 
                  "DOT", "COMMA", "IS", "WS", "CHARACTERS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.STR_action 
            actions[5] = self.FLOAT_action 
            actions[7] = self.INT_GT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1];

     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_', '');

     

    def INT_GT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text.replace('_', '');

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	if self.text[-1] in ['\n', '\r', '\t', '\b', '\f']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise  ErrorToken(self.text)
     


