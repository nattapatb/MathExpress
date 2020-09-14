import wx
from wx import *

import vlc
from lexicalAnal import *

s = ""
soundList = []
speakRate = 1.00
verbosity = 'verbose'

class MathExpressPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        font_courier_20 = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.BOLD, faceName="Courier New")
        font_courier_16 = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.BOLD, faceName="Courier New")
        font_roman_30 = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.BOLD, faceName="Times New Roman")
        font_roman_16 = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.BOLD, faceName="Times New Roman")
        font_sarabun_20 = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL, faceName="TH SarabunPSK")

        header = wx.StaticText(self, label="MathExpress v.2.1.1", pos=(20, 30))
        header.SetFont(font_roman_30)
        self.header = header

        LaTeX_label = wx.StaticText(self, label="LaTeX:", pos=(20,100))
        LaTeX_label.SetFont(font_courier_20)
        self.lblname = LaTeX_label
        LaTeX_field = wx.TextCtrl(self, value="", pos=(120, 100), size=(300,100), style=wx.TE_MULTILINE)
        LaTeX_field.SetFont(font_courier_16)
        self.editname = LaTeX_field

        #self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)

        # Spell button
        self.spell_button =wx.Button(self, label="Spell", pos=(450, 100))
        self.Bind(wx.EVT_BUTTON, self.OnClick_spell,self.spell_button)

        # Verbosity -- Radio Boxes
        radioList = ['verbose', 'brief', 'superbrief']
        self.rb_verbosity = wx.RadioBox(self, label="Verbosity", pos=(450, 130), choices=radioList,  majorDimension=2,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox_verbosity, self.rb_verbosity)

        # Thai Spelling
        quote_thai = wx.StaticText(self, label = "Thai Spelling:", pos=(20, 220))
        quote_thai.SetFont(font_roman_16)
        self.quote_thai = quote_thai

        self.thaiText = wx.TextCtrl(self, value = "", pos=(120, 220), size=(300,100),style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.thaiText.SetFont(font_sarabun_20)

        # Speak Button
        self.speak_button =wx.Button(self, label="Speak", pos=(450, 220))
        self.Bind(wx.EVT_BUTTON, self.OnClick_speak,self.speak_button)

        # Speed -- Radio Boxes
        radioList = ['1.00', '1.50', '2.00', '2.50', '3.00', '3.50', '4.00']
        self.rb_speed = wx.RadioBox(self, label="Playback Speed", pos=(450, 250), choices=radioList,  majorDimension=2,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox_speed, self.rb_speed)

    def OnClick_spell(self,event):
        latex = self.editname.GetValue()
        tokens = lexAnal(latex, verbosity = verbosity)
        thais = extractThai(tokens)
        soundList = cleanTokens(extractSounds(tokens))
        s = ''.join(cleanTokens(thais))
        self.thaiText.SetValue(s)
        print(soundList)
        composeSpeech(soundList, silenceDuration = 400)

    def OnClick_speak(self, event):
        player = vlc.MediaPlayer("../example.wav")
        player.set_rate(rate = speakRate)
        player.play()

    def EvtRadioBox_verbosity(self, event):
        global verbosity
        verbosity = str(self.rb_verbosity.GetStringSelection())
        print('verbosity =',verbosity)

        # ----- update Thai Spelling ------
        latex = self.editname.GetValue()
        tokens = lexAnal(latex, verbosity = verbosity)
        thais = extractThai(tokens)
        soundList = cleanTokens(extractSounds(tokens))
        s = ''.join(cleanTokens(thais))
        self.thaiText.SetValue(s)
        print(soundList)
        composeSpeech(soundList, silenceDuration = 400)

    def EvtRadioBox_speed(self, event):
        global speakRate
        speakRate = float(self.rb_speed.GetStringSelection())
        print('rate =',speakRate)
        player = vlc.MediaPlayer("../example.wav")
        player.set_rate(rate = speakRate)

app = wx.App(False)
frame = wx.Frame(None, size=(650,400))
panel = MathExpressPanel(frame)
frame.Show()
app.MainLoop()
