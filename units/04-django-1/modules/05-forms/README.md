# Module 5: Forms

## Videos

1. [Hello Forms](./videos/hello-forms.mp4)
2. [HTML Forms 1](./videos/html-forms-1.mp4)
3. [HTML Forms 2](./videos/html-forms-2.mp4)
4. [HTML Forms 3](./videos/html-forms-3.mp4)
5. [Validating With Django Forms](./videos/validating-with-django-forms.mp4)
6. [Rendering Django Forms](./videos/rendering-django-forms.mp4)
7. [Validating Related Fields](./videos/validating-related-fields.mp4)

## Exercises

### Exercise 1: Functions Over HTTP (with Forms!)

In this exercise you will create a project that completes a task similar to the original "Functions over HTTP" exercise, but this time you will implement use a template and process the user input with a Django Form (no path parameters!).

> In the provided [functions-over-http](./exercises/functions_over_http) project's `app` app, implement the following view and path pairs. Test cases have been provided to help you check your work.
>
> 1. [ ] **Hey You:** Your app should respond with `Hey, <name>!` when a request is made to `/hey/<name>`. For example, a request to `/hey/bcca` should respond with `Hey, BCCA!`.
> 2. [ ] **How Old:** Your app should respond with a user's age in some provided end year when a request is made to `/age-in/<end>/<birthyear>`. For example `/age-in/2050/2000` should respond with `50`. Your path should appropriately indicate that the `end` and `birthyear` path arguments are integers.
> 3. [ ] **Can I Take Your Order:** Your app should respond with an order total for a provided number of hamburgers, fries, and drinks when a request is made to `/order-total/<burgers>/<fries>/<drinks>`. Burgers are $4.50. Fries are $1.5. Drinks are $1. Your path should appropriately indicate that the `burgers`, `fries`, and `drinks` path arguments are integers.

### Exercise 2: Codingbat Over HTTP (with Forms!)

In this exercise you will create a project that completes a task similar to the original "Codingbat over HTTP" exercise, but this time you will implement use a template and process the user input with a Django Form (no path parameters!).

> For each of the paths bases below, implement the corresponding codingbat challenge as a view. I've created a [codingbat_over_http](./exercises/codingbat_over_http) directory for you to create your project/app in. Arguments should be collected from the path and the response should contain the answer to the challenge. Additionally, you should implement three of the test cases that coding bat provides as test cases in your django app.
>
> 1. [ ] `warmup-1/near-hundred/...` implemented with 3 test cases.
> 2. [ ] `warmup-2/string-splosion/...` implemented with 3 test cases.
> 3. [ ] `string-2/cat-dog/...` implemented with 3 test cases.
> 4. [ ] `logic-2/lone-sum/...` implemented with 3 test cases.

## Mastery Check (Benchmark)

You will be asked to create a django project that accomplishes a task similar to the "Codingbat Over HTTP (with Forms!)" exercise.
