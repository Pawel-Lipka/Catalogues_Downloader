import time
import os
import shutil

class File():

    # method to get the downloaded file name
    def getDownLoadedFileName(self, waitTime,driver):
        driver.execute_script("window.open()")
        # switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        # navigate to chrome downloads
        driver.get('chrome://downloads')
        # define the endTime
        endTime = time.time() + waitTime
        while True:
            try:
                # get downloaded percentage
                downloadPercentage = driver.execute_script(
                    "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
                # check if downloadPercentage is 100 (otherwise the script will keep waiting)
                if downloadPercentage == 100:
                    # return the file name once the download is completed
                    self.file_name = driver.execute_script(
                        "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
                    return self.file_name
            except:
                pass
            time.sleep(1)
            if time.time() > endTime:
                break



    def file_rename(self,old_file_name,new_file_name,path='C:\\Users\\plipka\\Downloads\\'):
        try:
            os.rename(path+old_file_name,path+new_file_name+old_file_name[-4:])
        except FileExistsError:
            os.remove(path+new_file_name+old_file_name[-4:])
            os.rename(path + old_file_name, path + new_file_name + old_file_name[-4:])
        except TypeError:
            print("can't rename - file don't exist")
            return "can't rename - file don't exist"


    def move_file(self,path_from,path_to):
        shutil.move(path_from,path_to)



