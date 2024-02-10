# This Python file uses the following encoding: utf-8

# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Config
login_time = 30                 # Time for login (in seconds)
new_msg_time = 30                # TTime for a new message (in seconds)
send_msg_time = 5               # Time for sending a message (in seconds)
country_code = +91               # Set your country code
action_time = 2                 # Set time for button click action
image_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\whatsappAutomationForImage\\img1.png'        # Absolute path to you image

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
msg = "📣 Get ready for a limited time offer that's too good to miss! 😱🔥💰 Introducing the C & C++ Limited Offer for only 1000/-! 💻💲Have you always wanted to master the programming languages of C & C++? Now is your chance! 🚀 Whether you're a beginner or looking to level up your coding skills, this offer is tailor-made for you.With C & C++ being the foundation of many software applications, learning these languages opens up a world of opportunities for you in the tech industry. 🌐💡Imagine being able to develop your own software, create impressive applications, or even contribute to open-source projects. The possibilities are endless! 💪💻But wait, that's not all! 🎉 When you grab this limited offer, you'll also get access to:1️⃣ Comprehensive video tutorials taught by industry experts. 🎥👨‍🏫2️⃣ Exciting coding challenges to put your skills to the test. 💪💡3️⃣ A supportive online community of fellow learners to connect with. 👥💬4️⃣ An official certification upon completion. 🎓✅Don't miss out on this incredible opportunity to boost your programming prowess and future-proof your career. 🚀🌟So what are you waiting for? Click the link below to avail this limited offer: https://bit.ly/stechnosolutions Let's dive into the world of C & C++ together and level up our coding game! 🙌💻"

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('number.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)
        time.sleep(new_msg_time)
        # Click on button to load the input DOM
        if(image_path):
            attach_btn = driver.find_element(By.CLASS_NAME, 'bo8jc6qi')
            attach_btn.click()
            time.sleep(action_time)
            # Find and send image path to input
            msg_input = driver.find_elements(By.CSS_SELECTOR, '._2UNQo input')[1]
            
            msg_input.send_keys(image_path)
            time.sleep(action_time)
        # Start the action chain to write the message
        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            # SHIFT + ENTER to create next line
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()