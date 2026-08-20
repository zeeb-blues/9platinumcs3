# Computational Thinking Exercise
## Smart School Canteen Queue
**Name:** Ariel Aloysus G. Latosa<br>
**Section:** Platinum<br>
**Last Name:** Latosa<br>
**Date:** 08/11/2026
---
## Scenario
The PSHS school canteen is small and often gets crowded, during lunch break. Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.
---
## Step 1: Identify the Big Problem
### Main Problem
The PSHS school canteen is small and often gets crowded during lunch break, as the process students go through to buy food is slow.
---
## Step 2: Identify the Sub-Problems
1. Some students take too long to decide what to order.
2. The cashier has to manually calculate totals and give change.
3. There is no system to track which food items are running out.
---
## Step 3: Apply Computational Thinking Skills
|          Sub-Problem          |       CT Skill       |                 Proposed Solution                 |
|-------------------------------|----------------------|---------------------------------------------------|
|Some students take too long to |Decomposition, Pattern|Have stanchions be set up to people looking at the |
|decide what to order.          |Recognition, and      |people looking at the food on display from the     |
|                               |Algorithms            |people lining up to organize the already huge crowd|
|                               |                      |to avoid confusion among the students.             |
|-------------------------------|----------------------|---------------------------------------------------|
|The cashier has to manually    |Decompositions,       |Supply the cashier a register and an automatic     |
|calculate totals and give      |Abstraction, and      |dispenser to reduce the workload for the cashier   |
|change.                        |Algorithms            |and speed up the process.                          |
|-------------------------------|----------------------|---------------------------------------------------|
|There is no system to track    |Decompositions,       |Implement a system wherein workers taking students'|
|which food items are running   |Abstraction, and      |orders start the day off by calibrating newly built|
|out.                           |Algorithms            |counters for the food items. Then, as students     |
|                               |                      |order throughout the day, whenever a food item's   |
|                               |                      |stock goes down, workers manually set the number   |
|                               |                      |on its designated counter down by one.             |
---
## Step 4: Algorithmic Solution
### Select Sub-Problem
There is no system to track which food items are running out.
### Pseudocode
START
Running ← 1
DECLARE FoodItems ← []
WHILE Running = 1 THEN
    INPUT Choice
    IF Choice = 1 THEN
        INPUT NoOfFoodItems
        FOR FoodItem ← 1 TO NoOfFoodItems
            INPUT Number
            APPEND FoodItems ← Number
        NEXT FoodItem
    ELSE
        IF Choice = 2 AND FoodItems != [] THEN
            INPUT Index
            IF Index >= 0 AND Index < LENGTH OF FoodItems THEN
                INPUT Number
                FoodItems[Index] ← Number
            ENDIF
        ELSE
            IF Choice = 3 THEN
                Running ← 0
            ENDIF
        ENDIF
    ENDIF
END
---