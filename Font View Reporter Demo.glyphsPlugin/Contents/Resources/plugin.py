import objc
from AppKit import (
    NSColor,
    NSRectFill,
)
from GlyphsApp import (
    Glyphs,
    GSCallbackHandler,
)
from GlyphsApp.plugins import ReporterPlugin


class FontViewReporterDemo(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = "Font View Reporter Demo"

    @objc.python_method
    def start(self):
        GSCallbackHandler.addCallback_forOperation_(self, "DrawFontView")

    @objc.signature(b'v@:@{CGRect={CGPoint=dd}{CGSize=dd}}')
    def drawFontViewBackgroundForLayer_inFrame_(self, layer, frame):
        NSColor.blueColor().setFill()
        NSRectFill(frame)

    @ objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
