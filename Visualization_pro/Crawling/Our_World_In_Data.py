from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


### XXXXX ####



url = "https://ourworldindata.org/natural-disasters"

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)


sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

# table = driver.find_element_class_name("tab clickable")
# print(table)


table_button = soup.find_all("li", class_ = "tab clickable")
'''
print(next(table_button[1].children))
next(table_button[1].children).click()
'''
print((table_button))


table_button = soup.find("div", class_ = "tableTab")
print(table_button)

contries = soup.find("td", class_ = "entity sorted")
print(contries)



'''
sources의 내용

<section>
    <div class="section-heading">
        <div class="wrapper">
            <div>
                <h2 id="number-of-deaths-from-natural-disasters">Number of deaths from natural disasters<a class="deep-link" href="#number-of-deaths-from-natural-disasters"></a></h2>
            </div>
            <div class="in-this-section">
                <div class="label">In this section</div>
                <div class="border"></div>
            </div>
            <ul class="subheadings">
                <li><a href="#annual-deaths-from-natural-disasters"><svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" class="svg-inline--fa fa-arrow-down " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><span>Annual deaths from natural disasters</span></a></li>
                <li><a href="#average-number-of-deaths-by-decade"><svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" class="svg-inline--fa fa-arrow-down " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><span>Average number of deaths by decade</span></a></li>
                <li><a href="#number-of-deaths-by-type-of-natural-disaster"><svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" class="svg-inline--fa fa-arrow-down " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><span>Number of deaths by type of natural disaster</span></a></li>
            </ul>
        </div>
    </div>
    <h3 id="annual-deaths-from-natural-disasters">Annual deaths from natural disasters<a class="deep-link" href="#annual-deaths-from-natural-disasters"></a></h3>
    <div class="wp-block-columns is-style-sticky-right">
        <div class="wp-block-column">
            <p>In the visualization shown here we see the long-term global trend in natural disaster deaths. This shows the estimated annual number of deaths from disasters from 1900 onwards from the <a href="https://www.emdat.be/">EMDAT International Disaster Database</a>.<a id="ref-1" class="ref" href="#note-1"><sup>1</sup></a></p>
            <p>What we see is that in the early-to-mid 20th century, the annual death toll from disasters was high, often reaching over one million per year. In recent decades we have seen a substantial decline in deaths. In most years fewer than 20,000 die (and in the most recent decade, this has often been less than 10,000). Even in peak years with high-impact events, the death toll has not exceeded 500,000 since the mid-1960s. </p>
            <p>This decline is even more impressive when we consider the rate of <a href="https://ourworldindata.org/world-population-growth">population growth</a> over this period. When we correct for population – showing this data in terms of death rates (measured per 100,000 people) – we see an even greater decline over the past century. This chart can be viewed <strong><a href="https://ourworldindata.org/explorers/natural-disasters?facet=none&amp;Disaster+Type=All+disasters&amp;Impact=Deaths&amp;Timespan=Annual&amp;Per+capita=true&amp;country=~OWID_WRL">here</a></strong>.</p>
            <p>The annual number of deaths from natural disasters is also available by country since 1990. This can be explored in the interactive map.</p>
        </div>
        <div class="wp-block-column">
            <div class="wp-sticky-container">
                <figure data-explorer-src="https://ourworldindata.org/explorers/natural-disasters?facet=none&amp;Disaster+Type=All+disasters&amp;Impact=Deaths&amp;Timespan=Annual&amp;Per+capita=false&amp;country=~OWID_WRL&amp;hideControls=true" style="width: 100%; height: 600px; border: 0px none;">
                    <div class="loading-indicator">
                        <span style="border-color:#333"></span>
                    </div>
                </figure>
                <figure data-explorer-src="https://ourworldindata.org/explorers/natural-disasters?tab=map&amp;facet=none&amp;Disaster+Type=All+disasters&amp;Impact=Deaths&amp;Timespan=Annual&amp;Per+capita=false&amp;country=~OWID_WRL&amp;hideControls=true" style="width: 100%; height: 600px; border: 0px none;">
                    <div class="loading-indicator">
                        <span style="border-color:#333"></span>
                    </div>
                </figure>
            </div>
        </div>
    </div>
'''