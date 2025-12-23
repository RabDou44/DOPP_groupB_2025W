## DOPP group B project

### Problem questions:
- How do rail travel times compare to air travel times between cities in Europe? 
- Are there routes on which high-speed rail leads to shorter journey times than air travel? 
- Which percentage of routes are faster travelled by train than by flight?
- How can estimates of travel time to and from airports be included? 
- Which is the most well-connected city in Europe in terms of minimising travel times to other cities?
- Which is the worst connected city in Europe in terms of minimising travel times to other cities?

### Datasets:
- https://www.kaggle.com/datasets/polartech/flight-data-with-1-million-or-more-records
- https://www.kaggle.com/datasets/headsortails/train-stations-in-europe
- https://data.4tu.nl/datasets/f045231a-a153-43cb-a5b2-9b37f4528ccf 

### General data :
- [EC report](https://ec.europa.eu/regional_policy/sources/work/2023-rail-vs-air_en.pdf)
- [DB data](https://github.com/piebro/deutsche-bahn-data)
- [EC comparison](https://ec.europa.eu/regional_policy/assets/scripts/map/regio-gis-maps/public_transport/rail_vs_air.html)
- [Eurostat](https://ec.europa.eu/eurostat/databrowser/explore/all/transp?lang=en&subtheme=rail.rail_pa&display=list&sort=category&extractionId=rail_pa_nbpass)

### Datasets we would like to be find:
- Explicit Train-route timetables

### Project Assumptions & Sources
- Average Traveltime to the Airport:
- Average Airport Check-in Time:
- Main Trainstation rule (Need your feedbacks):
    - to make analysis more consistent, only the main trainstations are retained
 
### Country List: EU 27
Its important that each Dataset contains the EU27 countries in order to be comparable. Scope may be reduced later down the line. 
- Austria : AT
- Belgium : BE
- Bulgaria : BG
- Croatia : HR
- Cyprus : CY
- Czech Republic : CZ
- Denmark : DK
- Estonia : EE
- Finland : FI
- France : FR
- Germany : DE
- Greece : GR
- Hungary : HU
- Ireland : IE
- Italy : IT
- Latvia : LV
- Lithuania : LT
- Luxembourg : LU
- Malta : MT
- Netherlands : NL
- Poland : PL
- Portugal : PT
- Romania : RO
- Slovakia : SK
- Slovenia : SI
- Spain : ES
- Sweden : SE

### Workplan:

### Deadlines:

### Project Requirements:

#### 1. Introduction
This is a rather open ended exercise with the aim to get you some practice working through the
steps of the Data Science Process covered in the lectures:
- Ask interesting questions
- Get the data
- Explore the data
- Model the data
- Communicate and visualise the results

#### 2. Task
The task is to take one of the questions listed in Section 3 as a starting point. Then work through
the steps of the Data Science process (including steps back as required) to answer the questions.
Some of the first cycles through the Data Science Process could also lead to a refinement or
modification of the questions. You may use whichever datasets are required to answer the questions
(some potentially useful datasets are listed in Section 4). During the data science process steps,
you may have to do some of the following:
- Understand what is in the data – are the data measurements or estimates? How accurate are
these measurements or estimates? Are there biases in the data (e.g. in the data gathering
process)? If you use estimates to make new estimates, how accurate are the new estimates?
Note that this list of questions is not exhaustive.
- Clean the data
- Check for missing data points – decide what to do about them
- Check for outliers – decide what to do about them
- Check for inconsistencies – decide what to do about them
- Calculate descriptive statistics
- Transform the data (e.g. changing units of measurements)
- Check if the necessary data is there to answer the questions. If not, then you could:
    - Combine columns in some way to generate the necessary data
    - Find the necessary data in another dataset
    - Change the questions asked (in this case you have the freedom to do this, but this may
not be the case if someone else is asking the questions)
- Visualise the data
- Calculate correlations
- Check predictions
