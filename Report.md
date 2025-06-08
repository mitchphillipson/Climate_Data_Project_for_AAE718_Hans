Github Link: https://github.com/HanchengLyu/Climate_Data_Project_for_AAE718_Hans
# Introduction

This report explores the relationship between extreme temperatures and snowfall in the state of Wisconsin. Understanding how these two factors interact is important for assessing the impacts of climate variability on local weather conditions, public safety, and infrastructure planning. In addition to examining this relationship, the report also investigates how patterns of extreme temperatures and snowfall amounts have changed in recent years.

The analysis is based on daily weather data collected from four representative stations across Wisconsin: **Chippewa Valley Regional Airport**, **La Crosse Regional Airport**, **Madison Dane County Regional Airport**, and **Milwaukee Mitchell International Airport**. The dataset spans the period from January 2015 through June 2025, providing a comprehensive view of recent trends. By leveraging data from multiple locations, this report aims to identify both statewide patterns and regional variations in the interaction between extreme temperatures and snowfall.

# 1 Temperature Trends across Wisconsin Regions

Across all four stations analyzed—Chippewa Valley Regional Airport, La Crosse Regional Airport, Madison Dane County Regional Airport, and Milwaukee Mitchell International Airport—daily temperature departures exhibit strong short-term variability but also reveal several common long-term patterns. The period from January 2015 to June 2025 includes numerous instances of both positive and negative temperature anomalies, with daily departures frequently ranging between -20°C and +20°C, and occasional extremes beyond these bounds.

A shared seasonal cycle is evident in all locations: larger temperature swings tend to occur during the winter months, while summer months typically show smaller deviations from the average temperature. This reflects the strong continental climate of Wisconsin, where winter cold spells and occasional warm anomalies drive larger departures, whereas summer temperatures are more stable.

In terms of long-term trends, all stations show subtle signs of increasing temperature variability in the most recent years (2020–2025), particularly through more frequent occurrences of extreme positive departures. This pattern is consistent with broader observations of increased climate volatility in the upper Midwest.

Some station-specific features are also noticeable. For example, Chippewa Valley and La Crosse display slightly more pronounced negative extremes during winter months compared to Madison and Milwaukee, likely due to their more inland locations and reduced moderating influence from Lake Michigan. Conversely, Milwaukee, being near the lake, shows relatively fewer large negative departures, particularly during winter, reflecting the lake's thermal buffering effect.

Overall, while all four regions share broadly similar temperature patterns, localized geographic factors contribute to subtle differences in the magnitude and frequency of extreme temperature departures.

## Temperature Departure Plots

**Fig. 1–4. Daily Temperature Departure (2015–2025) at Four Wisconsin Stations**

<table>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Chippewa_temperature.png" alt="Chippewa Temperature" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/La%20Crosse_temperature.png" alt="La Crosse Temperature" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 1. Chippewa Valley Regional Airport</td>
    <td align="center">Fig. 2. La Crosse Regional Airport</td>
  </tr>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Madison_temperature.png" alt="Madison Temperature" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Milwaukee_temperature.png" alt="Milwaukee Temperature" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 3. Madison Dane County Regional Airport</td>
    <td align="center">Fig. 4. Milwaukee Mitchell International Airport</td>
  </tr>
</table>

# 2 Snow Depth Trends across Wisconsin Regions

Snow depth patterns across the four Wisconsin stations display both common seasonal dynamics and regional variations. A consistent pattern observed across all stations is the occurrence of the highest snow depths typically between December and March, with most years showing distinct peaks followed by sharp declines. Interannual variability is also apparent: some winters, such as 2019–2020, recorded significantly higher snow depths across multiple stations, while other years experienced relatively mild snow seasons.

In terms of regional differences, Chippewa Valley generally recorded the highest snow depths among the four stations, with extreme peaks exceeding 60 centimeters, particularly notable during the 2019–2020 winter. Madison also exhibited years with substantial snow accumulation, with multiple events surpassing 30 centimeters. In contrast, La Crosse consistently reported lower snow depths, often remaining below 20 centimeters even during peak winter periods. Milwaukee showed moderate snow depths, though with occasional sharp spikes—reflecting both lake effect snow and rapid melting due to its proximity to Lake Michigan.

## Snow Depth Plots

**Fig. 5–8. Daily Snow Depth (2015–2025) at Four Wisconsin Stations**

<table>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Chippewa_snow_depth.png" alt="Chippewa Snow Depth" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/La%20Crosse_snow_depth.png" alt="La Crosse Snow Depth" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 5. Chippewa Valley Regional Airport</td>
    <td align="center">Fig. 6. La Crosse Regional Airport</td>
  </tr>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Madison_snow_depth.png" alt="Madison Snow Depth" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Milwaukee_snow_depth.png" alt="Milwaukee Snow Depth" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 7. Madison Dane County Regional Airport</td>
    <td align="center">Fig. 8. Milwaukee Mitchell International Airport</td>
  </tr>
</table>

# 3. Relationship between Snow Depth and Extreme Temperatures

## 3.1 Increasing Frequency of Extreme Snow Depth and Temperature Events

The scatter plots of snow depth versus temperature departure for the four stations—Chippewa Valley, La Crosse, Madison, and Milwaukee—clearly illustrate that extreme weather events have become more frequent in recent years.

For snow depth, the color-coded points show that during the 2020–2022 (orange) and 2023–2025 (red) periods, there were noticeably more days with high snow accumulation compared to earlier years. This pattern is particularly visible in Chippewa Valley and Madison, where several events with snow depths exceeding 30 centimeters occurred in these recent winters. In Milwaukee and La Crosse, while overall snow depths are lower, there is still an observable increase in the number of days with elevated snow depth in the more recent years.

Similarly, extreme temperature departures have become more common over time. The scatter plots indicate that both strongly negative and strongly positive temperature departures are increasingly represented by red and orange points, highlighting a rise in temperature extremes in recent winters. These trends are visible across all four stations.

In summary, the scatter plots suggest a clear temporal trend: both extreme snow depth events and extreme temperature departures have become more frequent in Wisconsin over the past five years.

## Snow Depth vs. Temperature Departure Scatter Plots

**Fig. 9–12. Snow Depth vs. Temperature Departure (2015–2025) at Four Wisconsin Stations**

<table>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Chippewa_snow_temp_colored_scatter.png" alt="Chippewa Snow Temp Scatter" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/La%20Crosse_snow_temp_colored_scatter.png" alt="La Crosse Snow Temp Scatter" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 9. Chippewa Valley Regional Airport</td>
    <td align="center">Fig. 10. La Crosse Regional Airport</td>
  </tr>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Madison_snow_temp_colored_scatter.png" alt="Madison Snow Temp Scatter" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Milwaukee_snow_temp_colored_scatter.png" alt="Milwaukee Snow Temp Scatter" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 11. Madison Dane County Regional Airport</td>
    <td align="center">Fig. 12. Milwaukee Mitchell International Airport</td>
  </tr>
</table>

## 3.2 Relationship between Snow Depth and Temperature Departure

The scatter plots with trendlines provide additional insight into the relationship between snow depth and temperature departure across the four stations. In all cases, there is a consistent negative slope in the fitted trendline, indicating that higher snow depths are generally associated with lower temperature departures—that is, colder than average temperatures.

This negative relationship is evident across all regions, though the strength of the trend varies. La Crosse and Milwaukee exhibit relatively stronger negative slopes, suggesting a clearer association between deep snow cover and colder temperature departures in these locations. Chippewa Valley and Madison also show a negative trend, albeit with a slightly more moderate gradient.

Overall, the trendlines suggest that periods of substantial snow accumulation tend to coincide with below-average temperatures across Wisconsin. This observation is consistent with the expectation that significant snowpack is more likely to persist during extended cold spells. Importantly, the consistency of this pattern across all four stations strengthens the robustness of this finding.

## Snow Depth vs. Temperature Departure with Trendlines

**Fig. 13–16. Snow Depth vs. Temperature Departure with Fitted Trendlines**

<table>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Chippewa_snow_temp_scatter.png" alt="Chippewa Snow Temp Trendline" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/La%20Crosse_snow_temp_scatter.png" alt="La Crosse Snow Temp Trendline" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 13. Chippewa Valley Regional Airport</td>
    <td align="center">Fig. 14. La Crosse Regional Airport</td>
  </tr>
  <tr>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Madison_snow_temp_scatter.png" alt="Madison Snow Temp Trendline" width="400"/></td>
    <td><img src="file:///D:/tasks/2025%20Spring/AAE%20718/Project03/Milwaukee_snow_temp_scatter.png" alt="Milwaukee Snow Temp Trendline" width="400"/></td>
  </tr>
  <tr>
    <td align="center">Fig. 15. Madison Dane County Regional Airport</td>
    <td align="center">Fig. 16. Milwaukee Mitchell International Airport</td>
  </tr>
</table>
