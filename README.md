# Python Sentiment Analysis using TextBlob  
  
Sentiment Analysis(using TextBlob) on a webpage scraped using Selenium.   
  
Here, sentiment analysis is performed on reviews scraped from Candy Crush's Google Play Store page. Selenium library is used for web scraping. while TextBlob is used for sentiment analysis.  
  
### Dependencies and Prerequisites  
  
Selenium and textblob python libraries;  
chromedriver.exe (any other browser driver will work with slight modification to the code)  
  
### How It Works?  
  
1. A selenium instance is used to open the [Candy Crush Google Play Store page](https://play.google.com/store/apps/details?id=com.king.candycrushsaga&showAllReviews=true).
2. The relevant review elements are extracted from the webpage using selenium, by passing appropriate CSS selectors(found using Chrome DevTools).
3. For simplicity, we only consider the first sentence of each review(a sentence being defined as the characters till the first period '.'). To exclude empty strings, only the sentences with more than 5 character lengths are considered.
4. Using TextBlob, each sentence is scored a polarity rating between -1 and 1(-1 being most negative, 1 being most positive). We assume sentences with a score > 0 to be positive. and with score < 0 to be negative. The sentences are individually printed with their sentiment score.  
5. Finally, the number of positive, negative and zero-rated reviews are printed.  
  
**NOTE : There might be a few dubious sentiment ratings for certain sentences. TextBlob isn't completely accurate!**



