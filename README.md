<div align="center">
<h1>Bridge</h1>

[![GitHub issues](https://img.shields.io/github/issues/shreyagupta30/Bridge?logo=github)](https://github.com/shreyagupta30/Bridge/issues)
![Size](https://github-size-badge.herokuapp.com/shreyagupta30/Bridge.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/torch)

[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/shreyagupta30/Bridge/blob/master/.pre-commit-config.yaml)
![GitHub](https://img.shields.io/github/license/shreyagupta30/Bridge)
![Travis (.org)](https://img.shields.io/travis/shreyagupta30/Bridge)
</div>

<strong> The current time is full of hardship which is taking a toll on everyone's lives.  As a student myself, these time have clearly shown how for granted we take our education system and daily learnings. It is still very convenient for normal people like us. But we hardly think how difficult it would have been for specially-abled people to adapt to this way of living. It can be very intimidating for these people to cope up with this virtual world and most importantly for students that no longer can go to their normal schools and learn in the way there are used to. In order to make it a little less tiresome and more fluent I come up with **Bridge**. Here I am trying to build a complete system that will help them in some way to make this shift easy.

***Bridge*** is an all in one application which aims towards 

- Visually Impaired people
- Speech/Hearing Impaired people

Bridge's ulitmate aim is to make technology, web surfing, work from home and education in the times of social distancing easier for specially-abled people, and thus enabling them to **brace the world of Covid-19.**
</strong>

## Overview and features

This application is an all in one application for all 3 of the mentioned disablities. It has two major modes -

1. ***Visual Impaired Mode*** - This mode is for the people who have lost their vision capabilities and have audio/speech abilities. 
2. ***Sound / Voice Impaired Mode*** - This mode is for the people who have lost the ability to listen or speak or both, and have retained their sight ability.

## Structure of the repository
This repository is divided in 4 sub directories
 1. [ASL](https://github.com/shreyagupta30/Bridge/tree/master/ASL)
 2. [HandwrittenText2Audio](https://github.com/shreyagupta30/Bridge/tree/master/HandwrittenText2Audio)
 4. [Speech2Text](https://github.com/shreyagupta30/Bridge/tree/master/Speech2Text)
 3. [Voice_automation](https://github.com/shreyagupta30/Bridge/tree/master/Voice_automation)

 `ASL` and `Speech2Text` is under **Visual Impaired Mode** of the Application whereas `HandwrittenText2Audio` and `Voice_automatio` is under **Sound/Voice Impaired Mode**.

## Installation and Setup

### Prerequisites
- pipenv should be installed in the system. It can be done using `sudo pip3 install pipenv`.
- Change the version of the python in `Pipfile` according to the python version available in your system

### Setup and running of project

- Fork the repo and clone it.
- Navigate to the cloned repository
- Then run `pipenv shell` to activate the environment of all the features you want test.

*Note: Installation guide of all the applications is in their respective README.*
  
## Demo

Demo of the project can be seen [here](https://drive.google.com/file/d/1UTvfl9ob75-Qc54s41XVQ3Gg-rszm9yN/view?usp=sharing)


## Contribution to the project

<div align="center">

[![GitHub issues](https://img.shields.io/github/issues/shreyagupta30/Bridge?logo=github)](https://github.com/shreyagupta30/Bridge/issues) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/shreyagupta30/Bridge?logo=git&logoColor=white)

</div>

### Git workflow

Please follow a systematic Git Workflow -

- Create a fork of this repo.
- Clone your fork of your repo on your pc.
- [Add Upstream to your clone](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
- **Every change** that you do, it has to be on a branch. Commits on master would directly be closed.
- Make sure that before you create a new branch for new changes,[syncing with upstream](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) is neccesary.

### Commits

- Write clear meaningful git commit messages (Do read [this](http://chris.beams.io/posts/git-commit/)).
- Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check [this](https://github.com/blog/1506-closing-issues-via-pull-requests) for more info)
- When you make very very minor changes to a PR of yours (like for example fixing a failing Travis build or some small style corrections or minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at [here](https://davidwalsh.name/squash-commits-git))
- When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.

## Future Enhancements
- [ ] Package all the features together in an Chrome/Firefox extension
- [ ] Create an electron based Desktop app to make it easy to use over desktop apps
- [ ] Create a GCP/AWS/Azure Deployment

## Thank you!
If you find this project useful, please leave a star on this repo!
