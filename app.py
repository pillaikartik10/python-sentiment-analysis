from selenium import webdriver                  #importing webdriver
from selenium.webdriver.common.by import By     #to select page elements
from textblob import TextBlob                   #for sentiment analysis

#following steps to prevent "usb_device_handle_win.cc:1020 Failed to read descriptor from node connection" error from appearing in terminal

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#give the path variable to chromedriver.exe here.
driver = webdriver.Chrome('D:/webdriver/chromedriver.exe',options=options)

driver.implicitly_wait(5)

#getting the review page for Candy Crush from Google Play Store
driver.get("https://play.google.com/store/apps/details?id=com.king.candycrushsaga&showAllReviews=true")

#getting the review section from the page. Can be verified using developer tools in Chrome(and an equivalent service in other browsers...)
optionsList = driver.find_elements(By.CSS_SELECTOR,'.UD7Dzf span')


#storing positive, negative and 0 feedbacks.
#for our purpose, positive feedback is defined as a score > 0, and negative feedback as a score < 0
positive_feedbacks = []
negative_feedbacks = []
zero_feedbacks=[]

print("Printing first line of the review with the sentiment analysis score... \n")

#For less complications, we are only considering the first sentence of each review.
#And to check for valid data, only those data with a char length > 5 will be accepted(to prevent garbage values and empty strings)

for x in optionsList:
    review = x.text.split('.')
    sentence = review[0]
    if len(sentence) > 5:
        print(sentence, end = ", ")
        review_polarity = TextBlob(sentence).sentiment.polarity
        print("score :",review_polarity)
        if review_polarity > 0:
            positive_feedbacks.append(sentence)
        elif review_polarity <0:    
            negative_feedbacks.append(sentence)
        else:
            zero_feedbacks.append(sentence)
        

print("\nOverall statistics : \n")
print('Positive_feebacks Count : {}'.format(len(positive_feedbacks)))
print('Negative_feedback Count : {}'.format(len(negative_feedbacks)))
print('Feedbacks with 0.0 sentiment analysis rating : {}'.format(len(zero_feedbacks)))

