# kolibree_backend_test

Test started at 22:01 - 25/09/2015

# Edit 23:31 - 25/09/2015

Difficult start, I wasted time to setup my environment properly, my IDE was stucked on python version 2.6.9 and it toke me a while to figure how to fix it. 

I choosed to work with mysql during this projet.

Then I toke my time (about 40min) to understand all the possible type for the model definition and what was their possible options.

I am going to explain this choices here : 
NB : For a reason I decided to setup blank=False for every field even if it's the default comportment, I feel it more readable this way.
 
I decided to create 2 tables :
*  User : based on your requirement
*  UserToken : This table will be used to keep record of the user authentications.
  *  A foreign key to the User (The relation is 1-N, I want to keep a record of all authentication)
  *  The token field is a UUIDField, I am not 100% sure about what is it for, but it looks to be able to genreate unique 32 chars long string what is good for my need ;). 
  *  The creation_datetime field is ... a datetime ;) this value will be automaticly set to 'now' on the creation (if auto_now option works as I expect). My idea is to create a DEFINE to setup how long a token is valid and to use relative DateTime comparaison to check if the token is still valid or not

# Edit 00:12 - 26/09/2015

I finaly manage to have a properly working migration (CharFields were missing mendatory parameters)

Let's move on models basic tests 

# Edit 04:00 - 29/09/2015

I had to do a break on this test during the last 3 days.

The base features of my models are now finished :
  * Creation of the user
  * Creation of the token
  * Validation of the token (according to expiration settings)

This features are fully tested (100% coverage)

I am now going to work on the API side of this project - I choosed to use django-rest-framework to do so
