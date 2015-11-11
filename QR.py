# -*- coding: utf-8 -*-
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
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
#####################################################################
from qrcode import *
import os
import wx
import wx.lib.filebrowsebutton as filebrowse
import time
from dbfpy import dbf
from dbfpy import dbf 
import os
import csv

piece11 = []
piece12 = []
name = []
####
a = 0
# -----------------------------------------------------------------------------------------------------------------
class Example(wx.Frame):
  	def __init__(self, parent, id, title):
		super(Example,self).__init__(parent, id, title)
		self.InitUI()

  	def InitUI(self):

	    menubar = wx.MenuBar()    #生成選單

	    filemenu2 = wx.Menu()
	    filemenu3 = wx.Menu()


	    qmi = wx.MenuItem(filemenu3, 4, u"查無出口")   #
	    qmi.SetBitmap(wx.Bitmap('icon\\i1.ico' ))

	    q1 = wx.MenuItem(filemenu2, 5, u'CSV')   #
	    q1.SetBitmap(wx.Bitmap('icon\\i4.ico' ))
	    q2 = wx.MenuItem(filemenu2, 6, u'DBF')   #
	    q2.SetBitmap(wx.Bitmap('icon\\i5.ico' ))

	    filemenu3.AppendItem(qmi)
	    filemenu2.AppendItem(q1)
	    filemenu2.AppendItem(q2)

	    menubar.Append(filemenu2, "&QRcode")
	    menubar.Append(filemenu3, "&Quit")
	    self.SetMenuBar(menubar)


	    self.Bind(wx.EVT_MENU, self.PATH, id=4)
	    self.Bind(wx.EVT_MENU, self.PATH, id=5)
	    self.Bind(wx.EVT_MENU, self.PATH, id=6)


	    self.SetSize((800, 300))
	    self.SetTitle(u"QRcode 產生帥帥的條碼")
	    self.Centre()
	    self.SetBackgroundColour('white')


	    self.Show(True)    #顯示框架

###########################################################################
	def PATH(self, e):
	    eid = e.GetId()
	    global a


	    if eid == 4 :
	      self.Close()

	    if eid == 5 :

	      if a == 5:
	        self.dbb.Destroy()
	        self.b.Destroy()

	        a = 0
	      if a == 6:
	        self.dbbo.Destroy()
	        self.bo.Destroy()

	        a = 0
	      self.dbb = filebrowse.FileBrowseButton(self, -1, size=(450, -1), buttonText=u'瀏覽', labelText=u'CSV根目錄:', changeCallback = self.dbbCallback)
	      self.b = wx.Button(self, 40, u'RUN', (500,28), style=wx.NO_BORDER)
	      self.b.SetToolTipString("Run QRcode\n")
	      self.Bind(wx.EVT_BUTTON, self.OnClick, self.b)
	      sizer = wx.BoxSizer(wx.VERTICAL)
	      sizer.Add(self.dbb, 0, wx.ALL, 5)
	      box = wx.BoxSizer()
	      box.Add(sizer, 0, wx.ALL, 20)
	      self.b.SetInitialSize()
	      self.SetSizer(box)
	      a = 5
	    if eid == 6 :

	      if a == 5:
	        self.dbb.Destroy()
	        self.b.Destroy()

	        a = 0
	      if a == 6:
	        self.dbbo.Destroy()
	        self.bo.Destroy()

	        a = 0
	      self.dbbo = filebrowse.FileBrowseButton(self, -1, size=(450, -1), buttonText=u'瀏覽', labelText=u'DBF根目錄:', changeCallback = self.dbbCallbacko)
	      self.bo = wx.Button(self, 40, u'RUN', (500,28), style=wx.NO_BORDER)
	      self.bo.SetToolTipString("Run QRcode\n")
	      self.Bind(wx.EVT_BUTTON, self.OnClicko, self.bo)
	      sizer = wx.BoxSizer(wx.VERTICAL)
	      sizer.Add(self.dbbo, 0, wx.ALL, 5)
	      box = wx.BoxSizer()
	      box.Add(sizer, 0, wx.ALL, 20)
	      self.bo.SetInitialSize()
	      self.SetSizer(box)
	      a = 6

##########################################################################
#################################CSV##########################################
	def dbbCallback(self, event):
	    Dir = self.dbb.GetValue()
	    self.path = Dir
	    event.Skip()
	def OnClick(self, event):
		self.listpath(self.path)
	def listpath(e,dirpath):
		piece11[:] = []
		piece12[:] = []
		name[:] = []
		a = 0
		tStart = time.time()
		if ".csv" not in dirpath and ".CSV" not in dirpath:
			wx.MessageBox(u"不存在DBF檔 請重新選取",u"提示訊息")
		else :
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
		csqrcommit(piece11,piece12,dirpath,name)
		tEnd = time.time()
		print "Success"
		print " spend  "+str((tEnd - tStart)//1)+"  second"
###########################################################################
#################################DBF##########################################
	def dbbCallbacko(self, event):
	    Dir = self.dbbo.GetValue()
	    self.path = Dir
	    event.Skip()
	def OnClicko(self, event):
		self.listpatho(self.path)
	def listpatho(e,dirpath):
		piece11[:] = []
		piece12[:] = []
		name[:] = []
		tStart = time.time()
		na = u'發票號碼'
		if ".dbf" not in dirpath and ".DBF" not in dirpath:
			wx.MessageBox(u"不存在DBF檔 請重新選取",u"提示訊息")
		else :
			db = dbf.Dbf(dirpath) 
			for record in db:
				piece11.append( record['QRCODE1'] )   
				piece12.append( record['QRCODE2'] )  
				name.append( record[na.encode('big5')] )  
				record.store()
		ise = os.path.exists(dirpath.replace('.dbf','').replace('.DBF',''))
		if not ise:
			os.mkdir(dirpath.replace('.dbf','').replace('.DBF',''))
		dbqrcommit(piece11,piece12,dirpath,name)
		tEnd = time.time()
		print ("Success")
		print (" spend  "+str((tEnd - tStart)//1)+"  second")
###########################################################################
def dbqrcommit(data1,data2,filenamepath,name):
    for x in range(len(piece11)):
        qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4)
        qr.add_data(data1[x].decode('big5'))
        qr.make()
        im = qr.make_image()
        im.save(filenamepath.replace('.dbf','\\').replace('.DBF','\\')+name[x].strip()+'-1.jpg')
        print (data1[x])
    for x in range(len(piece12)):
        qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4)
        qr.add_data(data2[x].decode('big5'))
        qr.make()
        im = qr.make_image()
        im.save(filenamepath.replace('.dbf','\\').replace('.DBF','\\')+name[x].strip()+'-2.jpg')
        print (data2[x])
def csqrcommit(data1,data2,filenamepath,name):
    for x in range(len(piece11)):
    	qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4,)
    	qr.add_data(data1[x].decode('big5'))
    	qr.make()
    	im = qr.make_image()
        im.save(filenamepath.replace('.csv','\\').replace('.CSV','\\')+name[x].strip()+'-1.jpg')
        print data1[x]
    for x in range(len(piece12)):
    	qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=10,border=4,)
    	qr.add_data(data2[x].decode('big5'))
    	qr.make()
    	im = qr.make_image()
        im.save(filenamepath.replace('.csv','\\').replace('.CSV','\\')+name[x].strip()+'-2.jpg')
        print data2[x]
# ------------------------------------------------------------------------------------------------------------------------
def main():
  ex = wx.App()     
  Example(None, id=-1, title="main")  
  ex.MainLoop()

if __name__ == "__main__":
  main()
