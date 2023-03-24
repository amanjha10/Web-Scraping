Report: Analysis of Musical Keyboards on Flipkart

Introduction
Musical keyboards are a popular instrument for music enthusiasts and beginners alike. With a wide variety of brands and models available in the market, it can be overwhelming to choose the best one for your needs. In this report, we analyze the product data of musical keyboards from Flipkart, a popular online shopping platform, to identify the best and worst-rated keyboards and compare their prices.

Data Collection
To collect data, we used the Python requests library and BeautifulSoup module to scrape product information from Flipkart's search results pages. We targeted the search query "musical keyboard 61 keys" and collected data from 10 pages. We extracted the product name, price, rating, and discount information from each product's page and stored it in a CSV file.

Data Analysis
We used the pandas library to read the CSV file into a pandas dataframe and analyzed the data as follows:

Keyboard that are given rating of 5: We filtered the dataframe to show only the rows where the rating is 5 and printed the product names of the keyboards with a 5-star rating.

Best and worst-rated keyboards: We assumed that the most liked keyboard is the one with the highest rating and the least liked keyboard is the one with the lowest rating. We converted the price column to numeric values, sorted the dataframe by rating, and selected the first row (most liked) and last row (least liked) using the iloc[] function. We then created a new dataframe to compare the prices of these two keyboards.

Price comparison of most and least liked keyboards: We created a bar chart to visualize the price comparison of the most and least liked keyboards. The x-axis shows the product names, and the y-axis shows the price in Rupees. We also added a title and labels to the chart to make it easier to read.

Conclusion
Based on our analysis of musical keyboards on Flipkart, we found that the most liked keyboard is the <insert most liked product name>, and the least liked keyboard is the <insert least liked product name>. The most liked keyboard is priced at <insert price> Rupees, while the least liked keyboard is priced at <insert price> Rupees. Overall, our analysis provides valuable insights into the product data of musical keyboards on Flipkart, which can help customers make informed decisions when purchasing a keyboard.
