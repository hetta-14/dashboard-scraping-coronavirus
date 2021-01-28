# Coronavirus Scraping Dashboard

In this tutoriel, we will be reviewing an application for automating  web scraping of newest health advice from the World Health Organization from the Worldometers website
and view all data concerning COVID-19 by depoying a dashboard.
**We have 4 main files:**
  1. get_data.py : scraping data with Selenium.
  2. dashboard.py : visualising figures of the dashboard.
  3. index.html : HtML code of the dashboard
  
## Set up
You can clone this public repository by entering the following command into terminal :
```python
git clone https://github.com/hetta-14/dashboard-scraping-coronavirus/
```
### Requirements 
Once you've download the code you should install needed libs by typing the command :
```python
sudo pip install -r requirements.txt
```
All the libraries with their specified versions can be found in this file.
### Web scraping
We will recover the data scraped from the site https://www.worldometers.info/coronavirus/ by entering the following command :
```python
python get_data.py
```
Selenium launches and controls the web browser. The webdriver "chromedriver.exe" manages the browser by Selenium.
Note : 
  - Read the website terms and conditions at robots.txt for understand how you can legally use the data. Most of sites prohibit you from using the data for commercial purposes.
  - Be sure not to download the data too quickly, as this may damage the website. You could also be blocked from the site.
### Launching the dashboard visualization
Using Plotly, we are going to plot and visualize the figures from the scraped data with the command :
```python
python dashboard.py
```
We will visualize the following figures on the dashboard :
![](https://github.com//hetta-14/dashboard-scraping-coronavirus/blob/master/img/A.PNG)
![](https://github.com//hetta-14/dashboard-scraping-coronavirus/blob/master/img/B.PNG)


