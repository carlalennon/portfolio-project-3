
# Closing Time : A Pub RPG

![The menu of Closing time](./images/rm-menu.png)

## Description

"Closing Time" is a basic text-based RPG about spending the night in a pub. You must avoid social errors, boring conversation, and aggressive patrons to survive as long into the night as you can. 

The project was inspired by the cyclicle nature of rural life, how the patrons of the typical Irish "local" have their allocated seats, usual drinks, and rarely deviate from their routines. There's a comfort in knowing who everyone is. My game aims to capture the feel of small town life in a quirky and funny way.

I chose an old fashioned RPG because I am interested in old tech. I grew up in the era of game guides being written in ASCII art and printed onto sheets of paper. I have a deep fondness for all things early internet culture, and I wanted to experiment with a branching decision tree type RPG.

The goal of the project is to entertain the player, as they navigate through a night in a small local pub.

## Project Features

![The user interface](./images/rm-ui.png)

![Taking the user name input](./images/rm-name.png)

Closing Time is simple, but has a few features:
- An in game clock that prints the time as the player makes decisions throughout the night.
- A tile that indicates the room the player is in.
- A function that take's the player's name
- A score counter that keeps tabs on the player's score
- A branching decision tree that brings the player through a narrative
- A narrative that features consequences for your actions
- Answers are case insenstive

I knew I definitely didn't want to have fifty chained if/else statements, so I endeavoured to build a "state machine" that would handle nearly all the narrative and player answers. This gave me problems at the Game Over part of the game, but it allows me in theory to add as many questions and scenarios as I can dream up.

## Installation Instructions

To play the game, head to this URL: [https://portfolio-project-carla-lennon-3003e71640e8.herokuapp.com/]

The game should deploy on opening this page.
In the future, I would like to export the file as a standalone application to share with friends.

## Usage Guide

To navigate the game, you must enter the text in [Square Brackets] to answer each question.

There is a character guide in the "About" section of the menu. 

To restart the game, click the "Run Program" button at the top of the web page.

![How to restart the game](./images/rm-restart.png)

## Credits

I did relatively little research for this game, compared to my last project. Python logic came together easily after building the first function from the linked tutorial below. 

Once I understood that the order in which functions are called is important in Python, the coin dropped for me in creating the game loop.

- [Baober Video Containing the Player Function](https://www.youtube.com/watch?v=xHPmXArK6Tg&list=PL1-slM0ZOosXf2oQYZpTRAoeuo0TPiGpm&index=2&ab_channel=Baober)
- [W3 Schools: Nested Dictionaries](https://www.w3schools.com/python/python_dictionaries_nested.asp)
- [Code to Clear The Screen (Unused)](https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python)
- [Iterating Through A Python Dictionary](https://blog.enterprisedna.co/python-iterate-dictionary/#:~:text=To%20access%20both%20dictionary%20keys,for%20each%20key%2Dvalue%20pair.&text=This%20script%20will%20print%20both,values%20of%20a%20Python%20dictionary.)
- [More Iterating Through Python Dictionarys](https://realpython.com/iterate-through-dictionary-python/)
- [Python Compiler I Used for Testing](https://www.programiz.com/python-programming/online-compiler/)
- [General Python reading](https://www.pygame.org/news)

## Testing

I tested this game as I build it. This was both to check that the game worked, and that as I was adding dictionaries they were properly formatted.

I used the Programiz compiler to test my game as I went. This allowed me to have the game open on one screen and VS Code open in the other.

Despite my testing, there are many errors still in this game.

My code goes through the VSCode Python linter with no issues

![Linter pass: yay!](./images/rm-linter.png)

## Failing Criteria

Here's the criteria where the project failed, and what I did to fix them.

1. The project does not handle incorrect inputs correctly
   <details>
    <summary>2.1 Fail in Assessment</summary>
        <img src="images/readme-failing-criteria-1.png" alt="	The application rigorously checks user input only for the initial question. For subsequent questions, it fails to handle empty or invalid inputs, leading to the application crashing. This needs addressing to ensure consistent user experience throughout."/>
    </details>
       <details>
    <summary>3.2 Fail in Assessment</summary>
        <img src="images/readme-failing-criteria-2.png" alt="	The application rigorously checks user input only for the initial question. For subsequent questions, it fails to handle empty or invalid inputs, leading to the application freezing/pausing and not going forward. This needs addressing to ensure consistent user experience throughout."/>
    </details>
        <summary>2.1 and 3.1 Fail in Assessment</summary>
        <img src="images/readme-failing-criteria-3.png" alt="	The application rigorously checks user input only for the initial question. For subsequent questions, it fails to handle empty or invalid inputs, leading to the application freezing/pausing and not going forward. This needs addressing to ensure consistent user experience throughout."/>
    </details>
    
    I solved this by accident. When opening the file, I noticed the dictionarys made the file very long and hard to work with. After working through PP4, I was more comfortable with Python. I decided to move the dictionarys to their own files. 


    <img src="images/readme-new-files.png" alt="The new files in the project">

    I set up two calls in the main file, one calls the choice dictionary and one calls the narrative dictionary 

    <img src="images/readme-new-files-calls.png" alt="The calls for the dictionarys">

    I then placed the dictionarys in the files, and wrapped them in a function that declares them. The run file calls these functions, and the dictionarys are delivered inside them to the game 

    <img src="images/readme-new-files-narrative.png" alt="The function in the narrative dictionary">
    <img src="images/readme-new-files-choice.png" alt="The function in the choice dictionary">

    I then deployed the project to Heroku to check that these dictionarys are being called correctly. Then, after breaking my project into a smaller size, I got started trying to replicate the first error it failed on. But......

    <img src="images/readme-failing-criteria-error-replication.png" alt="A string of increect inputs handled correctly">

    I can no longer replicate this error! I believe what happened is that when an incorrect answer is entered, the function for a dictionary entry is called again. Before, an incorrect answer would point to an empty space in a dictionary, causing the error. This is how I solved the incorrect answer handling by accident.

2. Functions are missing explanatory comments

    <details>
    <summary>1.1 Fail in Assessment</summary>
        <img src="images/readme-failing-criteria-2.png" alt="	Functions are missing explanatory comments">
    </details>

    Easliy remidied by adding comments to functions.

    <img src="images/readme-failing-criteria-comments.png" alt="Some comments in functions from run.py">

3.  Lack of documentation of errors
4.  
    <details>
    <summary>5.1 Fail in Assessment</summary>
        <img src="images/readme-failing-criteria-5.png" alt="The README file contains a note about the use of the PEP8 linter and input validations, but results are only mentioned. Consider documenting the PEP8 results, test input validations, unexpected user behavior and edge cases.">
    </details>

    This is tricky to fix, as memories of errors fixed in October are long gone. However, I will address some known issues and document that process here, and also the major error solve above has been documented in detail. 

    For known issue
    - If the player takes certain routes, the clock will run out of numbers to print, and print "TimeError" instead.
    -   I will fix this by adding more times to the clock
    -  <img src="images/readme-failing-criteria-extra-time.png" alt="Player clock with added times for 4am and 5am">
    -  The player can now drink in the pub until the sun comes up without running out of time. If the player take a paticularly long path there will still be enough time.
<br>
        For known issue
    - The room printer will break on several scenarios, due to the room not being entered into the dictionary.
    -   I will fix this by adding all rooms in dictionary 
    - <details>
    <summary>Error from broken room key</summary>
        <img src="images/readme-error-01-room-crash.png" alt="The error that shows when there's no room key in a dictionary">
    </details>


## Known Issues

- There are only 3 choices in the first message, when there were originally intended to be 5.
- The score function always adds a positive, even if the player loses.

## Future Improvements

- Add the last two branchs into the game
- Add more times to the clock OR limit the length of certain players paths to be less than the time limit
- Implement a system wherein the player can type their answer incorrectly as many times as they like without breaking the game
- Add negative scoring to the game
- Fix all instances of the room printer
- Add an option to play again upon game completion

## Final Thoughts

I enjoyed learning Python. I regret not having time to fully implement my vision, due to overtime at work this month. I may continue with this project.

Python is integral to my career path as an animator. I contacted several technical animators, animation software developers and pipeline specialists over the last month. They all said that Python was essential, as a lot of automation in animation is opening folders, putting all the images into video format, and moving those files into a cloud based production software. 