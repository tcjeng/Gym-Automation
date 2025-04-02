## Gym-Automation

#### Project Motivation
The University Union and Recreation Center are managed by Associated Student.Inc (ASI) at Cal Poly. The ASI app provides live activity levels of these facilities to better help students plan their visit. The setback of this website is that it lacks a historical view to show the trend of activity level of each facility. The goal of this project is to help create such an automated user interface using AWS QuickSight along with other AWS services. 

#### Prototype Design
This prototype requires various AWS services including Lambda, S3, IAM, and QuickSight. Other required resources include a Python web scraper script and compatible packages for the Lambda environment.  
- AWS Lambda: Used to deploy the Python web scraper script
- AWS EventBridge: Provides a trigger to allow the web scraper to run in a 15 min interval
- AWS S3: Used to store scraped data as “occupancy_level.csv”
- AWS IAM: Used to create a user group and assign permission to make sure each AWS service works with each other as well as each member in the project can access the project
- AWS QuickSight:  Used to analyze and visualize data in the  “occupancy_level.csv” with an auto refresh schedule is set at 23:00 daily, making sure the analysis is up to date

#### Comparison with Competitors
In this project, we are comparing business intelligence tools mainly provided by cloud service providers Amazon, Microsoft, and Google. AWS QuickSight was designed for users who have adapted the AWS ecosystem, offering seamless experience with services like S3, Lambda, and EventBridge. Microsoft Power BI follows the logic of  Microsoft Office Suite softwares, such as Excel and Access. Google Looker, on the other hand, is a favorite for data-driven enterprises leveraging Google Cloud, particularly BigQuery.
Since all three tools offer similar core functionalities, we focus on their learning curve, product ecosystem, and pricing to differentiate them. The following sections will explore these differences in detail, with a particular focus on how AWS QuickSight stands out in its native environment.

#### Learning Curve
AWS QuickSight offers a straightforward interface but requires some familiarity with AWS services to unlock its full potential. While it’s not overly complex, users new to AWS may face a slight learning curve. That said, its dashboard creation process is relatively simple, making it a good choice for teams already embedded in the AWS ecosystem.
Microsoft Power BI offers a similar UI to Excel and PowerPoint, such as tool taps, drag-and-drop function. Users do not need to spend too much time on getting used to the new tool.It is accessible to both technical and non-technical users. For organizations looking to get up and running quickly, Power BI is a strong contender.
Google Looker is the most technical intense option among the three. Its learning curve is steep but with high flexibility. Its LookML code is based on YAML. Developers can precisely fine tune data relations, permission, and calculation logic. Looker is ideal for data-savvy teams who need deep customization, but it may not be the best fit for organizations seeking a plug-and-play solution.

#### Product Ecosystem
The integration capability of these three products with its cloud ecosystem is crucial in this comparison. 
One of AWS QuickSight’s core competitive advantages is its deep integration with the entire AWS service family. For example, users can use AWS lambda to clean and merge data and later visualize them in QuickSight. Our prototype was, in fact, designed to demonstrate such integration in a more comprehensive way. This level of integration makes QuickSight a cohesive addition to the AWS ecosystem.
Likewise, Microsoft Power BI takes advantage of the Microsoft product family, making it a natural choice for Microsoft-centric businesses. Companies who have adapted the Microsoft ecosystem will save resources on training staff. Data can be shared seamlessly with Excel, Azure, Dynamics 365, and Teams. In addition, non-Microsoft data sources can also be integrated, so it maintains its flexibility. 
Google Looker is a perfect data visualization tool working with BigQuery. Its API-driven architecture also allows for embedding analytics into other applications. As a result, it is a powerful choice for organizations that prioritize real-time data and custom integrations.

#### Sample Findings
An analysis was conducted after collecting data for a complete week. Daily and hourly average activity level at the Recreation Center was calculated and plotted using QuickSight. The result shows that, on average, the daily activity level for Tracker Room, Upper Exercise Room, and Lower Exercise Room are 73.61%, 71.74% and 46.48% respectively. In terms of hourly pattern, Tracker room has the longest peak hour starting from 10:00 am to 8:00 pm. Upper Exercise Room’s peak hour starting from 10:00 am to 7:00 pm. Upper Exercise Room’s peak hours only occur from 4:00 pm to 5:00 pm, which is the shortest. This result has proven that the prototype is working as intended.

#### Future Enhancements
Expand the Scope: Expanding the scope to other facilities on campus can help manage crowds especially for places like dining halls or parking lots that can get really crowded during school days
Apply predictive analysis: Use machine learning to analyze historical trends and predict future peak usage times to allow better planning and resource allocation
Get it published: Providing students with real-time access to this data can help students plan their time more efficiently 

## Applications
Retail & Shopping Malls: Retailers can monitor foot traffic to optimize store layouts, staffing, and apply marketing strategies 
Office Spaces: Companies can track meeting rooms and public area usage to improve efficiency in onsite work settings
Public Transportation: Cities can track the usage of transportation to adjust transit schedule to fit the demands
Event Management: Large-scale events, such as music festivals, concerts, stadium or sport events can track crowd movements to enhance safety and logistics
Election: Election stations could track the crowd to inform voters, so voters can go vote at a lower-traffic time to avoid long wait time
