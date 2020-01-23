# Stock-Alarmi



## Vision Statement

Having stocks in different markets in different time zone and having limited time in a day to look into different apps, I found the need to have a source of truth where I would like to check in one place to get the best possible information. Oftentimes, I decide to purchase stocks when below or above the threshold in my mindset; however, in the midst of information and numbers the stock market provides, I often forget the numbers I have in my mind. Thus, the goal is to have a place where it collects multi-dataset from companies users have put into the "watch list" and by adding algorithms based on the dataset and their needs, it would send notification when the conditions are met automatically. 



## Design

### Feature List 

#### Alarmi-bot 

* collect the current stock-price from "watch list" companies on scheduled time (decides on Time Interval)
* update and send if the noticeable change happened
* update and send if it has met my price cutline
* update and send if any important upcoming event is happening (advanced feature)
* update and send if any important deals, related news (advanced feature)



#### Data Analysis

* analyze based on time-line
* analyze based on revenue, debt, etc. 
* analyze based on news, deals, earning report, etc. (advanced feature)



### Use Cases 

* User can add companies of their interest into the "Watch list" by typing into the channel
* User can remove companies with no more interest from "Watch list" by typing into the channel
* User can add threshold for each company they put into Watch list
* User can provide their number of shares to keep current total price 



## Architecture

Tha main platform will be Slack. 

* A collector/worker 
  * set up locally to run every time interval during the market hours. 
  * send API to get the price from <https://www.alphavantage.co/>
  * update the database
  * process the logic to see if it meets the condition
  * send to Slack channel 

Extensibility

* If for more advanced features, use the backend infra to build Mobile App

