# Handwritten Text to Audio for Visually Impaired

Its hard for visually impaired people to attend their online classes specially if the teacher is writing notes on the whiteboard. So, to ease up the process, this handwritten translator converts to typed text using Tensorflow and Deep learning. And, the converted text is then translated to audio using inbuilt JavaScript properties.

## Set up on your local system

Make sure you have `pipenv` installed in your system. If not then download using,

``` bash
sudo pip install pipenv
```
Follow the steps to setup the project
1. Change into the directory

2. Activate the virtual environment
``` bash
pipenv shell
```
3. To install the requirements of the project, run 

``` bash
pipenv install
```
This can take some time.

## Run the web application locally
The pretrained model was too huge to be uploded on GitHub, so in order to make this application work, download it from [here](https://drive.google.com/file/d/1KqbIoF-48YAJXQuMNKe8LQ2plZJ6taIR/view?usp=sharing). Place this model in he `/model` directory. 

To run and test the application, run the command after all the installation is completed succesfully

``` bash
python3 src/upload.py
```
It will run the application on http://localhost:5000/

## Screenshot
![Screenshot](https://user-images.githubusercontent.com/33135343/93141262-81077900-f701-11ea-9976-341204af1ba7.png)

## Use Cases
1. Visually impaired people can use computers without any hesitation.
2. Inclusion of this community in normal schools.
