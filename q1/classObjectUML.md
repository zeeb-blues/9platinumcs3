# SG4 - Understanding Classes and Objects
## Class Name
Context / Class Name: Mathematics / Function

## Class Description
The class represents relations in a mathematical context that have only one output (y) assigned to each input (x), describing the properties (e.g., degree, leading coefficient, constant, and name) and actions (e.g, shifts, reflections, stretches, and compressions) pertained to its instances.

## Properties
| Property | Data Type | Description |
|---|---|---|
|name|string|the label of a function. (e.g., f(x), g(x), and h(x))|
|degree|float|the highest degree of variable x.|
|leading_coefficient|float|the numerical coefficient of the term with the highest degree.|
|constant|float|the numerical coefficient of the term with no x beside it.|

## Methods
| Method | Description |
|---|---|
|xshift|shifts the graph by a number of units horizontally given by the user.|
|yshift|shifts the graph by a number of units vertically given by the user.|
|xreflect|reflects the graph across the x-axis.|
|yreflect|reflects the graph across the y-axis.|
|xstretch|horizontally stretches the graph by the reciprocal of a factor given by the user.|
|ystretch|vertically stretches the graph by a factor given by the user.|
|xcompress|horizontally compresses the graph by the reciprocal a factor given by the user.|
|ycompress|vertically compresses the graph by a factor given by the user.|

## Class Diagram
![alt text](classDiagram.png)

## Design Explanation
### Why did you choose this class?
I chose this class because of how it applies to STEM, specifically in the field of mathematics, and the diversity of functions in contrast with their seemingly simple properties.

### Which property is the most important? Why?
Its degree is the most important as it dictates both the graph's end behavior and stretch/compression.

### Which method is the most useful? Why?
Each and every one method is equally useful as they all serve as different forms of transformations of a function's graph.