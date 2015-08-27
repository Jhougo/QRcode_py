# -*- coding: utf-8 -*-
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' //|     |// '.
#                 / //|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | //  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永無BUG
from qrcode import *
import wx
import wx.lib.filebrowsebutton as filebrowse
import time
piece11 = []
#########################################
class TestPaneldis(wx.Panel):
    def listpath(e,dirpath): 
        tStart = time.time()
    	f = open(dirpath,'r')
    	for line in f.readlines():
    	    print line
            piece11.append(line)
    	f.close()
        qrcommit(piece11,dirpath)
        tEnd = time.time()
        print "Success"
        print " spend  "+str((tEnd - tStart)//1)+"  second" 
                        
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent)
        self.log = log
        self.dbb = filebrowse.FileBrowseButton(self, -1, size=(450, -1), buttonText=u'瀏覽', labelText=u'文字檔根目錄:', changeCallback = self.dbbCallback)
        b = wx.Button(self, 40, u'RUN', (500,28), style=wx.NO_BORDER)
        b.SetToolTipString("Run QRcode\n") 
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        sizer = wx.BoxSizer(wx.VERTICAL)        
        sizer.Add(self.dbb, 0, wx.ALL, 5)
        box = wx.BoxSizer()
        box.Add(sizer, 0, wx.ALL, 20)
        b.SetInitialSize()  
        self.SetSizer(box)
    def dbbCallback(self, event):
        Dir = self.dbb.GetValue()
        self.path = Dir
        event.Skip()
    def OnClick(self, event):    
        self.listpath(self.path)
        

class Framedis ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"QRcode", pos = wx.DefaultPosition, size = wx.Size(700,150))
        panel = TestPaneldis(self, -1)

class App(wx.App):
    def OnInit(self):
        self.frame = Framedis(parent=None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
###########################################################################




def qrcommit(data,filenamepath):
    for x in piece11:
    	qr = QRCode(version=20, error_correction=ERROR_CORRECT_H)
    	qr.add_data(x)
    	qr.make() # Generate the QRCode itself
    	# im contains a PIL.Image.Image object
    	im = qr.make_image()
    	# To save it
    	im.save(filenamepath[0:filenamepath.rfind('/')+1].decode('UTF-8').strip()+x.decode('UTF-8').strip()+'.png')
if __name__ == '__main__':
    app = App()
    app.MainLoop()
