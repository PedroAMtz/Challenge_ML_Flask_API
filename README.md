## Challenge Machine Learning Flask REST API :rocket:

:star: **Challenge objective:** Create a REST API that could recive input sentences in spanish and return the named entities in each sentence. 

**API characteristics:** 

* Spacy and Flaskas as core modules for development.
* Implementation of NLP tools provided by Spacy in order to solve the proposed challenge.
* Simple implementation _(less than 60 lines of code)_ :wink:


**¿How to use the API?** 

* **Step 1:** Clone this repository into yout local machine -> (requirements: Python adn git installed)
* **Step 2:** Select a virtual environment, activate it and run pip install -r requirements.txt (or you can install the dependencies locally)
* **Step 3:** Run the following command _python app.py_ from the terminal (make sure to be in the directory where the github was cloned) aditionally it would be easier by installing insomnia, which a software develepment tool to test the application. Inside the insomnia project click on the adding button and select HTTP Request.
* **Step 4:** Once the HTTP Request is selected you would be able to test the GET and POST methods, which are the main methods of the application (desired method -> POST).
* **Step 5:** Select POST method and copy the localhost endpoint provided (example: http://127.0.0.1:5000) by running the app.py from step 3.
* **Step 6:** Now you can enter the input in JSON format following the example provided: _{
 "oraciones": [
 "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
 "San Francisco considera prohibir los robots de entrega en la acera."
 ]
}_
* **Step 7:** Finally click on the Send button and the desired output will be displayed!! :smile:

### Insomnia GUI example:

!['Imagen de la competencia'](/insomnia.png)

**Additional resources**

* Dockerfile created -> (from terminal run _docker image build -t challenge-ml-api ._) this will allow to at least create a Docker image from the application :whale:
* requirements.txt




