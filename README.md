# ApplyBoard Hack the North Lightning Challenge  🎓

<p align="center">
  <a href="https://evilmartians.com/?utm_source=size-limit">
    <img src="https://didmdw8v48h5q.cloudfront.net/ca/wp-content/uploads/2018/07/New-2018-AB.png"
         alt="ApplyBoard Logo" width="170" height="50">
  </a>
</p>

## Background 📖

[applyboard-img]:                       https://didmdw8v48h5q.cloudfront.net/ca/wp-content/uploads/2018/07/New-2018-AB.png
At ApplyBoard, we believe that education is a right, not a privilege. We empower people around the world to access the best education available. Through our platform and team of experts, we streamline the application process, from submission to enrolment, assisting thousands of students pursue their dreams of studying abroad.

One of the most important aspects of our platform is our search page www.applyboard.com/quick_search which allows users to browse through our catalog and partnerships with over 1,200 of the top secondary and post-secondary institutions across North America. Users are able to discover schools and programs by applying a range of filters such as their country, province/state, school type, program level etc. In addition, users are able to discover their eligibility for these schools and programs by providing their nationality, education level, grading scheme, grading average and english exam type as an initial screening.

Ultimately our search page must take this huge amount of user input information and parse it for our backend to understand and return back the appropriate programs and schools according to the user's criteria.

## Problem 🖥

For this lightning challenge you must parse through an actual production sample json located at (`tests/challenge.json`) you receive from ApplyBoard.com. Our backend engineers however are unable to understand this JSON as all of the data types are strings. You must go through the json and convert each string into their appropriate datatype (eg. `"grade": "90"` of type string should be `grade: 90` of type integer.

The skeleton code and some basic tests are provided to you.

You have the choice of doing the challenge in one (or all if you are up for it) of three languages:
#### 1. JavaScript
* Input your solution in the `javascript_solution.js` file. The file should export a function called `refineParameters` (`module.exports` or `export` are both fine).
* (Optional) If you want to see if your code passes our test
1. Run `npm install` to install `jest` testing framework
2. Run `npm test` to see if the test pass
#### 2. Ruby
* Input your solution in the `ruby_solution.rb` file
#### 3. Python
* Input your solution in the `python_solution.py` file
* To test your solution locally use the following steps:
1. [Install](https://pip.pypa.io/en/stable/installing/) pip
2. Install `pytest` using the following command:
```
pip install -r requirements.txt
```
3. Use pytest to run the tests with the following command:
```
pytest
```

The winner of the challenge will be selected based on:

* Correctness
* Readability
* Efficiency
* Edge-case handling

## Rules ⚠
* You **may not** use any existing libraries, or copy existing code.
* You should fork this project, and submit your entry by submitting a pull request to `master`.
* Your latest commit must be on GitHub no later than the time specified by the engineer running the challenge.

## Prizes 🏆
**GOLD TIER (First Prize)**
* The winner of the ApplyBoard lightning challenge will receive a brand new Nintendo Switch! 🎮

**BRONZE Tier (Sucessful submission)**
* By completing this lightning challenge and submitting a pull request with the correct answer in any of the 3 languages you will receive an **ApplyBoard reusable straw**! Educate the world while saving the environment 🌲
