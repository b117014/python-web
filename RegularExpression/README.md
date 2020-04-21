
## Regular Exprresion

- Regular expression is pattern to used the mathing of characters.

#### Library of Regular Expression in python
- import re     // re is the library of regular expression.

### Some syntax of RE

![](./Images/syntax.png)

#### some method of "re" library
- search
  1. re.search()    // search method work like find() if you find any word or pattern then we can use search.
- findall()
  1. to find all string which has match to the RE.

  ### Example of search method

  ![](./Images/SearchMethod.png)
  <img src="./Images/SearchMethod-2.png" height=400 width=800 >

<h3>Match Example </h3>
  <img src="./Images/MatchExample.png">
  <img src="./Images/MatchExample-2.png">

<h2> Greedy match </h2>
<img src="./Images/GreedyMatch.png>

## Non Greedy Match
- Use +? or *? operator for non greedy match. It will choose shorter string.
<img src="./Images/NonGreedyMatch.png">

## None blank Character Syntax
- [^ ] using this syntax regex return the non blank character.
- It serach untill blank character comes.
<img src="./Images/MatchNonBlankCharacter.png" >