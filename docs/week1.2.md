# Week 2: Static code analysis

In this exercise we are going to look at the code delivered by a student. [Download the code-basae using this link](files/exercise1.zip). Because of reasons of privacy and NDA's, we have changed the code somewhat, so if you see any strange stuff that's probably because of that. 

Static code analysis is meant to be done without running or even compiling the code. It can be done using techniques as `fgrep`, but also just by glancing over the code, opening files and see how they interact with each other. Different, very professional techniques exist for these kinds of jobs, but for this small code base doing stuff by hand will suffice.

In this session, we will divide the group in five different sub-groups. Each group will work on the following assignments for about an hour and a half. After that, each sub-group will present one of the exercises in a small pitch: no PowerPoint or other presentation is required, just talk us through your findings.

## Exercise 1: The factory

The application can parse the report in two different formats as a pdf file or as a text file. In the future, it could be possible that the hospitals share the information in another file format than the two that are currently implemented. To extend the functionality in the feature, a parent class `HsmrParser` was created which must be extended in the implementations of the specific parsers. 

At the moment, two different parsers are realised, but more can be added in the future. A factory was created to get an instance of the parser based on the parser types which are defined as constants in the file `parserTypes.py` file.

- What is a factory? 

- Does the implementation of the factory method follow the *Interface Segregation Principle*?


## Exercise 2: Single reponsibility

The application uses the CCS classification to extract the information from the HSMR reports. The application uses a CSV file with the ccs index and the corresponding Dutch description. This information is provided by the [CBS](https://www.cbs.nl/nl-nl/onze-diensten/methoden/onderzoeksomschrijvingen/aanvullende%20onderzoeksbeschrijvingen/hsmr-2016-methodological-report) as a Microsoft Office Excel file. The necessary data was extracted and saved as a CSV file.

Review the python files starting with Ccs. Are those files adhering to the single-responsibility principle: "Every class should have only one responsibility”?


## Exercise 3: The base classes

In the code, several base classes are used. Can you find examples of the [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle): "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it." Explain your answer.


## Exercise 4. The local settings object

A settings file was used inside the application to store the settings which can be changed over time or are user-specific. For instance, the path to a temp directory is saved inside the settings file because they will be different between users. Also, specific table names of the HSMR report, API URLs, and API headers are saved in this file because they can change and must be easily assessable. 

The Settings object is implemented as a Singleton object inside the application to prevent multiple instances of the same class. It also prevents multiple unnecessary parsing of the settings file and eventually different settings when the settings are manually changed during runtime of the program. 

-	Search for the Settings class. What makes this class a singleton object and is a singleton object SOLID? 

-	The hospital types codes are stored in a python module `hospital_types.py`. Is this a logical solution?

-	Is there an alternative solution for these kinds of local settings and parameters? Please elaborate.


## Exercise 5. UML Class diagram

Draw the class diagram for this program. 



