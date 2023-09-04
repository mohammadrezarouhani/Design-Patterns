# Design-Patterns

### <a href="#memento">1-Memento Pattern </a>

### <a href="#state">2-State Pattern </a>

# <a id="memento">Memento Pattern</a>

<img src="files/memnto.png">

The main purpose of this model is to implement the undo mechanism like in editors and ...
for doing this purpose we have 3 class one is editor that is our main class you can assume it as a real editor
that can we write content on it.
another class is editor state that modeling editor attributes and the other one is history class that is responsible for saving and keeping editor diffrent state

##note
you may ask a quesion why we dont implement all these on editor class the answer is simple because of single responsibility in SOLID priciple, that says a class only should have one and only one reason to change

# <a id="state">State Pattern</a>

<img src="files/state.png">

this design pattern is use when we have an entity that constatntly changes to diffrerent states like a paint application whtch we can change our selection tool to brush , selection, rectangle , circle , ....

we can implemnt this by using << if statements >> and get the state value from input and check what state our client need and get some action base on that state we got.

this is simple solution but what if we want to add more and more state during our app development?
we should constantly change our class and add more if else statement. this violate open close principle that say a class should open for execution and close to modification.

##solution
we can get some hand from state pattern in here base on the digram.
we have multiple class one, is canvas, another is Tool that have two abstrac methods and the bruhs and selection class that inherit from Tool class
as you can see we get canvas Instances and set the tool to Selection and call the mouseDown and mouseUp event

##note
you can add as many tools by this pattern by adding a new class

##practice
you can think what is other scenarios exist that we should use state pattern on them.
also try to add another paint tool to this pattern