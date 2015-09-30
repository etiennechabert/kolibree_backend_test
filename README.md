# Welcome

# First impression about this test
First of all I would like to apologize for the deliver delay of this test.
I was in a rush during my last month of work, and needed a break a the end of my previous contract (last wednesday).
I began this test Saturday, and work on it with an average of 3H / Day for a total arround 10-12h of work
It was a bit painful to be honest (my first run with Django) ;) Exceptions were sometimes a bit hard to understand and fix, the framework looks pretty strict (this is a good point for me)

I will be happy to talk with you about the choices I made, even if I am not totally confident about it ;) 

# API Actions
* API Root page (api/users [GET])
    * A short usage about possible actions of the API

* Register users (api/users [POST])
    * Example of a usable json (just copy past it)
{ "first_name" : "Etienne", "last_name" : "Chabert", "date_of_birth" : "1990-11-18", "password" : "mon_pass", "email" : "mail@mail.com }

* Auth user (api/users/auth [POST])
    * Exemple of a usable json (just copy past it)
{ "email" : "mail@mail.com", "password" : "mon_pass" }

* Retrieve user (api/users/retrieve [POST])
    * Simply copy past the response of the previous action to get your token

# Additionnal details about authentication

To handle the expiration of the token : The token is a separate model, with a 1-N relation with the user (1 User - N Tokens). When the user authenticate if we are not able to found an active token (mean still valid) we create a new one. On the creation we attribute a datetime to the token. By this way we know when the token expirate.

The advantage of using a separate table for the token is to keep traces of all the authentication of the user (we may imagine tracking IP, bad authentication and so on).

A 'sexy' by heavy authentication system to avoid entering password : During the registration step of a User, the server generate a private / public key. The public key is shared with the User, we could then imagine fully encrypted exchange between server and client. No need to ask a password to the client, all requests will be impossible to read without the appropriate key. The password is only required to get / generate a new key (if necessary).

This solution is a bit overkill, but I like it ;)
