# Details about this Repository
This is the first application I made with Django (A Python Framwork). I made it in about 10 hours in september 2015. The goal was to design a simple API (Register / Authenticate / Get user's details)
I made it for a Job interview. On the 2nd part (-> Additionnal details about authentication) I am explaning the logic of my implementation and answering this question : 'How to avoid entering a password for the user ?'.

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
    * Simply copy past the response of the previous action, this is your token (1H validity)

# Additionnal details about authentication

To handle the expiration of the token : The token is a separate model, with a 1-N relation with the user (1 User - N Tokens). When the user authenticate if we are not able to found an active token (mean still valid) we create a new one. On the creation we attribute a datetime to the token. By this way we know when the token expirate (1 hour latter).

The advantage of using a separate table for the token is to keep traces of all the authentication of the user (we may imagine tracking IP, bad authentication and so on).

A 'sexy' by heavy authentication system to avoid entering password : During the registration step of a User, the server generate a private / public key. The public key is shared with the User, we could then imagine fully encrypted exchange between server and client. No need to ask a password to the client, all requests will be impossible to read without the appropriate key. The password is only required to get / generate a new key (if necessary).
