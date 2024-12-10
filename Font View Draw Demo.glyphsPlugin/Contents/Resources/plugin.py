import objc
from AppKit import (
    NSColor,
    NSRectFill,
)
from GlyphsApp import (
    Glyphs,
    GSCallbackHandler,
)
from GlyphsApp.plugins import GeneralPlugin


class FontViewDrawDemo(GeneralPlugin):
    @objc.python_method
    def settings(self):
        self.name = "Font View Draw Demo"

    @objc.python_method
    def start(self):
        GSCallbackHandler.addCallback_forOperation_(self, "DrawFontView")

    @objc.signature(b'v@:@{CGRect={CGPoint=dd}{CGSize=dd}}')
    def drawFontViewBackgroundForLayer_inFrame_(self, layer, frame):
        NSColor.yellowColor().setFill()
        NSRectFill(frame)

    @ objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
