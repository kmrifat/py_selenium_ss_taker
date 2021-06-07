import os.path
from io import StringIO
from timeit import Timer

from PIL import Image
from Screenshot import Screenshot_Clipping
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class TakeSnapShot(BasePage):
    target = '.ut-hero-passed'  # .is-sticky, .ut-hero-passed

    def take_snap(self, network, url):
        WebDriverWait(self.driver, 10)  # sleep a bit
        script = """
        let hello = setInterval(()=>{
        let isSticky = document.querySelector('[class*="%s"]');
            if (isSticky){
                 isSticky.style.visibility = 'hidden'
                 clearInterval(hello)
            }
        },1000)
        """ % self.generate_target(network)

        self.driver.execute_script(script)
        ob = Screenshot_Clipping.Screenshot()
        img_url = ob.full_Screenshot(
            self.driver,
            save_path=self.get_save_dir(network),
            image_name=url.split(".")[0] + ".png"
        )

    def generate_target(self, network):
        switcher = {
            1: 'is-sticky',
            2: 'ut-hero-passed',
            3: 'sticky',
        }
        return switcher.get(network, '.d')

    def get_save_dir(self, network):
        dir = os.path.join(os.getcwd(), network)
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir
