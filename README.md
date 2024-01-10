# ** AirBnB project: **

The goal of the project is to deploy a simple copy of the AirBnB website.

This web Application must composed by:
- A command interpreter to manipulate data without a visual interface, like in a
  Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static
  and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your
  data (retrieve, create, delete, update them)

## ** The Interpreter (console): **

The first piece is to manipulate a powerful storage system. This storage engine
will give us an abstraction between “My object” and “How they are stored and
persisted”. The console will be a tool to validate this storage engine.

main tasks:
- create data model
- manage (create, update, destroy, etc) objects via a console / command
  interpreter
- store and persist objectss to a file (JSON file)
