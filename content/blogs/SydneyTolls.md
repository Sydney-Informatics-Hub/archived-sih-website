+++
date = "2019-04-23T00:00:00+10:00"
title = "Exploring Sydney Toll Road Data"
draft = false
type = "sidebar"
blog = true
stream = "news"

thumbnail = "/images/blog/SydneyTolls_use.png"
summary = "For a project with a Transport Informatics group we were exploring some of the data availble on Sydney toll roads. Here are some insights into the data and a few starting points for exploring and visualising a dataset."

authorname = "Nathaniel Butterworth"
authoravatar = "/people/NathanielButterworth.jpg"
authorbio = "Works in in the Research Computing team, plays with HPC, visualisation, general hacking."
+++

I was asked to give a talk by [Emily Moylan](https://sydney.edu.au/engineering/people/emily.moylan.php) about data visualisation for a transport informatics unit so I thought I would use a dataset that was relevent to them. As it turns out all the toll data in Sydney is availble for free download! How nice of them*. You can get it yourself here: https://nswtollroaddata.com/

Firstly, let's jump on the some numbers.

There were **2,120,731,776** toll gantry beeps between 2009 to 2019. These toll roads are the ED, CCT, M7, M2, LCT, M4. I missed the M5 because that data comes in a slightly different format - I will leave it as an exercise for the reader. The data is basically a time series in 15 minute increments for each gantry point with the number of cars/trucks passing through that gantry in the time interval. That means we have **36,447,919** time series points for all roads for all time. 

Don't know [what a gantry is?](https://en.wikipedia.org/wiki/Gantry_(road_sign)) In this context, it is the thing that goes ***beep*** and makes you question why you live in Sydney again.

## The Cross City Tunnel - 1 month
Looking at all that data in one go might be tricky. Let's just start with the Cross City Tunnel for the month of November only back in 2017. Here is what the ***1,257,705*** cars and trucks moving in the CCT looks like over that month look like: 

<figure>
<p align="center">
  <img src="/images/blog/SydneyTolls_CCT_201711_volume.png" style="height:480px">
  <figcaption><em>Volume of vehicles in the Cross City Tunnel for November 2017.</em></figcaption>
  <br>
</p>
</figure>

Straight away you can see lots of non-suprising patterns emerge.

The ups and downs are literally night and day. Plus you can see each peak has a mini up-down which is the morning and evening rush hour. Finally, there is an undulating wave passing over the month, that 7-day period is known as a week! Pretty interesting, but as I said, not suprising. This is pretty typical of all the data. 

## The Cross City Tunnel - 2009-2019
Now let's look at all **135,230,287** trips on the CCT over our 10 year timespan of data (FYI, that is ***26 vehicles per minute***, and at around $5 a pop is worth about **$676 Million dollars** in this time frame, just from the CCT).

<figure>
<p align="center">
  <img src="/images/blog/SydneyTolls_CCT_2010-2019_breakdown_flat.png" style="height:480px">
  <figcaption><em>All tolls collected in the Cross City Tunnel toll road, coloured by gantry and vehicle type.</em></figcaption>
  <br>
</p>
</figure>

On this scale we lose the day-to-day patterns and even the weekly patterns, but we can see there are dips in the volume of vehicles around Chistmas time every year. Best time of year to drive around Sydney toll roads! The different colors representing the different entry/exit points on the CCT and the distinction between cars and trucks doesn't tell us much, except that there are a lot more cars than trucks. Other than that, they all follow the same pattern - people and goods are all moving in different directions but they are moving at similar times.

Anyway, I plotted this as a 3D stacked bar plot (which took about 1 hour and 40GB RAM just to make the figure - I had to run it on out Artemis HPC to stop my computer from crashing) to make visualising the different gantry entry/exit points and car/truck use a bit clearer:

<figure>
<p align="center">
  <img src="/images/blog/SydneyTolls_CCT_2010-2019_breakdown.png" style="height:480px">
  <figcaption><em>All tolls collected in the Cross City Tunnel toll road, broken down by gantry and vehicle type, in 3D.</em></figcaption>
  <br>
</p>
</figure>

To look at this a different way, and probably more informative but less pretty, you can just plot a histogram of the total number of cars/trucks:


<figure>
<p align="center">
  <img src="/images/blog/SydneyTolls_CCT_2010-2019_alltraffic.png" style="height:480px">
  <figcaption><em>All tolls collected in the Cross City Tunnel toll road, broken down by gantry (N/E/W) and vehicle type (Car/Truck), with total numbers for the 2009-2019 collection time.</em></figcaption>
  <br>
</p>
</figure>

## All the roads 2009-2019
There are lots of different ways to explore this data set and many more insights to learn from it.
Rather than doing the same thing for each of the Toll Roads I wanted to try and capture some kind of informative metric across Sydney, so I thought I would plot them all as an animated map and see which tolls are used the most:

<figure>
<p align="center">
  <img src="/images/blog/SydneyTolls_tolluse.gif" style="height:480px">
  <figcaption><em>Most of Sydney toll gantry points coloured according to total volume of use for each year. Sad times when the M4 turns back on in 2018 after not being a toll road for a long time. Note the scale is the total volume of vehicles for that year coloured between 1,000,000 and 10,000,000 vehicles.  </em></figcaption>
  <br>
</p>
</figure>


*From the [toll data website](https://nswtollroaddata.com/) this dataset was released according "with Transurban’s obligations under an Undertaking accepted by the ACCC on 29 August 2018 under section 87B of the Competition and Consumer Act 2010" to basically make it so future toll roads can be competitive when bidding for tenure. And it gives a fun dataset to explore and interogate to learn more about people in the city and data in general. You can access the Python Notebooks I used for exploration from [here](https://github.com/natbutter/SydneyTolls).

If you have done some cool data analysis or have done something with the M5 data [let us know](mailto:sih.training@sydney.edu.au).
