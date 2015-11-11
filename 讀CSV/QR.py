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
import csv
import os
piece11 = []
piece12 = []
name = []
a = 0
#########################################
class TestPaneldis(wx.Panel):
    def listpath(e,dirpath):
        a = 0
        tStart = time.time()
        with open(dirpath, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, dialect='excel')
            for row in spamreader:
                if a != 0:
                    name.append(row[0])
                    piece11.append(row[16])
                    piece12.append(row[17])
                a += 1
        ise = os.path.exists(dirpath.replace('.csv',''))
        if not ise:
            os.mkdir(dirpath.replace('.csv',''))
<<<<<<< HEAD
        qrcommit(piece11,piece12,dirpath,name)
        tEnd = time.time()
        print "Success"
        print " spend  "+str((tEnd - tStart)//1)+"  second"
=======
    	# f = open(dirpath,'r')
    	# for line in f.readlines():
    	#     print line
        #     piece11.append(line)
    	# f.close()
        qrcommit(piece11,piece12,dirpath,name)
        tEnd = time.time()
        print ("Success")
        print (" spend  "+str((tEnd - tStart)//1)+"  second")
>>>>>>> origin/master

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
<<<<<<< HEAD




def qrcommit(data1,data2,filenamepath,name):
    for x in range(len(piece11)):
    	qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4,)
    	qr.add_data(data1[x].decode('big5'))
    	qr.make() # Generate the QRCode itself
    	# im contains a PIL.Image.Image object
    	im = qr.make_image()
    	# To save it

        im.save(filenamepath.replace('.csv','\\')+name[x].strip()+'-1.jpg')
        print data1[x]
    for x in range(len(piece12)):
    	qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4,)
    	qr.add_data(data2[x].decode('big5'))
    	qr.make() # Generate the QRCode itself
    	# im contains a PIL.Image.Image object
    	im = qr.make_image()
    	# To save it
        im.save(filenamepath.replace('.csv','\\')+name[x].strip()+'-2.jpg')
        print data2[x]
    	# im.save(filenamepath[0:filenamepath.rfind('/')+1].decode('UTF-8').strip()+x.decode('UTF-8').strip()+'.png')
=======
def qrcommit(data1,data2,filenamepath,name):
    for x in range(len(piece11)):
        qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4)
        qr.add_data(data1[x].decode('big5'))
        qr.make()
        im = qr.make_image()
        im.save(filenamepath.replace('.csv','\\')+name[x].strip()+'-1.jpg')
        print (data1[x])
    for x in range(len(piece12)):
        qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4)
        qr.add_data(data2[x].decode('big5'))
        qr.make()
        im = qr.make_image()
        im.save(filenamepath.replace('.csv','\\')+name[x].strip()+'-2.jpg')
        print (data2[x])
>>>>>>> origin/master
if __name__ == '__main__':
    app = App()
    app.MainLoop()
