## World Trade Data Visualization 


![E8AC4DB6-B836-4EF1-9161-5F7972E3B19A_1_105_c](https://github.com/user-attachments/assets/93bfb320-da49-431c-a512-ecd6b2f9afa7)

During my IB I got a bit of an exposure to the sheer complexity of human interactions, and how they extend to the interactions between countries. While indeed, the initial inspiration for this project was just the prospect of learning how to make data visualizations in Python using libraries like Plotly and Matplotlib, which interestingly became my first use case of cornerstone libraries like Pandas, it quickly became more than that. The project explored the main exports of each country, coloring the countries by that main export, it also connected countries and their main trade partners using black lines adjusted for boldness depending on the volume of trade. The data used was mostly from the 2022 - 23 period and as the power of visualizations does dictate, it is very clear that there are some very unlikely bilateral trade friendships, like the sheer volume of trade between the US and China, I also went to do a different exploration on a more worrying trend, where a lot of the countries, close to 50% of all the countries in the world reported their main trade partner as the USA or China.


<img width="350" alt="Screenshot 2024-12-01 at 4 30 37 PM" src="https://github.com/user-attachments/assets/4086e4b1-de59-4df2-aa9d-1a9438447406">


I was desperate to make a point about how this affects economic development, but I have no statistical reason to claim this (don't worry I am still trying to figure out how to pull a p-hack and Texas sharp-shooter analysis on this for my next Ted talk). 

The visualization is a very simple Python execution. Finding the right data was pretty much the biggest challenge. For my map, I used a GeoJson file. From datahub, the file is available within the project but this is the source:

https://datahub.io/core/geo-countries

the economic data was largely from the World Trade Organization. However, most of the main binary trade partner infoormation was acquired though google searches. I am not sure that I have a better way to conduct this process now, and I think it really did give me insight into the challenges that arise when you want specific data but it has not yet been compiled in a proper scientific way. 
