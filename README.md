<img src="https://images.pexels.com/photos/3407778/pexels-photo-3407778.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260">



## Gourmet's Diary

### User Experience and Features

This website as the name suggests is a guide to help people to understand more about different kind of cuisines, food or drinks. Italian love their coffees, but do we know how all kind of coffes are made? Cocktails are getting very popular and when visiting other countries on holidays sometimes we are limited with our usual drinks when ordering because of the lack of knowledge of huge variety of drinks.

The website contains of 4 pages. The first one "Cuisine" when you click on the buton with external link tells you some facts about some famous cuisines.

Second page "Recipes" is the page with some recipes accesed from mongo db database, however I run of time and wanted to have a lot more interactivity on this page with more recipes.

Third page "Cocktails"  provides some interesting info about world-known cockatils, how to make them or the most populat bars in the world where you can buy cocktails that you never find anywhere else. This is also provided from external links added to the page. When You click below first image, the Trip's guide, the reader can find out the story and history behind those drinks. Below second image is button with "Get inspiration here" and that will take you to the recipes of the coktails. The last part of the cocktails page is about very popular bars in the world where they serve their signature cocktails you wouldnt have anywhere else.

The forth page is about speciality coffees, how many different coffees exist, which of some we never heard of. 

User experience is to find interesting facts about all different kinf of food or drinks for example if they would like to go for a holiday or just to try a new restaurant and to access some delicious recipes.

### Design, Images, Color scheme

The coffee bean background is well matched with images of food and drinks, the main colors are brown, blue and mustardy color for fonts. I think is really good combination and gives very nice look overall.

### Technology

Bootstrap 4.4.1: Bootstrap specially the Grid system was used to structure the Recipe page.

Free Bootsrap Theme: were used for the static pages, I unzip them to my workspace in Gitpod and then I created Templates, pages where I was using Python and customized them.
Reference: https://startbootstrap.com/themes/

Git and Github  used for version control.


Python was used and the aplication was deployed to Heroku

### Testing and Deployment

1. Created run.py file.

2.Imported flask (from flask import Flask). 

3. Created test function (Hello world).

4. Inside our app.run() function, we set the host.

5. We use the os import (import os), get the IP and set the Port and set the debug to True.

6. We test by opening the https... and we see the Hello World

7. Create an acoount on Heroku and create a new app

8. Created uniqe name for the app and then choose Europe as a region

9. Next in our teminal window in our workspace we login (heroku login) and enter our credentials

10. writing heroku apps to the terminal

11. Git init, git add . git commit -m "Initial commit"

12. heroku git:remote -a (name of the app)

13. git push heroku master

14. However  we need to add our Procfile and requirements.txt in order to work

15. In terminal window we write:

    pip3 freeze --local > requirements.txt
    echo web: python run.py > Procfile
    add . commit -m "This cahnges" and again git push heroku master
    
16. heroku ps:scale web=1  for scaling dynos...

17. In heroku app open settings, Reveal Config wars

18. Set IP address to 0.0.0.0 and port 5000

19. The app was succesfully installed

20. To get Flask talking to Mongo we write in terminal window  (pip3 install flask-pymongo )

21. Install package called dnsython to use the new style  connection string for MongoDB atlas (pip3 install dnspython)

22  In our run.py we access the library from flask_pymongo (from flask import PyMongo)

23.  We say that MongoDB stores in JSON like format BSON (from bson.objectid import ObjectId)

24.  app config 

     app.config["MONGO_DBNAME"] = 'Recipes'
     app.config["MONGO_URI"] = "mongodb+srv://blanka:blanka@cluster0.w783e.mongodb.net/Recipes?retryWrites=true&w=majority"
     
25. In our cluster in MongoDB Atlas page click on overwiev and connect, click connect to our aplication

26. Copy the connection string and paste that in quotes, changing the name of database and adding our root password, see step n. 24.

27. Create a function with decorator using app route

    @app.route('/about')
    @app.route('/get_recipes')
    def get_recipes(): 
    return render_template("about.html", recipes=mongo.db.recipes.find())
    
28. another functionality from flask, render_template, request, redirect, url_for

29. I used "base.html" to link with other  pages with same navigation and footer and then just added block content in other pages.

30. Then I used the css cards for the recipes
    Reference: https://freefrontend.com/css-recipe-cards/, and from the mongoDB access the recipes on the "about.html" which is recipe page
    
{% block content %}
 
     {% for recipe in recipes %} 
     <div class="row">
     <div class="col-12 col-sm-6 col-md-3 col-lg-3">
<div class="card-container">
  <div class="card u-clearfix">
    <div class="card-body">
      <span class="card-number card-circle subtle"></span>
      <span class="card-author subtle"><strong>Allergies:</strong><br> {{recipe.recipe_allergens}}</span>
      <h2 class="card-title"> {{ recipe.recipe_name }}</h2>
      <span class="card-description subtle"><strong>Ingredients:</strong><br>  {{ recipe.recipe_ingredients}}</span>
      <button onclick="myFunction()">More...</button>
      <div id="myDIV"> {{ recipe.cooking_steps }} </div>
    </div>
    <img class="recipe_image" src="{{ recipe.recipe_image}}">
  </div>
  <div class="card-shadow"></div>
</div>
</div>

{% endfor %}

<script>
function myFunction() {
    var x =
  document.getElementById("myDIV");
  if (x.style.display ==="none")  
  {
      x.style.display = "block";
  }   else {
      x.style.display = "none";
  }
}
</script>

### Testing

I was adding the recipes to the mongodb and they automaticly were added to my app which I wanted to achieve.
Test fail - I wanted to have on all cards the button more... where you can wiev and also hide the cooking steps, as it looks better when hidden, however when I used the jquery to do that it is only working for the first recipe. I believe is because all the recipes have uniqu ID which is generated by MongoDB automaticly. I tried with the class but din't work.

### Credits

- [Bootstrap Themes ](https://startbootstrap.com/themes/)
- [Free-fronted CSS Cards](https://freefrontend.com/css-cards/)
- [w3schools](https://www.w3schools.com/howto/howto_css_contact_form.asp)
- [Code Institute solutions](https://github.com/Code-Institute-Solutions/readme-template)
- [Code Institute materials](https://courses.codeinstitute.net/courses/course-v1:codeinstitute+FE+2017_T3/info)

### Media


- [free-stock photo website](https://www.pexels.com/search/restaurant/)

### Acknowledgements

- My Mentor for his feedbacks and support
- Code Insttitute Team for their continuous support.
    



    













