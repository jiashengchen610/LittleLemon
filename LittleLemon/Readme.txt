Hey, thanks for reviewing my work!!
here's the user and end point for testing:

Superuser:
{
    "username": "admin",
    "password": "0000"
}

Test user:
{
    "username": "test1",
    "password": "a12345678!"
}

here's the endpoints:
1. User Authentication Endpoints

- POST http://localhost:8000/api/auth/token/login/
  Description: Obtain a token for a registered user.
  Request Body:
  {
    "username": "admin",
    "password": "0000"
  }

- POST http://localhost:8000/api/auth/token/logout/
  Description: Logout the user and invalidate the token.
  Request Body: None (Token is sent via headers).

2. User Registration Endpoints

- POST http://localhost:8000/api/users/
  Description: Register a new user.
  Request Body:
  {
    "username": "new_user",
    "password": "new_password",
    "email": "user@example.com"
  }

- GET http://localhost:8000/api/users/me/
  Description: Retrieve the current authenticated user's details.
  Request Body: None (requires authentication token).

3. Menu Item Endpoints (for Restaurant App)

- GET http://localhost:8000/restaurant/menu/
  Description: Retrieve a list of all menu items.
  Response Body: A list of menu items in serialized format.

- POST http://localhost:8000/restaurant/menu/
  Description: Create a new menu item.
  Request Body:
  {
    "title": "Pizza",
    "price": 9.99,
    "inventory": 100
  }

- GET http://localhost:8000/restaurant/menu/{id}/
  Description: Retrieve a single menu item by its ID.
  Response Body: A single menu item with the specified ID.

- PUT http://localhost:8000/restaurant/menu/{id}/
  Description: Update an existing menu item by its ID.
  Request Body:
  {
    "title": "Updated Pizza",
    "price": 10.99,
    "inventory": 50
  }

- DELETE http://localhost:8000/restaurant/menu/{id}/
  Description: Delete a menu item by its ID.
  Request Body: None.

4. Booking Endpoints (for Restaurant App)

- GET http://localhost:8000/restaurant/booking/
  Description: Retrieve a list of all bookings.
  Response Body: A list of bookings in serialized format.

- POST http://localhost:8000/restaurant/booking/
  Description: Create a new booking.
  Request Body:
  {
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2024-12-01T19:00:00"
  }

- GET http://localhost:8000/restaurant/booking/{id}/
  Description: Retrieve a single booking by its ID.
  Response Body: A single booking with the specified ID.

- PUT http://localhost:8000/restaurant/booking/{id}/
  Description: Update an existing booking by its ID.
  Request Body:
  {
    "name": "Updated Name",
    "no_of_guests": 2,
    "booking_date": "2024-12-01T18:00:00"
  }

- DELETE http://localhost:8000/restaurant/booking/{id}/
  Description: Delete a booking by its ID.
  Request Body: None.
