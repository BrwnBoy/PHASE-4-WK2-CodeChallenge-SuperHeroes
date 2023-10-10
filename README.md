# PHASE-4-WK2-CodeChallenge-SuperHeroes
**Authour**: *Brian Mwangi Maina.*

## Prerequisites:

**Technologies Used**

<li>Python
<li>REACT
<li>JSON
<li>Render

****
**Setup/Installation Requirements**

*To run the application, in your terminal*

<li>Open the terminal and clone the repository to your local machine://git@github.com:BrwnBoy/PHASE-4-WK2-CodeChallenge-SuperHeroes.git//
<li>cd into *PHASE-4-WK2-CodeChallenge-SuperHeroes*
<li>Finally, open up vs.code by typing in (code .) while in the repository.

### What Goes Into Making The Programs Run:

(1)**Models**: This module defines the database models and establishes the relationships between them.In this case, there are three models: Hero, Power, and HeroPower.The relationships are defined as follows:
*A Hero has many Powers through HeroPower.*
*A Power has many Heros through HeroPower.*
*A HeroPower belongs to a Hero and belongs to a Power.*

(2)**Validations**: This module adds validations to the HeroPower and Power models. The validations ensure that certain conditions are met before saving the data to the database. For example, the strength attribute of HeroPower must be one of the values: *'Strong', 'Weak', or 'Average'. The description attribute of Power must be present and at least 20 characters long.*

(3)**Routes**: *This module sets up the routes for the Flask application. Each route corresponds to a specific HTTP verb and URL path. Here are the routes defined*:
<li>GET /heroes: Returns a JSON response with information about all the heroes in the database.
<li>GET /heroes/:id: Returns a JSON response with information about a specific hero based on the provided ID.
<li>GET /powers: Returns a JSON response with information about all the powers in the database.
<li>GET /powers/:id: Returns a JSON response with information about a specific power based on the provided ID.
<li>PATCH /powers/:id: Updates the description of a specific power based on the provided ID.
<li>POST /hero_powers: Creates a new HeroPower record associated with an existing Power and Hero.

(4)**Error handling**: *The code includes error handling for certain scenarios. Here's an overview of the error handling in the provided routes*:
**GET /heroes/:id**:
If the requested hero does not exist, the route returns a JSON response with the following data:
     {
       "error": "Hero not found"
     }
The appropriate HTTP status code is also returned to indicate that the resource was not found.

**GET /powers/:id**:
If the requested power does not exist, the route returns a JSON response with the following data:
     {
       "error": "Power not found"
     }
The appropriate HTTP status code is also returned to indicate that the resource was not found.

**PATCH /powers/:id**:
If the requested power does not exist, the route returns a JSON response with the following data:
     {
       "error": "Power not found"
     }
The appropriate HTTP status code is also returned to indicate that the resource was not found.
If the power fails validation and is not updated successfully, the route returns a JSON response with the following data:
     {
       "errors": ["validation errors"]
     }
The appropriate HTTP status code is also returned to indicate that the request was not successful.

**POST /hero_powers**:
If the HeroPower fails validation and is not created successfully, the route returns a JSON response with the following data:
     {
       "errors": ["validation errors"]
     }
The appropriate HTTP status code is also returned to indicate that the request was not successful.

*These error handling mechanisms ensure that appropriate error messages are returned to the client when certain conditions are not met or when requested resources are not found.*
****

#### License 

Copyright (c) 2023 Brian Mwangi Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
****
**Deployed Application Link**:(https://superheroes-2gym.onrender.com)
****
