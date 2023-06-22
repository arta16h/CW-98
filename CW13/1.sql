-- 1
SELECT film.title, category.name as category
FROM film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id;

--2
SELECT film.title, category.name as category, film.release_year
FROM film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
WHERE category.name IN ('Action', 'Comedy', 'Family');

--3
SELECT category.name, COUNT(film. film_id)
FROM film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id;

--4
SELECT category.name, COUNT(film. film_id)
FROM film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id 
GROUP BY category.name
having 60 < COUNT(film. film_id) < 68;

--5
SELECT film.title, category.name as category, language.name as language from film
join film_category on film.film_id = film_category.film_id
join category on category.category_id = film_category.category_id
join language on language.language_id = film.language_id;

--6
SELECT film.title, customer.first_name, (rental.return_rate - rental.rental_date) as rent_duration
from customer
join rental on rental.customer_id = customer.customer_id
join inventory on inventory.inventory_id = rental.inventory_id
join film on inventory.film_id = film.film_id
ORDER BY (rental.return_rate - rental.rental_date) DESC;

