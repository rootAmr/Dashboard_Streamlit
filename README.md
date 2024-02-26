# 🚲 Capital Bikeshare: Bikesharing Analysis and Dashboard

## 📝 Analysis with Jupyter Notebook

🚧 See the detail of this analysis and visualization on the [notebook](https://github.com/fikrionii/Dicoding-Bike-Sharing/blob/main/notebook-bikeshare-analysis.ipynb) 🚧

### Defining Question
1. How is the trend in the number of bike-sharing rides in recent years?
2. What is the usage pattern of bike-sharing rides based on time of day?
3. What season has the highest bike-sharing rides?
4. What is the usage pattern of bike-sharing rides based on day of the week?
5. Are there any correlations between temperatures that indicate conditions when bike-sharing rides are high?
6. Does weather affect bikeshare usage?

### Insights and Findings
1. The number of bikeshare rides in 2012 was higher than in 2011. Both years showed the same trend and seasonality, with the number of rides increasing in the middle of the year and decreasing at the beginning and end of the year.

2. For registered users, the number of rides peaked at 8:00 AM and 5:00 PM, suggesting that they may have used the bikes to commute to work. For casual users, the number of rides started to increase during the day and decreased during the night.

3. Bikeshare rides were highest during the summer season and lowest during the winter season.

4. For registered users, the number of rides was higher during weekdays. This is consistent with the findings in question 2, suggesting that registered users likely used the bikes to commute to work. For casual users, the number of rides was higher on weekends than on weekdays, indicating that they used the bikes for leisure activities on weekends.

5. Yes, there is a moderate correlation between temperature and the number of bikeshare rides. The number of rides is lowest at colder temperatures, which occur during the winter, and starts to increase as the temperature increases, which happens in the summer. However, there is a "sweet spot" or temperature range when the number of rides is highest, which is between 20°C and 30°C. This temperature range typically occurs during the summer and fall seasons. On days with these temperature conditions, we can expect the number of bikeshare rides to be high.

6. Yes, the number of rides is significantly higher during clear weather than during more extreme weather conditions.

## 📊 Dashboard with Streamlit
### Streamlit Cloud

🚧 View the dashboard on streamlit could directly on this link: https://capital-bikeshare-alfikri.streamlit.app/ 🚧

The dashboard shows the count of total rides across the year and season. It also shows the difference casual riders and registered riders use of the bikesharing service, based on hour and day of the week.

<p align="center">
  <img src="/image/streamlit_dashboard.png" />

### Run Streamlit on Local

#### Install Dependencies

To install all the required libraries, open your terminal/command prompt/conda prompt, navigate to this project folder, and run the following command:

```bash
pip install -r requirements.txt
```

#### Run Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```

Thanks for visiting my project! 🔥
