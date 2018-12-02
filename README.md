Chips and Salsa
===================================================
*Overview:*
-----------
CoSolo allows freelancers to view and apply for freelance projects from multiple project websites easily.  

The initial version of the product should 



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
