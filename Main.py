import base64
import paz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = r'C:\Users\Admin\Desktop\Frigo\Catalogues_Downloader\chromedriver.exe'
class Cataloge_downloader():

    def __init__(self,driver_patch):
        self.driver = webdriver.Chrome(driver_patch)
        self.user = base64.b64decode(paz.uz).decode('utf-8')
        self.pas = base64.b64decode(paz.uz).decode('utf-8')

    def sn_input(self):
        try:
            sn = str(input('Type cooler sn number: '))
            return sn
        except:
            print('unexpected error')


    def log_in(self):
        login = self.driver.find_element_by_id('login')
        login.send_keys(self.user)
        password_driver = self.driver.find_element_by_id('password')
        password_driver.send_keys(self.pas)
        self.driver.find_element_by_css_selector("#authForm > div > div > div.mpof_ki.myre_zn.myre_8v_s.m7f5_sf.mp4t_16_s._d596d_1JtF3 > button").click()


    def page_open(self):
        self.driver.get('https://allegro.pl/logowanie?origin_url=%2F')
        self.driver.find_element_by_css_selector("body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(2) > div > div > div > div > div._15pc6._d9spf.mpof_z0.m7er_k4.mp7g_oz.mse2_56.mp4t_0.m3h2_0.mryx_0.munh_0.m911_5r.mefy_5r.mnyp_5r.mdwl_5r.mh36_0.mg9e_16.msts_9u.mjb5_zl.meqh_bv.mj7a_8.mj7a_16_m > div._9f0v0._jkrtd.mj7a_0.mh36_16.mvrt_16.mg9e_16.mpof_ki.m389_6m.munh_56.m3h2_56.myre_zn.myre_8v_s.m7f5_5x_s.mjru_vb._854c2_OPWNL > button.mgn2_14.mp0t_0a.m9qz_yo.mp7g_oh.mse2_40.mqu1_40.mtsp_ib.mli8_k4.mp4t_0.munh_0.m911_5r.mefy_5r.mnyp_5r.mdwl_5r.msbw_2.mldj_2.mtag_2.mm2b_2.mqvr_2.msa3_z4.mqen_m6.meqh_en.m0qj_5r.mh36_16.mvrt_16.mg9e_0.mj7a_0.m9tr_pf.m2ha_2.m8qd_qh.mjt1_n2.bqyr8.mgmw_9u.msts_enp.mrmn_qo.mrhf_u8.m31c_kb.m0ux_fp.b1bc7.m7er_0k.m7er_56_s.mjru_k4._854c2_2sUz3.mryx_24.mryx_0_s.m3h2_0.m3h2_16_s").click()



a = Cataloge_downloader(PATH)
a.page_open()
a.log_in()
