Capstone: Peer-graded Assignment: Little Lemon Web Application, S/W Testing

Important Rules:   You have to be authenticated to,
1.  To create, that is, POST a booking, but you have to be admin to get all, update or 
delete bookings.  Non-admins can only see there own bookings and will get a Method not 
allowed error message in Insomia’s response panel, if they try to violate security.

2.  To retrieve, that is, do a GET to view all or single menu items, but ONLY admin 
can create, update or delete menu items.  Non-admins will get a Method not allowed 
error message in menu and a 404 Not Found in Booking if users violate security.

3.  Test menu and booking endpoints in DRF Browsable API.

ENDPOINT URL LIST To Be Tested:  Tests were done using Insomnia.

Note 1:  These 2 links are for Browsable API only: 
	/api-auth/ then, append login/ to endpoint    
    /api-auth/ then, append logout/ to endpoint
For more information, instructions and limitations on their use, see project level urls.py 
and find endpoint /api-auth/.  They do not work in Insomnia, only DRF Browsable API.  So, 
they were not used in s/w testing below.

Note 2: If you  use endpoint http://127.0.0.1:8000/api/users/3/, you will not be able to use 
the Extra Actions button found in djoser urls.  Auth endpoint puts email first, 
while /api/users/ puts username first.  It will also prevent you from using djoser
auto-created urls.

Tokens used in Testing: Can be done as Bearer token or by using Header tab in Insomnia.
Authorization token are examples.
- Account: admin, role admin
	HEADER Tab:
		Authorization Token a85fb0ea4c0487a71f0b8032237907c164a231b6
- Account: jen, non-admin
		Authorization Token  283a7b8f3434c716e81f23077116de29bfeab0b9

0.  Register a new user:

    	POST 				http://127.0.0.1:8000/api/registration/

1.  ADD or Retrieve users: One must use an admin account to do GET, but non-admin can POST a new account.

    	GET, POST 			http://127.0.0.1:8000/auth/users/

2.  Get single user id=7:

       GET, PUT, PATCH, DELETE	http://127.0.0.1:8000/auth/users/7/

3.  Get an access token by POST, by providing a username and password to prove 
authentication is configured.                                 

       POST 				http://127.0.0.1:8000/api/api-token-auth/

4.  Add, display or update Menu Items:  Test in Browsable and Insomnia.  Use admin account
to create, update and delete.  Non-admins can't do that, but they can GET to retrieve
the menu item list.

       GET, POST  			http://127.0.0.1:8000/api/menu/
       GET, PUT, PATCH, DELETE	http://127.0.0.1:8000/api/menu/13/

5.  Render to client an HTML 5 Template to display Welcome to Little  Lemon Restaurant 
and serves static HTML content.

    	http://127.0.0.1:8000/api/

6.  Add, display or update bookings:  Test in Browsable and Insomnia.  Use non-admin accounts
to create, update and delete bookings belonging only to them.  Admins can do everything.
 
    	GET POST http://127.0.0.1:8000/api/booking/
    	GET, PUT, PATCH, DELETE  http://127.0.0.1:8000/api/booking/26/

7. Do unit testing using Power Shell command in the directory containing manage.py:

		python manage.py test

S/W Testing Results:

1.  Does the web application use Django to serve static HTML content?  YES.

Renderd to client an HTML 5 Template to display “Welcome to Little Lemon Restaurant”  
containing a static content image logo.png from the static directory.

http://127.0.0.1:8000/api/

Output in VS Code terminal with Server status:
"GET /api/ HTTP/1.1" 					200 	397
"GET /static/img/logo.png HTTP/1.1" 	304 	0

HTTP Status Code: 200.  Means web page successfully rendered static content in the form 
of an image called logo.png, 304 means the page was not modified (cache hit).
 
Test Result: Passed.  Answer: YES.

------------------------------------------------------------------------------------------------------------------

2.  Has the learner committed the project to a Git repository?  YES

The project has been pushed (committed) to its Git repository over 5 times so far 
using these commands:

Steps to do a Push:

git remote show origin
git status
git diff
git branch
git checkout -B littlelemon
git add .
git push origin littlelemon
Last 2 lines of processing are very important.

To https://github.com/getmcd/LittleLemon.git
   7a34fcf..8a9cd1a  littlelemon -> littlelemon


They mean:
- The remote repository is LittleLemon.git
- The branch littlelemon on my machine was successfully pushed
- The remote branch littlelemon was updated
- It moved from commit 7a34fcf to commit 8a9cd1a
Logged into GitHub and opened repository LittleLemon.git.  

Created a Pull Request where feature branch littlelemon  compared to branch main, 
which is production.  When ready to merge is asserted by GitHub, did the merge and confirmed it.

Next Step, do a pull on remote main onto local main.

Steps to do a pull on main in the repository:

git branch
git status
git checkout main
git pull origin main

If the pull aborts, execute “git stash” and re-run the pull command.

git stash
git pull origin main

From https://github.com/getmcd/LittleLemon
 * branch            main       -> FETCH_HEAD
Updating 3aed4d6..9fa4c78

Meaning:
Git contacted the remote repository:
- https://github.com/getmcd/LittleLemon
- It fetched the remote branch named main
- It temporarily stored the fetched state in a special pointer called: FETCH_HEAD, which lets Git know:
- Here is what the remote branch currently looks like.
- It does not change your local branch yet.

Updating 3aed4d6..9fa4c78 means:
- The branch advanced from commit 3aed4d6 to commit 9fa4c78.
- Git downloaded new commit data
- Git learned the remote branch moved forward
The pull synchronizes, ie. Updates, client-side littlelemon with Git’s repository main, 
also known as production.   Now, the client-side littlelemon has an exact copy of 
production main.

------------------------------------------------------------------------------------------------------------------

3.  Does the application connect the backend to a MySQL database?  YES.

Used this PS command to install MySQL database.

pip3 install mysqlclient
Here is the database configuration for MySQL located in Settings.py file.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "LittleLemon",
        "USER": "root",
        "PASSWORD": "lemon@789!”	# for example
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "OPTIONS": {
            # keep your strict mode
            "init_command": (
                "SET sql_mode='STRICT_TRANS_TABLES'; "
                #"SET time_zone = '+00:00';"
            )
        },
    }
}

Enter this command to prove that the database settings work by connecting to MySql.

Mysql -u root -p

Enter password:  lemon@789!		# for example

Test database connectivity by doing a SELECT on a table by following these steps.

Step 1:

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| bookings           |
| information_schema |
| littlelemon        |
| menu_db            |
| menu_items         |
| mysql              |
| performance_schema |
| reservations       |
| restaurant         |
| sakila             |
| sys                |
| world              |
+--------------------+
12 rows in set (0.00 sec)

Step 2:  

Tell MySql to use database littlelemon.

mysql> use littlelemon;
Database changed

Step 3: 

Do a SELECT.

mysql> use littlelemon;
Database changed

mysql> Select * from restaurant_booking;
+----+------------------+------------------+----------------------------+---------+
| 19 | Pedro's family   |                4 | 2026-02-15 18:00:00.000000 |      12 |
| 20 | Cookie and Dad   |                2 | 2026-02-15 12:43:17.000000 |       7 |
| 22 | Jen              |               13 | 2026-02-21 20:44:00.000000 |       5 |
| 23 | Tom              |                2 | 2026-02-15 23:00:00.000000 |       1 |
| 24 | admin and family |                6 | 2026-02-15 13:15:35.000000 |       1 |
| 25 | admin            |                2 | 2026-02-25 20:44:00.000000 |       1 |
| 26 | Jen              |               22 | 2026-02-16 20:44:00.000000 |       5 |
+----+------------------+------------------+----------------------------+---------+
7 rows in set (0.00 sec)

Answer: Yes

The application connected to the backend’s MySQL littlelemon database and returned 7 records.

------------------------------------------------------------------------------------------------------------------

4.  Are the menu and table booking APIs implemented?   YES

Yes, here are the results of s/w testing on the menu and table booking API’s.  Menu uses path(), while booking uses the DefaultRouter() and does not use a path() mapping view to endpoint.

Used Insomnia to test both APIs.

MENU	TESTING:

=========================================================================
Tested menu CRUD, authorization and authentication capabilities having  Created, 
retrieved, updated and deleted model instances.  

The non-admin account must not be allowed to add, update or delete menu items.  
Only the admin account can do that.
------------------------------------------------------------------------------------------------------------------

Test admin account first:
	Account: admin, role admin
	HEADER Tab:
		Authorization Token a85fb0ea4c0487a71f0b8032237907c164a231b6
=========================================================================

Doing the GET is Read Only.

GET  http://127.0.0.1:8000/api/menu/

JSON Output:  Partial list
{
	"count": 9,
	"next": "http://127.0.0.1:8000/api/menu/?page=2",
	"previous": null,
	"results": [
		{
			"id": 5,
			"title": "beef pie",
			"price": "5.95",
			"inventory": 6
		},

HTTP Status Code: 200 OK.  9 menu items successfully retrieved.

Test Result: Passed.
------------------------------------------------------------------------------------------------------------------

POST  http://127.0.0.1:8000/api/menu/

With POST, must check with both an admin and a non-admin account.  The non-admin account 
must not be allowed to add, update or delete menu items.  Only admin can do that.

Note:  If you click link http://127.0.0.1:8000/api/menu/?page=2 in the response panel 
instead of adding ?page=2 to the input URL box next to the GET button, it will redirect to 
DRF Browsable API.

JSON Payload
{
	"title": "chicken pie",
	"price": "9.95",
	"inventory": 22
}

JSON Output
{
	"id": 14,
	"title": "chicken pie",
	"price": "9.95",
	"inventory": 22
}

HTTP Status Code: 201 Created.  Menu item chicken pie successfully created.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

GET http://127.0.0.1:8000/api/menu/14/

JSON Output
{
	"id": 14,
	"title": "chicken pie",
	"price": "9.95",
	"inventory": 22
}

HTTP Status Code: 200 OK.  Retrieved and displayed Menu item 14.
Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

PUT http://127.0.0.1:8000/api/menu/14/

JSON Before PUT:
{
	"title": "chicken pie",
	"price": "8.95",
	"inventory": 32
}
JSON Input Paylaod:
{
	"title": "chicken pie",
	"price": "9.95",
	"inventory": 22
}
JSON Output:
{
	"id": 14,
	"title": "chicken pie",
	"price": "9.95",
	"inventory": 22
}

HTTP Status Code: 200 OK.  Menu item 14 was successfully updated: price 8.95 to 9.95 
and inventory from 32 to 22.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

PATCH http://127.0.0.1:8000/api/menu/14/ 

JSON before PATCH
{
	"title": "chicken pie",
	"price": "9.95",
	"inventory": 22
}
JSON INPUT Payload
{
	"price": "8.95",
	"inventory": 32 }

JSON Output
{
	"id": 14,
	"title": "chicken pie",
	"price": "8.95",
	"inventory": 32
}

HTTP Status Code: 200 OK.  Retrieved Menu item 6 and successfully updated price to $7.95.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

DELETE http://127.0.0.1:8000/api/menu/3/

OUTPUT
No body returned for response

HTTP Status Code: 204 No Content.  Retrieved and successfully deleted menu item 6, Strawberry Ice Cream.

Test Result: Passed.


=========================================================================
Continue testing endpoint http://127.0.0.1:8000/api/menu/ , but with a non-admin account.
------------------------------------------------------------------------------------------------------------------

User: jen.  Is a non-admin account.
NON-ADMIN Account Authorization Token  283a7b8f3434c716e81f23077116de29bfeab0b9
=========================================================================

POST http://127.0.0.1:8000/api/menu/

JSON Payload:
{
		"title": "Lamb Stew",
		"price": "8.95",
		"inventory": 32 }
JSON OUTPUT:
{
	"detail": "You do not have permission to perform this action."
}

HTTP Status Code: 403 Forbidden.  Success: Non-admin accounts were NOT allowed create 
new menu items using POST Http Method.  The custom IsAdminOrReadOnly permission worked 
to prevent unauthorized access by non-admins

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

GET http://127.0.0.1:8000/api/menu/

JSON Output:
{
	"count": 11,
	"next": "http://127.0.0.1:8000/api/menu/?page=2",
	"previous": null,
	"results": [
		{
			"id": 13,
			"title": "Avocado Sandwhich",
			"price": "9.95",
			"inventory": 14
		},# first 11 lines of output

HTTP Status Code: 200 OK.  Retrieved and displayed all Menu items successfully using non-admin account.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

GET http://127.0.0.1:8000/api/menu/14/

JSON Output:
{
	"id": 14,
	"title": "chicken pie",
	"price": "8.95",
	"inventory": 32
}
HTTP Status Code: 200 OK.  Retrieved and displayed Menu item 14 successfully using non-admin account.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

PUT http://127.0.0.1:8000/api/menu/14/

Update inventory to 31.

JSON Payload
{
		"title": "Lamb Stew",
		"price": "9.95",
		"inventory": 32
 }
JSON Output:
{
	"detail": "You do not have permission to perform this action."
}

HTTP Status Code: 403 Forbidden.  Success: Non-admins were NOT allowed to update menu items.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

PATCH http://127.0.0.1:8000/api/menu/14/ 

JSON INPUT Payload
{
	"price": "9.95",
	"inventory": 32
 }
JSON Output
{
	"detail": "You do not have permission to perform this action."
}

HTTP Status Code: 403 Forbidden.  Success: Non-admins were NOT allowed to update menu items.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

DELETE http://127.0.0.1:8000/api/menu/6/

JSON OUTPUT
{
	"detail": "You do not have permission to perform this action."
}

HTTP Status Code: 403 Forbidden.  Success: Non-admins were NOT allowed to delete menu items.

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------

BOOKING:

=========================================================================

Tested POST, GET, PUT, PATCH, DELETE for endpoint http://127.0.0.1:8000/api/booking/  

------------------------------------------------------------------------------------------------------------------
Test admin account first:
	Account: admin, role admin
	HEADER Tab:
		Authorization Token a85fb0ea4c0487a71f0b8032237907c164a231b6
=========================================================================

GET http://127.0.0.1:8000/api/booking/

JSON Output
{
	"count": 6,
	"next": "http://127.0.0.1:8000/api/booking/?page=2",
	"previous": null,
	"results": [
		{
			"id": 22,
			"name": "Jen",
			"number_of_guests": 15,
			"booking_date": "2026-03-24T20:44:00",
			"user": 5
		},  # First 12 lines
HTTP Status Code: 200 OK. Admin successfully retrieved all Bookings for all users. 

Test Result: Passed.  

------------------------------------------------------------------------------------------------------------------

POST http://127.0.0.1:8000/api/booking/

JSON Input Payload
{
	"name": "admin",
	"number_of_guests": 2,
	"booking_date": "2026-02-25T20:44:00"
}
JSON Output

{
	"id": 25,
	"name": "admin",
	"number_of_guests": 2,
	"booking_date": "2026-02-25T20:44:00",
	"user": 1
}

HTTP Status Code: 201 Created. Admin successfully Booked a table 

Test Result: Passed, admin has full control over booking.

------------------------------------------------------------------------------------------------------------------

GET  http://127.0.0.1:8000/api/booking/22/

JSON Ouput:
{
	"id": 22,
	"name": "Jen",
	"number_of_guests": 15,
	"booking_date": "2026-03-24T20:44:00",
	"user": 5
}

HTTP Status Code: 200 OK. Admin successfully retrieved  Booking 22 belonging 
to non-admin Jen.
Test Result: Passed, admin has full control over booking.
------------------------------------------------------------------------------------------------------------------

PUT  http://127.0.0.1:8000/api/booking/22/

Output before PUT:
{
	"id": 22,
	"name": "Jen",
	"number_of_guests": 15,
	"booking_date": "2026-03-24T20:44:00",
	"user": 5
}
JSON Input Payload
{
	"name": "Jen",
	"number_of_guests": 8,
	"booking_date": "2026-02-27T20:44:00",
	"user": 5
}
JSON Ouput:
{
	"id": 22,
	"name": "Jen",
	"number_of_guests": 8,
	"booking_date": "2026-02-27T20:44:00",
	"user": 5
}

HTTP Status Code: 200 OK. Admin successfully updated  number of guests and date for 
Booking 22 belonging to non-admin Jen. 

Test Result: Passed, admin has full control over booking.

------------------------------------------------------------------------------------------------------------------

PATCH  http://127.0.0.1:8000/api/booking/22/

JSON Input Payload
{
	"number_of_guests": 2
}

JSON Ouput:
{
	"id": 22,
	"name": "Jen",
	"number_of_guests": 2,
	"booking_date": "2026-02-27T20:44:00",
	"user": 5
}

HTTP Status Code: 200 OK. Admin successfully updated  number of guests for 
Booking 22 belonging to Jen.

Test Result: Passed, Admin as control over update ooking.


------------------------------------------------------------------------------------------------------------------


DELETE  http://127.0.0.1:8000/api/booking/21/

Ouput:

HTTP Status Code:  204 No Content, No body returned for response.  Admin successfully deleted Booking 16 belonging to Jen.

Test Result: Passed, but only on ability to delete a booking.

=========================================================================

User: jen.  Is a non-admin account.
------------------------------------------------------------------------------------------------------------------

NON-ADMIN Account Authorization Token  283a7b8f3434c716e81f23077116de29bfeab0b9
=========================================================================
      
GET http://127.0.0.1:8000/api/booking/

JSON Output
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 22,
			"name": "Jen",
			"number_of_guests": 2,
			"booking_date": "2026-02-27T20:44:00",
			"user": 5
		}
	]
}

HTTP Status Code: 200 OK. Jen successfully retrieved only  Bookings that only belong to her. 

Test Result: Passed.  Recommend to add IsAdminOrReadOnly


------------------------------------------------------------------------------------------------------------------

POST http://127.0.0.1:8000/api/booking/

JSON Input Payload
{
	"name": "Jen",
	"number_of_guests": 22,
	"booking_date": "2026-02-16T20:44:00"
}
JSON Output
{
	"id": 26,
	"name": "Jen",
	"number_of_guests": 22,
	"booking_date": "2026-02-16T20:44:00",
	"user": 5
}

HTTP Status Code: 201 Created. Jen successfully Booked a table 

Test Result: Passed.

------------------------------------------------------------------------------------------------------------------
      
GET  http://127.0.0.1:8000/api/booking/25/

Booking 25 is admin and does not belong to non-admin jen.  Instead of responding with a 
403 Forbidden, it’s more secure to respond with a 404 not found.

Important:  When a non-admin tries:
-  PUT /api/bookings/123/ , where booking 123 belongs to someone else,  DRF tries to find 
the object using my filtered queryset:
--  Booking.objects.filter(user=request.user).get(pk=123)
- That returns no rows, so DRF concludes: No Booking matches the given query.
- Responds with 404 Not Found.
- This is actually a common security-friendly pattern
- Returning 404 for “not yours” avoids leaking whether the object exists (it prevents “ID probing”).

JSON Ouput:
{
	"detail": "No Booking matches the given query."
}

HTTP Status Code: 404 Not Found. Jen was NOT successful at updating   Booking 25, which  
belongs to user admin, not her.

Test Result: Passed, Security maintained by not responding with a 404 Not Found, NOT a 403 Forbidden.

------------------------------------------------------------------------------------------------------------------

PUT  http://127.0.0.1:8000/api/booking/25/

JSON Input Payload
{            
  "name": "admin",
  "number_of_guests": 4,
  "booking_date": "2026-02-25T20:44:00"
}
JSON Ouput:
{
	"detail": "No Booking matches the given query."
}

HTTP Status Code: 404 Not Found. Jen was NOT successful at updating   Booking 25, which  
belongs to user admin, not her.

Test Result: Passed, Security maintained by not responding with a 404 Not Found, 
NOT a 403 Forbidden.

------------------------------------------------------------------------------------------------------------------

PATCH  http://127.0.0.1:8000/api/booking/25/

JSON Input Payload
{
	"number_of_guests": 20,
}

JSON Ouput:
{
	"detail": "No Booking matches the given query."
}

HTTP Status Code: 404 Not Found. Jen was NOT successful at updating   Booking 25, which  
belongs to user admin, not her.

Test Result: Passed, Security maintained by not responding with a 404 Not Found, 
NOT a 403 Forbidden.

------------------------------------------------------------------------------------------------------------------

DELETE  http://127.0.0.1:8000/api/booking/25/

Ouput:
{
	"detail": "No Booking matches the given query."
}

HTTP Status Code: 404 Not Found. Jen was NOT successful deleting Booking 25, which  belongs 
to user admin, not her.

Test Result: Passed, Security maintained by not responding with a 404 Not Found, 
NOT a 403 Forbidden.

------------------------------------------------------------------------------------------------------------------

5.  Is the application set up with user registration and authentication?  YES

A.  Registration, this endpoint allows a user to create and register a new account 
using Insomnia with NO access token:

POST	http://127.0.0.1:8000/api/registration/

JSON Payload:
{
  "username": "Lory",
  "email": "lor@littlelemon.com",
  "password": "lemon@lor!"
}
JSON Output:
{
	"id": 15,
	"url": "http://127.0.0.1:8000/api/users/15/",
	"username": "Lory",
	"email": "lor@littlelemon.com"
}

HTTP Status Code: 201 Created
Admin Panel User Status: Active, customer can register and then generate access tokens

Test Result: Passed.  API is setup for user registration.

------------------------------------------------------------------------------------------------------------------

B.  Authentication, will create an Authorization Token using endpoint /auth/token/login/. 

 If my API successfully returns an authorization token, it proves that:
-  API has authentication configured
-  API is using token-based authentication

This confirms:
- The user’s credentials were validated
- The system generated (or retrieved) a token
- TokenAuthentication is active in my project

POST http://127.0.0.1:8000/auth/token/login/

Endpoint /api/users/ cannot create an authorization token.  
Note:  Only POST is allowed for this endpoint.

JSON Body Payload:
{
	"username": "jen",
	"password": "lemon@jen!"
}
JSON Output:
{
	"auth_token": "283a7b8f3434c716e81f23077116de29bfeab0b9"
}

HTTP Status Code: 200 OK
Customer can generate Authorization tokens using /auth/token/login

Test Result: Passed.  Authenication was used successfully to obtain an Authorization Token.

------------------------------------------------------------------------------------------------------------------

6.  Does the application contain unit tests?  YES

YES, it contains two unit tests in a tests directory at the project level with an 
empty __init__.py to turn it into a package.

Test_models.py:

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80.00")

test_views.py:

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a normal user and authenticate
        self.user = User.objects.create_user(username="tester", password="pass1234!")
        self.client.force_authenticate(user=self.user)

        # Create test data
        MenuItem.objects.create(title="IceCream", price="8.00", inventory=50)
        MenuItem.objects.create(title="Burger", price="10.00", inventory=20)

    def test_getall(self):
        # Adjust path if yours is different (e.g., "/api/menu/")
        response = self.client.get("/api/menu/")

        # compares response status code with expected code 200 OK
        self.assertEqual(response.status_code, 200)

        # If pagination is ON, data is in response.data["results"]
        data = response.data.get("results", response.data)

        # self.assertEqual(len(data), 2) verifies that the API returned two menu 
        # items, matching the two objects created in the test setup().
        # - Your view is connected
        # - Database objects exist
        # - Queryset is correct
        # - Serialization worked
        
        self.assertEqual(len(data), 2)

        # Because you order_by("title"), Burger comes before IceCream
        self.assertEqual(data[0]["title"], "Burger")
        self.assertEqual(data[1]["title"], "IceCream")


In terminal at PS prompt, enter this command to run the tests automatically.

python manage.py test      

PS C:\Capstone-project\littlelemon> python manage.py test      

Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.219s

OK
Destroying test database for alias 'default'...

Test Result: Passed.  OK displayed, Unit Testing resulted in no errors found.

------------------------------------------------------------------------------------------------------------------

7.  Can the API be tested with the Insomnia REST client?

Yes, s/w testing confirmed that all endpoints were successfully tested using Insomnia REST client.


https://github.com/Codem-3/Little-Lemon-a