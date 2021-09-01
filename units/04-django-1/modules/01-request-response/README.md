# Module 1: Request -> Response

## Videos

1. [App, Path, View](./videos/app_path_view.mp4)
2. [Request, Response](./videos/request_response.mp4)
3. [More about Paths](./videos/more_about_paths.mp4)
4. [Testing Views](./videos/testing_views.mp4)

## Exercises

### Exercise 1: Hello World

- [ ] Create a project in `~/projects/hello-django`.
- [ ] Create an app named `app` inside that project.
- [ ] Add a view that responds with `"Hello World!"` at the path `/hello`.

### Exercise 2: Functions Over HTTP

In the provided [functions-over-http](./exercises/functions_over_http) project's `app` app, implement the following view and path pairs. Test cases have been provided to help you check your work.

1. [ ] **Hey You:** Your app should respond with `Hey, <name>!` when a request is made to `/hey/<name>`. For example, a request to `/hey/bcca` should respond with `Hey, BCCA!`.
2. [ ] **How Old:** Your app should respond with a user's age in some provided end year when a request is made to `/age-in/<end>/<birthyear>`. For example `/age-in/2050/2000` should respond with `50`. Your path should appropriately indicate that the `end` and `birthyear` path arguments are integers.
3. [ ] **Can I Take Your Order:** Your app should respond with an order total for a provided number of hamburgers, fries, and drinks when a request is made to `/order-total/<burgers>/<fries>/<drinks>`. Burgers are $4.50. Fries are $1.5. Drinks are $1. Your path should appropriately indicate that the `burgers`, `fries`, and `drinks` path arguments are integers.

### Exercise 3: Codingbat Over HTTP

For each of the paths bases below, implement the corresponding codingbat challenge as a view. I've created a [codingbat_over_http](./exercises/codingbat_over_http) directory for you to create your project/app in. Arguments should be collected from the path and the response should contain the answer to the challenge. Additionally, you should implement three of the test cases that coding bat provides as test cases in your django app.

1. [ ] `warmup-1/near-hundred/...` implemented with 3 test cases.
2. [ ] `warmup-2/string-splosion/...` implemented with 3 test cases.
3. [ ] `string-2/cat-dog/...` implemented with 3 test cases.
4. [ ] `logic-2/lone-sum/...` implemented with 3 test cases.

## Mastery Check (Benchmark)

You will be asked to create a django project (and app) with a few small coding challenge style views that accept string or numeric information from the path. You will also be required to write test cases for these views.
