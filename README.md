# set-statistics

Taking a look at the game Set, and running scripts to determine game behavior

## Overview

In my own words, [Set](https://www.playmonster.com/product/set/) is a pattern-matching speed-style card game where the goal is to form sets of 3 cards with complete matching or non-matching attributes.

This is more clearly described on the game's official website - [PlayMonster.com](https://www.playmonster.com/product/set/)(May 2022) - also listed below:

> The award-winning game challenges players to race to find as many SETs as they can! A SET is three cards where each individual feature (color, shape, number and shading) is either all the same OR all different! The first player to see a SET calls out “SET” and grabs the cards—there are no “turns” and no luck here! And not only is it fast-paced fun, it also builds skills and exercises the brain! Because it has a rule of logic, and because players must apply this rule to the spatial array of patterns all at once, they must use both left brain and right brain thought processes! At the end of the game, the player with the most SETs wins! SET is prefect for a wide age range and number of players (including solo play!), and is a fun intergenerational game as well.

The game's full instructions can be found on [setgame.com](https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf) or in [this repository](./set-instructions.md).

In this repository, you'll see references to a 'play' quite frequently. A play represents an idle state of the table, where all cards are down and players are scanning the table for a set. The instructions do not provide a term for this state, so 'play' has been chosen.

## Base facts

1. Set has exactly 81 cards in its deck.
2. A single set card has 4 attributes (shape, number, color, shading), each with 3 available states. Knowing this, we know there are 3ˆ4 (81) available card options.
3. Fact 1 and 2 together mean there are no duplicate cards in Set.
4. If we express the states of each available attribute with values - 1, 2, 3 - we can determine if a single attribute across 3 cards supports a valid set, if and only if, the sum of those values is divisible by 3.
5. The summation of a single attribute across 3 cards will always be between 3 and 9, inclusive.

## Invalid plays

In the game of Set, there is a condition where if all players aggree that if no sets can be found, 3 additional cards are temporarily added to the play. This is to ensure gameplay keeps moving, and can assist players who are less seasoned. The question I'd like to answer with this is, of all the available possible plays, how often is this condition necessary? Out of all the possible plays, how many of them contain no valid sets?
