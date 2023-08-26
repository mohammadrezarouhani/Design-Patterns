# Design-Patterns

<a href="#memento">1-Memento Pattern </a>
<img src="files/memnto.png">

##
The main purpose of this model is to implement the undo mechanism like in editors and ...
for doing this purpose we have 3 class one is editor that is our main class you can assume it as a real editor 
that can we write content on it.
another class is editor state that modeling editor attributes and the other one is history class that is responsible for saving and keppping editor diffrent state

##note
you may ask a quesion why we dont implement all these on editor class the answer is simple because of single responsibility in SOLID priciple, that say a class only hould have one and only one reason to change 



