class Cataloge_downloader():

    def sn_input(self):
        try:
            sn = str(input('Type cooler sn number: '))
            return sn
        except:
            print('unexpected error')


a = Cataloge_downloader()
b= a.sn_input()
print(a)
