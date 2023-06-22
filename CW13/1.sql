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
SELECT category.name, COUNT(film. film_id) as count
FROM film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id

--4