SELECT name, 
DATE_FORMAT(CONVERT_TZ(booking_date, '+00:00', '-08:00'), '%Y-%m-%d %h:%i %p') AS local_booking_time 
FROM restaurant_booking;
