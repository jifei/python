import wx

class Frame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title="Hello,World!"):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
class App(wx.App):

    def OnInit(self):
        print "OnInit"
        image = wx.Image('a.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    def OnExit(self):
        print "OnExit"
def main():
    app = App(True,'output')
    app.MainLoop()

if __name__=='__main__':
    main()