# ECDS - ECommerce Data Scraper
## PRODUCT MARKET TREND ANALYSIS TOOL

![image](https://github.com/Dhanush-Mohan/ECDS/assets/115526861/d19a4759-1fd3-4778-a09a-76b7a7abc321)


# 1.	Introduction

The Product Market Trend Analysis Tool is a web application designed to assist businesses in analysing market trends for specific products on various e-commerce websites. The tool allows users to input a product name and select an e-commerce site, providing them with detailed product ratings, reviews, and other relevant information from the chosen platform. 
## 1.1.	Project Overview:
The need for the Product Market Trend Analysis Tool arises from the ever-evolving and competitive landscape of today's market. Understanding market trends is vital for businesses for several reasons:
1.	**Product Launch Decisions**: When launching a new product, businesses need to gauge market demand and competition. Analysing trends helps in deciding the right time for the product launch.
2.	**Competitive Advantage**: Knowing what products are currently trending can give a business a competitive edge. By aligning their offerings with current market preferences, businesses can attract more customers.
3.	**Inventory Management**: For retailers, understanding market trends is crucial for managing inventory efficiently. Stocking popular products and reducing less popular ones can optimize resources and minimize waste.
4.	**Pricing Strategies**: Market trends influence pricing decisions. Businesses can adjust their pricing strategy based on the demand for certain products, seasonal trends, and competitive pricing.
5.	**Marketing Campaigns**: Effective marketing campaigns are built on understanding consumer behavior and preferences. Knowing what's trending helps create targeted and relevant marketing materials.
6.	**Customer Satisfaction**: By offering products that are currently popular, businesses can enhance customer satisfaction and loyalty. Customers are more likely to return if they find what they're looking for.
7.	**Risk Mitigation**: Understanding market trends can help businesses identify potential risks early. For example, if a product category is declining in popularity, it might be wise to diversify.

8.	**Data-Driven Decision Making**: In today's data-driven world, making decisions based on solid data and market insights is essential. This tool provides data to inform decisions.
   
# 2.	Prerequisites

The prerequisites for this tool are:
1.	**Python Installed**: Ensure that Python is installed on your system. You can download Python from the official website (https://www.python.org/).
2.	**Python Libraries**: Install the necessary Python libraries using pip:
•	*beautifulsoup4* for parsing HTML content.
•	*requests* for sending HTTP requests 
•	*selenium* for web automation and interaction.
•	*webdriver* for setting up webdrivers 
•	*streamlit* for creating the user interface.

3.	**Web Browser**: You will need a web browser for Selenium to interact with. Most commonly used is Google Chrome. Make sure you have Google Chrome installed on your system.
4.	**WebDriver**: Download the WebDriver for the web browser you are using (e.g., Chrome WebDriver for Google Chrome). Ensure that the WebDriver version matches your browser's version. You can download the Chrome WebDriver from the official site: https://sites.google.com/chromium.org/driver/
5.	**Browser Extensions**: Depending on the websites you are scraping; you might need to install browser extensions or plugins. For example, some websites use CAPTCHA protection, and you might need to install CAPTCHA-solving extensions.
6.	**Streamlit Setup**: Since your project uses Streamlit for the user interface, make sure you have Streamlit installed (as mentioned in step 2). You can create a Streamlit application script to display the scraped data.
7.	**Data Sources**: Ensure you have access to the websites you plan to scrape. Some websites have terms of service that prohibit scraping. Make sure you comply with these terms or seek permission if necessary.
8.	**Internet Connection**: A stable internet connection is required for web scraping, as the tool will need to access external websites.
By ensuring that these prerequisites are in place, you'll be well-prepared to start working on your project for market trend analysis.

# 3.	Installation

To install the required libraries, follow these steps:

1.	Clone or download the project repository from GitHub.
  
2.	Open a terminal and navigate to the project directory.
  
3.	Run the following command to install the required libraries:

        pip install -r requirements.txt
  
# 4.	Usage

## 4.1. Running the application:
To run the application, execute the following command:

streamlit run app.py

Access the tool in your web browser at http://localhost:8501.
## 4.2. Using the Interface:
1.	Enter the Product Name in the designated input field.
2.	Choose the E-commerce Site from the dropdown menu (e.g., Amazon, Flipkart).
3.	Click the Analyse button to retrieve product data.
4.	The tool will display detailed product information, including ratings, reviews, and other relevant data.

# 5.	Code Structure

The project code is structured as follows:
1. ***scraper_flipkart.py***:
This module contains the web scraping logic specific to Flipkart. It extracts product ratings, reviews, and other information from Flipkart's product pages. Here we scrape by html parsing.
2. ***scraper_bigbasket.py***:
This module contains the web scraping logic specific to BigBasket. It extracts product ratings, reviews, and other information from BigBasket's product pages. BigBasket, being a dynamic js based website, doesn’t support simple html parsing. So, we use selenium that enables automation in browsing.
3. ***scraper_jiomart.py***:
This module contains the web scraping logic specific to JioMart. It extracts product ratings, reviews, and other information from JioMart’s product pages. Here, we use selenium again.
4. ***app.py***:
This is the master script that contains the code for the Streamlit application. It involves importing the above defined modules and get the user input in the UI and display the required output in the same UI.

# 6.	Features

Some of the salient features of the product are:
1.	**Product Search and Selection:**
   
•	Product Name Input: Users can input the name of the product they want to analyze. This feature allows users to focus their analysis on a specific item or brand.

•	E-commerce Site Selection: Users can select the e-commerce website (e.g., Amazon, Flipkart, BigBasket, JioMart) from which they want to gather product data. This feature ensures that users can access information from their preferred platform.

2.	**Comprehensive Data Retrieval:**
   
•	Ratings and Reviews: The tool retrieves and displays product ratings, user reviews, and other relevant information from the selected e-commerce site. Users can gain insights into the quality and popularity of the product based on these ratings and reviews.

•	Product Information: In addition to ratings and reviews, the tool provides other product-related information such as price, availability, and product descriptions. This comprehensive data helps users make informed decisions.

3.	 **Multi-Site Support:**
   
•	Support for Multiple E-commerce Sites: The tool supports a variety of popular e-commerce websites, allowing users to analyze market trends across different platforms. This flexibility is essential for businesses that want to compare data from various sources.

•	Expandability: The tool's modular design allows for easy integration of additional e-commerce sites in the future, making it adaptable to changing market dynamics.

4.	**User-Friendly Interface:**
   
•	Streamlit Frontend: The user interface is built using Streamlit, providing an intuitive and user-friendly experience. Users do not need to have programming knowledge to access and utilize the tool effectively.

•	Simple Interaction: Users can initiate the analysis with a few simple clicks, making it accessible to a wide range of users, including those less familiar with technical tools.

5.	**Data Presentation and Visualization:**
    
•	Clear Data Presentation: The tool presents scraped data in an organized and easily understandable format. Ratings and reviews are displayed in a structured manner, making it easy for users to extract insights.

•	Visualizations (Optional): Depending on project requirements, the tool can be extended to include data visualizations, such as charts or graphs, to provide a visual summary of the market trend data.

6.	**Data Export:**
   
   The tool allows users to export the retrieved data to formats like CSV or Excel for further analysis or reporting.

7.	**Real-time Data Retrieval (Potential Enhancement):**

Real-time Data Updates: While the current version of the tool retrieves data on-demand, future enhancements could include scheduled data updates, ensuring that users always have access to the latest market trend information.

# 7.	Limitations

While the Product Market Trend Analysis Tool can be a valuable resource for businesses, it's essential to be aware of its limitations and potential challenges:

1.	**Website Changes:** E-commerce websites frequently update their layouts, class names, or structures. When this happens, your web scraping code may break, requiring updates to maintain functionality.
2.	**Rate Limiting and IP Blocking:** Many websites employ rate-limiting mechanisms and may block IP addresses that send too many requests in a short time. This can affect the tool's ability to scrape data.
3.	**Legal and Ethical Issues:** Web scraping may raise legal and ethical concerns, especially when done without permission. Websites may have terms of service that prohibit scraping, and scraping sensitive or personal data may be illegal.
4.	**Captcha and Authentication:** Some websites use CAPTCHA challenges to deter scraping bots. Handling CAPTCHAs programmatically can be complex. Additionally, some websites require authentication, which adds complexity to the scraping process.

5.	**Data Accuracy:** The tool relies on the accuracy of data available on e-commerce websites. User-generated reviews and ratings can be biased or manipulated.
6.	**Limited Data Depth:** The tool may not access all available product reviews and ratings due to pagination or lazy loading of content. Ensuring comprehensive data retrieval can be challenging.
7.	**Dependency on Third-Party Tools:** The tool depends on external libraries and web browsers (e.g., Selenium, Chrome WebDriver). Updates or compatibility issues with these tools can impact the functionality of the tool.
8.	**Maintenance Overhead:** As websites change over time, maintaining the tool to adapt to these changes can be time-consuming. Frequent updates may be required.
9.	**No Guarantee of Future Data Availability:** The tool's functionality relies on the structure and data availability of e-commerce websites. There's no guarantee that websites will continue to provide the same data in the future.
10.	 **Limited Scope:** The tool provides data primarily on product ratings and reviews. It doesn't consider other market factors like competitor pricing, economic trends, or consumer sentiment outside of reviews.
11.	 **Performance:** Scraping data from multiple websites can be resource-intensive and time-consuming. It may not be suitable for real-time analysis or large-scale data collection.
12.	 **User Input Errors:** Users may input incorrect product names or website names, leading to inaccurate or incomplete data.
13.	 **Privacy Concerns:** Handling and storing user input and scraped data must be done with consideration for user privacy and data protection regulations.
14.	 **User Experience:** The tool's performance and user experience can vary based on internet speed, the volume of data to be scraped, and the responsiveness of the websites being scraped.
To mitigate some of these limitations, it's important to continuously monitor the tool's functionality, stay updated on changes to websites, and consider the ethical and legal implications of web scraping. Additionally, providing clear documentation and disclaimers to users about the tool's capabilities and limitations is essential.

# 8.	Conclusion

In summary, the Product Market Trend Analysis Tool addresses the need for businesses to stay informed about market dynamics. By providing ratings and reviews of specific products on various e-commerce sites, it equips businesses with valuable data to make informed decisions, adapt to changing market conditions, and ultimately thrive in a competitive marketplace.
