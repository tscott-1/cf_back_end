# cf_back_end
A repository for a django crowd funding back end in SheCodesPlus

# Crowdfunding Back End
Tenille Scott

## Planning:
### SPPORRT
A crowdfunding site for sports clubs to raise money for various activities or events.

### Intended Audience/User Stories
Club owners can create a sports club - club location and club size to be specified:
        ("S", "< 10 Members"),
        ("M", "10-50 Members"),
        ("L", "50-120 Members"),
        ("XL", ">120 Members"),
Club owners can create a project for their sports club - project purpose to be specified:
        ("E", "Equipment and Uniforms"),
        ("C", "Competitions and Events"),
        ("F", "Players Fees"),
        ("S", "Coaching"),
        ("I", "Club Infrastructure")
Club owners can add club members to their club
Club owners can specify if pledges are only available to club members (this is useful for club events or coach gifts)
Supporters can pledge a donation or contribution towards a project
Club member supporters can pledge a donation or contribution towards a member-only project for their club.

### Front End Pages/Functionality
- Add a sport 
  - requires sport and sport-type (i.e. Field/Court/water/Athletics)
- 
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose     | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ----------- | ------------ | --------------------- | ---------------------------- |
| https://spporrt-5d288951e37a.herokuapp.com/users/    |      GET       |      Get a list of users    |       n/a      |              200         |            none                  |
| https://spporrt-5d288951e37a.herokuapp.com/users/    |      POST      |      add a user    |      {username, email, password}     |              200         |            none                  |
| https://spporrt-5d288951e37a.herokuapp.com/api-token-auth/   |      POST       |      Get a User Token    |      {username, password}      |              200         |            none                  |
| https://spporrt-5d288951e37a.herokuapp.com/users/(pk)   |     GET     |      Get User Details    |      n/a    |              200         |            none  |
| https://spporrt-5d288951e37a.herokuapp.com/sports/    |     POST    |      Add a Sport    |      {sport, sport_type}   |              200         |            Authorised User  |
| https://spporrt-5d288951e37a.herokuapp.com/sports/    |     GET    |      Get List of sports   |     n/a    |              200         |            none |
| https://spporrt-5d288951e37a.herokuapp.com/sports/(pk)   |  GET    |      Get Sports Details   |     n/a    |              200         |            none |
| https://spporrt-5d288951e37a.herokuapp.com/sports/(pk)   |   GET   |      Get Sports Details   |     n/a    |              200         |            none |
### DB Schema
![ERD Diagram](./images/ERD.jpg )

