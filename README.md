
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#set-up">Set up</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#web-scraping">Web scraping</a></li>
        <li><a href="#launching-the-dashboard-visualization">Launching the dashboard visualization</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

# Coronavirus Scraping Dashboard
## About the projet
In this tutoriel, we will be reviewing an application for automating  web scraping of newest health advice from the World Health Organization from the Worldometers website
and view all data concerning COVID-19 by depoying a dashboard.

**We have 3 main files:**
  1. get_data.py : scraping data with Selenium.
  2. dashboard.py : visualising figures of the dashboard.
  3. index.html : HTML code of the dashboard
### Built With

This project was built using :
* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Plotly](https://plotly.com)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  
## Set up
You can clone this public repository by entering the following command into terminal :
```sh
git clone https://github.com/hetta-14/dashboard-scraping-coronavirus/
```
### Prerequisites 
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

![](https://github.com/hetta-14/dashboard-scraping-coronavirus/blob/master/img/A.PNG)
![](https://github.com/hetta-14/dashboard-scraping-coronavirus/blob/master/img/B.PNG)
![](https://github.com/hetta-14/dashboard-scraping-coronavirus/blob/master/img/C.PNG)
![](https://github.com/hetta-14/dashboard-scraping-coronavirus/blob/master/img/D.PNG)
![](https://github.com/hetta-14/dashboard-scraping-coronavirus/blob/master/img/E.PNG)
![](https://github.com/hetta-14/dashboard-scraping-coronavirus/blob/master/img/F.PNG)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b your-new-branch-name`)
3. Commit your Changes (`git commit -m 'Add some changes'`)
4. Push to the Branch (`git push origin  <add-your-branch-name>`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

ETTABAA Hajar - [@hajar-ettabaa](https://www.linkedin.com/in/hajar-ettabaa/) - hajar.etta.7@gmail.com



