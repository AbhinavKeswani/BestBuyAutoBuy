import time
import smtplib
from email.message import EmailMessage 
import timeit
import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() #setting the driver for use with firefox


username = '' #put username here
password = '' #put password here




#values for beep alert on local device
freq = 237
dur = 1000 #lasts for 1000 milliseconds, change to whatever works for you

#this is the link for the sign in screen, as seen on google search. To obtain this, I searched for best buy login, 
#and copied link address
#THIS LINK MAY NOT WORK FOR EVERYONE. PLEASE FOLLOW MY STEPS AS DESCRIBED ABOVE FOR BEST RESULTS
driver.get("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwievreMyJftAhV4VTABHcxFB5sQFjAAegQIBBAC&url=https%3A%2F%2Fwww.bestbuy.com%2Fidentity%2Fglobal%2Fsignin&usg=AOvVaw1mnFl_G4wNQURCzKVsUPrf")



#finds email input box, and enters the value in the username variable above
emailInputBox = driver.find_element_by_class_name("tb-input ")
emailInputBox.send_keys(username)

#finds password input box, and enters the value in the password variable above
passwordInputBox = driver.find_element_by_id("fld-p1")
passwordInputBox.send_keys(password)

time.sleep(1)

passwordInputBox.send_keys(Keys.ENTER) #submits username and password, effectively logs in user

time.sleep(5)

#this line will bring up the item itself, so this can be changed based on the item one wants. Just copy the link in the address bar, and paste it here
driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")

#this boolean type determines whether the add to cart button exists in the instance or not. We set it at false to keep the loop running
foundButton = False

while not foundButton:
    #this searches for the button by using the html class name, and this can be found using inspect element tab of the browser
    addToCartButton = addButton = driver.find_element_by_class_name("add-to-cart-button")

#this is the search query for the string inside the class attribute. It basically searches for "btn-disabled" inside the class to determine if it exists or not
    if("btn-disabled" in addToCartButton.get_attribute("class")):
        time.sleep(3) #sleeps 3 seconds

        driver.refresh() #reloads page

        addToCartButton = addButton = driver.find_element_by_class_name("add-to-cart-button") #refreshes the addToCartButton variable to ensure no data loss
                    

    else: #case where the add to cart button is found, which stops the while loop
        foundButton = True#this variable controls the loop, so when the button is found, you can quickly change the value and stop the loop


addToCartButton.click()#clicks the add to cart button
driver.get("https://www.bestbuy.com/cart")#navigates to the cart
winsound.Beep(freq, dur)#makes a sound to alert user that item has been added

#ONCE THE SOUND RINGS, BE THERE FOR HUMAN VERIFICATION, OTHERWISE YOU WILL LOSE YOUR PRODUCT