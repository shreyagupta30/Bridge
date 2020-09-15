# Sign Language to Text for Hearing Impaired

Hand gestures conversion in 3D space using a single low resolution camera for converting American Sign Language into any spoken language for other person to understand

## Set up on your local system

Make sure you have `pipenv` installed in your system. If not then download using,

```bash
sudo pip install pipenv
```

Follow the steps to setup the project

1. Change into the directory

2. Activate the virtual environment

```bash
pipenv shell
```

3. To install the requirements of the project, run

```bash
pipenv install
```

This can take some time.

## Run the web application locally

To run and test the application, run the command after all the installation is completed succesfully

```
python app.py -i 0.0.0.0 -o 8080
```

It will run the application on http://localhost:8080/

## Screenshots

### Q

![Q](https://user-images.githubusercontent.com/33135343/93141668-3a664e80-f702-11ea-9f48-cfced771335d.png)

### H

![H](https://user-images.githubusercontent.com/33135343/93141670-3afee500-f702-11ea-95c5-11f57b02e75b.png)

## Dataset used

Sign Language MNIST (https://www.kaggle.com/datamunge/sign-language-mnist)
Each training and test case represents a label (0-25) as a one-to-one map for each alphabetic letter A-Z (and no cases for 9=J or 25=Z because of gesture motions).

## Use Cases

1. Hearing impaired people can have a common classroom by asking their questions/doubts without any hesitation.
2. Inclusion of this community in normal schools and well as conventional online classrooms.