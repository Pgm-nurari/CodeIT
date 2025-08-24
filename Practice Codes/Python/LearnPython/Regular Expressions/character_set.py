import re

text = '''
Report on Introduction to Stock Market
The workshop event, "Introduction to Stock Market," was organized on October 12, 2023, by the Trivandrum-based IEDC at CET. The event aimed to provide valuable insights into the world of stock market investments and was led by the knowledgeable speaker, Shafeeq Muhammed.
Event Details:
Speaker: Shafeeq Muhammed
Venue: CGPU Hall, CET Trivandrum
Time: 10:00 am
Event Summary:
The event was well-attended by individuals eager to learn about stock market investments. Shafeeq Muhammed addressed several crucial topics, highlighting key objectives during the workshop. The event spanned a specific duration, featuring various activities.
Introduction to Stock Market:
1.Investments and Company Shares: Shafeeq Muhammed emphasized the importance of investments in company shares, which serve as a vital component of the stock market.
2.Warren Buffet: The event presumably touched upon the investment strategies and principles followed by renowned investors like Warren Buffett.
3.Investment Strategy: Attendees learned that successful stock market investments require a proper analysis of a company's growth potential. Shafeeq Muhammed advised participants to invest in companies that promise better growth and an optimistic investment future. He also emphasized the concept of diversification, where even if one company faces bankruptcy, the shareholder's overall portfolio remains relatively stable.
Wanna Make 1 Crore:
1.SIP Calculator: The workshop possibly discussed the concept of a SIP (Systematic Investment Plan) calculator as a means to achieve financial goals.
2.Saving Strategy: Shafeeq Muhammed may have suggested that saving a small amount, such as Rs. 40 per day, can lead to accumulating 1 crore in a year.
Mutual Funds:
The event introduced participants to the world of mutual funds, offering insights into this investment vehicle:
1.Selecting Mutual Funds: Attendees were guided to select mutual funds with an annual growth rate of 12% through platforms like Groww or Coin-Zerodha.
2.Increasing Investment: Shafeeq Muhammed may have advised increasing investments by 10% per year to benefit from compounding returns.
Risks and Management:
1.Investment Sources: Shafeeq Muhammed urged participants never to invest with money borrowed from personal or any kind of loans as they are liabilities, not assets. He emphasized the importance of using savings, which represent a form of asset, to purchase more assets.
2.Diversification: The speaker suggested investing in multiple companies simultaneously. This strategy ensures that even if one company faces losses, the profits from others can offset those losses.
3.Sector Diversification: Attendees were encouraged to diversify their investments across various sectors and to invest in the leading company within each sector.
Websites to Explore:
Morningstar
Screener
YouTube: The speaker recommended watching the YouTube channel "Penny Stock Shafiq SMK" with specific reference to a video titled "13:43."
Conclusion
In conclusion, the "Introduction to Stock Market" workshop, led by Shafeeq Muhammed, proved to be an informative and insightful event for all those keen to understand the world of stock market investments. Attendees gained valuable knowledge about investment strategies, risk management, and tools to achieve financial goals. Shafeeq Muhammed's expertise and guidance left a lasting impact on the eager participants, setting them on a path towards more informed and strategic investing.

This workshop not only emphasized the significance of diversification and intelligent investment choices but also provided practical tips and resources, such as the SIP calculator and online platforms for mutual fund investments. The event successfully demystified the complexities of the stock market, making it more accessible to a broader audience seeking to secure their financial future.


Sabhyam Mishra,
CTO, IEDC, Amrita School of Computing, Amrita Vishwa Vidyapeetham - Kochi Campus
12 - 10 - 2023
'''
pattern = r'IEDC'
matches = re.finditer(pattern,text)
for match in matches:
    print(match)
