# Design-Patterns

### <a href="#memento">1-Memento Pattern </a>

### <a href="#state">2-State Pattern </a>

# <a id="memento">Memento Pattern</a>

<img src="files/memnto.png">

The main purpose of this model is to implement the undo mechanism like in editors and ...
for doing this purpose we have 3 class one is editor that is our main class you can assume it as a real editor
that can we write content on it.
another class is editor state that modeling editor attributes and the other one is history class that is responsible for saving and keeping editor diffrent state

## note
you may ask a quesion why we dont implement all these on editor class the answer is simple because of single responsibility in SOLID priciple, that says a class only should have one and only one reason to change

# <a id="state">State Pattern</a>

<img src="files/state.png">

this design pattern is use when we have an entity that constatntly changes to diffrerent states like a paint application which we can change our selection tool to brush , selection, rectangle , circle , ....

we can implemnt this by using << if statements >> and get the state value from input and check what state our client need and get some action base on that state we got.

this is simple solution but what if we want to add more and more state during our app development?
we should constantly change our class and add more if else statement. this violate open close principle that say a class should open for execution and close to modification.

## solution
we can get some hand from state pattern in here base on the digram.
we have multiple class, first one is canvas, another is Tool that have two abstract methods and the brush and selection class that inherit from Tool class
as you can see we create canvas instance and set the tool to Selection instance and call the mouseDown and mouseUp event

## note
you can add as many tools by this pattern by adding a new class

##practice
think what is other scenarios exist that we should use state pattern.
also try to add another paint tool to this pattern

# <a id="state">Iterator Pattern</a>

<img src="files/iterator.png">

iterator pattern used when we want to store some value as history or any thing else But it is possible to change our data structure to store the desired data in the future.

for example in iterator.py what we do is saving and controling browsing history in a list but it is possible that we change it to tuple or dictinary or it is possible that we want a fixed array

here the problem is when we want to write this code in normal way, in future if we want to change our desired data structure to something else it is hard to do refactoring in our code, because we should chanage all consumers that use BorwsHistory class 

so what we do is to create an iterator class that is responsible for iterating the used data structure and all consumers instead of using data structor operators using Iterator class to get access to data, in future if we want to change our data structure only we should apply some change to iterator and history class 

in example code, we have three class one is Iterator that is abstrac and we used it only as an interface, the other one is BrowsHistory class that responsible for pushing and poping data and keeping our desired data structure, another one is ListIterator inner class that inherit from Iterator class 

when consumers want to add or delete some data they use push & pop mehtod and when they want to iterate over history they call create_itrator class and get a itrable instance from desired data structure and they can itrate throw data by calling next & prev & current & has_next method 

## note
in future if we change our datastructure to Array we only need some changing in BrowsHistory and ListItrator class 

