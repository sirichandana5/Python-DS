class mom():
    def mdisplay(self):
        print("mom class")
class dad():
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()
