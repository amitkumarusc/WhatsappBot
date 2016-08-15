from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

def web_driver_load():
	global driver
	driver = webdriver.Chrome(os.path.join(os.getcwd(),'chromedriver'))

def web_driver_quit():
	driver.quit()

def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	wait(10)


def sendMessage(msg, recepient_list):
	for recep in recepient_list:
		print "Sending to : ",recep
		try:
			one_chat = driver.find_element_by_xpath("//span[@title='%s']"%(recep))
		except:
			print "Unable to find username [%s]"%recep
			continue
		if one_chat != None:
			try:
				one_chat.click()
				wait(1)
				print "Chatbox opened for ", recep
				text_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
				for letter in list(msg):
					text_box.send_keys(letter)
					wait(0.1)
				text_box.send_keys(Keys.RETURN)
			except:
				print "Unable to send msg [%s] to [%s]"%(msg, recep)
				continue
			print "Message [%s] sent to [%s]"%(msg, recep)

if __name__ == '__main__':
	number_of_times = 1
	messages = ["""The modern Olympic Games or Olympics (French: Jeux olympiques[2]) are leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 nations participating.[3] The Olympic Games are held every four years, with the Summer and Winter Games alternating by occurring every four years but two years apart.""",\
          """Their creation was inspired by the ancient Olympic Games, which were held in Olympia, Greece, from the 8th century BC to the 4th century AD. Baron Pierre de Coubertin founded the International Olympic Committee (IOC) in 1894. The IOC is the governing body of the Olympic Movement, with the Olympic Charter defining its structure and authority."""]
	recepients = ["Testing"]

	web_driver_load()
	whatsapp_login()

	for i in range(number_of_times):
		for msg in messages:
			print "[%d]"%(i+1)
			sendMessage(msg, recepients)
	web_driver_quit()