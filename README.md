Chips and Salsa
===================================================
*Overview:*
-----------
CoSolo allows freelancers to view and apply for projects from multiple project websites conveniently.  Using AI-based recommendation engine, CoSolo will present projects that match freelancer's preference and probablity of winning the project, in ranked order.  This would ensure that Freelancer can sift through the noise and only apply to projects that make the most sense for him/her. 

The initial version of the product would have ability for the freelancer to log-in using linkedIn profile, which would allow CoSolo to download linkedIn profile data of the freelancer, so he/she does not have to retype it.  There will be a preference page where the freelancer can add preferences for their projects such as hourly rate, location and number of workdays in a week.  Finally, there will be a dashboard of top 5 projects in ranked order based on recommendation engine.  These projects would have been ingested from various project sites that have open APIs or which we can scrape project info from.  Eventually, we would need to integrate with these systems so we can apply to them directly, but for now, we would just present them, and the freelancer would have to go to each site to apply for it.  We believe that just having one consolidated place where they can see the projects that matter to them the most would be a value-add for the freelancers. 

The ideal recommendaiton engine should recommend based on freelancer's preference as stated on their preferene page as well as based on a machine-learned algorithm which will be based on past-history of freelancer applying for the jobs.  Since we won't have this historical data for a given freelancer in the beginning, we would initially ask freelancer whether they like or do not like n number of projects.  It would be akin to using Tinder's like or dislike UI. Based on this, we can create an AI model to predict whether freelancer will like other available projects. In addition, once freelancer starts applying for and winning the projects, we can capture this data and feed it back into the engine to increase accuracy of preference prediction as well as winnability. 

For the purpose of the Hackathon we focused on building only the recommendation engine, as this was the core AI part of our product. We used Random-Forrest Classifer algorithm because this provided most flexibility in terms



xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Classifer and Forest-model


*Key Technologies:*
-------------------
Flask, nltk, scikit-learn

*Steps to Build and Test:*
--------------------------


Code Structure and basic instructions
-------------------------------------

Data
-------------------
Ideally, we need to have a dataset that shows which projects are preferred by freelancers. Therefore the dataset would have some columns for project such as description, rate, dates, skills required, and columns for freelancers such as summary, rate, available dates, and skills.  In addition, there would be a preference column that shows whether freelancer would prefer to work on the project or not.  This type of data is something we would be able to get once we have freelancers on our site, and we can either ask them directly which projects they prefer, or determine this based on projects they select to apply.  

For the purpose of hackathon, we attempted to first find this dataset from somewhere.  Whoever, we could not find any dataset that showed matches on projects to people. Therefore, we needed to create synthetic test data that we could use to train the model. 

We created our test data based on 2 sources of data. 
* Project data: We used Octoparse tool to scrape all 214 project data in Gocatalant.com, which is a project-bid website that is catetered for higher-income independent workers. We focused on scraping summary descriptions for each project, along with what type of project it was (e.g. corporate strategy, marketing & communications)
* Freelancer data: LinkedIn was ideally the best site to scrape freelancer data, but we could not easily scrape the site due to its anti-scraping defensive mechanisms.  So we found another site called velvetjobs.com that had many sample resume summaries per types of profiles. We focused on scraping 40 profiles - 10 summaries per 4 different types of roles: Strategy, Marketing, Finance, and Operations. Much of the dataset had good summaries for these types of roles, but some of them seemed more to be a job post description than resume summary of a person.  Nevertheless, the description did have keywords that were related to the role, so we believe that this would be fine for the test.  In the future, we can buy real freelancer linkedIn data from a vendor who sells it to get cleaner set of data.  

Based on above data, we now had to determine if a particular project is something each freelancer would prefer to work on.  Since we don't really know what the synthetic freelancer would actually prefer to work on, we created a mechanism to assign a preference. This was done by matching the project type with the freelancer role.  For example, if a project type was corporate strategy, and a freelancer's role type was strategy, we assigned preference to be a "Y". On the other hand, if for the same project type, freelancer's role was marketing, then we assigned preference to be a "N".  

In addition, to be more focused on solving data science problem, in the model, we only inputted project description and freelancer summary, as opposed to matching them on other more tactical fields such as dates, and rates, which do not require machine learning to solve. 

Based on above, we were able to create 4 columns of data (ID, ProjectDescription, ProfileDescription, Preference) for 8560 rows (40 freelancer data to every 214 projects) with 710 "Y" data.  We used 80/20 


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Max_df

When building the vocabulary, it ignores terms that have a document frequency strictly higher than the given threshold. This could be used to exclude terms that are too frequent and are unlikely to help predict the label. For example, by analyzing reviews on the movie Lion King, the term 'Lion' might appear in 90% of the reviews (documents), in which case, we could consider establishing Max_df=0.89

Contributers
------------
Dylan Chatterjee  
Manlo Ngai  
Rahul Bhaskar  
Tony Lew  