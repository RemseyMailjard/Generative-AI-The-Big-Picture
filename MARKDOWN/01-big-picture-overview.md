# Big Picture AI and ML Concepts

In this section we are attempting to layout the scope of the field of AI, and in so doing foreshadow the rest of the class.

## Do you use Generative AI for anything?

* You should get some answers. If not, share some stuff YOU use it for. 

## What have you heard AI is being used for?

* Now you'll surely get a lot of answers...

* Common, good, pro-social uses:
    * Solving “The blank page problem”
    * Illustration & Image creation
    * Editing support (code & text)

* Common not-so-good uses:
    * Deepfake porn
    * Scams
    * Crappy website SEO bait

## Narrow vs Broad AI & General AI 

* "Artificial General Intelligence" is what most sci-fi movies portray: A machine that "thinks" in very much the same way we imagine humans and many other animals thinking.
    * Such machines take in all kinds of input (like animals) and can perform reasoning based on those inputs in a wide variety of contexts.

* State of the Art generative systems arguably contain some aspects of general intelligence.
    * Debate among experts about how close we are to general AI is quite fierce. 
    * Most ML systems are still "narrow" though.
    * These can achieve superhuman results, but only in quite limited domains.
    * AlphaGo can play Go, but it cannot answer even the most basic math questions.
    * Image generators often struggle with text inside of images
    * Self driving cars can't ride a bike...

## Generality Through Composition?

* Self-driving cars are a series of specialized ML systems combined
    * "navigation" and "driving" components are separate.
    * Driving itself is several sub-components:
        * A CNN system for object localization
        * A separate system to process LIDAR input
        * A Reinforcement Learning agent to process the outputs of these other AI's and make decisions to turn the wheel or accelerate/decelerate...
        * Explicitly NOT one unified system making decisions. Many smaller systems added together.

## Generality Through Scale?

* Models have become increasingly large, which has definitely increased their power and usefulness.
* Some researchers fundamentally believe that "scale is all you need" to create a general purpose AI.
* In many ways, it's fair to argue that state of the art text generators are already "generally" intelligent:
    * Although all they do is produce text, that text is applicable to a wide array of topics.
    * Programming is text production.
    * Screenwriting is text production.
    * Translation is text production.
    * **A massive portion of many skills can be demonstrated by writing about those skills, if GenAI can write about those skills, does it effectively have them?**

# So How Do These Things Work?

## ML vs Non-ML systems

* Machine learning systems are a form of AI that involve automatically finding patterns in large datasets
* Many AI systems don't work this way. For example:
    * Google Maps uses an explicit model of the world and graph search to find the shortest path between two places.
        * Although ML is now used to predict traffic.
    * Deep Blue (the chess AI) was an "expert system" that just did tree search and used hand crafted algorithms to determine the value of each move.
    * (there are many others, feel free to share your favorite)

* ML is becoming especially popular for a few reasons:
    1. Hardware is much faster now than ever before, and ML works best with access to lots of computational power.
    2. The internet age has resulted in a wide variety of incredibly large datasets.
    3. Some types of patterns are extremely hard to define explicitly, and ML systems have become adept at finding some such patterns. 
        * Computer vision and weather prediction are two prime examples.
        * Image and text generation are modeled as similarly complex patterns.

## Four Types of ML

* Supervised Learning
    * By far the most popular.
    * Involves learning from "labeled" data, meaning the answer to our question is known (we know which pictures are cats and which are not).
    * Widely used in a huge number of domains.

* Unsupervised Learning
    * Less popular in general.
    * Involves unlabeled data.
    * Often used as a way to "bootstrap" labeled data for supervised learning.
    * Clustering is the most common example.
    * We do not talk much about unsupervised learning in this class.

* Semi-supervised learning combines some supervised and some unsupervised tactics.
    * The most common example is using a supervised learning agent to classify datasets, then using those AI-classified datasets to further train the model.
    * In generative AI "actor/critic" models like GANs are semi-supervised.

* Reinforcement Learning
    * Used in situations where an agent needs to keep making decisions.
    * Most popular in game playing and robotics, but has been used in some other domains.
    * Involves an "agent" and an "environment" where the agent "reads" the environment, takes an "action" and then "reads" the environment again to make it's next decision.

* Generative Models frequently combine multiple of these tactics.
    * ChatGPT and other chatbots use aspects of reinforcement learning to "track" a conversation over time. 
    * Chatbots and image generators look at huge amounts of text and images respectively.
    * Diffusion models and GANs have an aspect of semi-supervision baked into actor/critic model

## Intuition on How Training Works for Generative Models

* Text generators are typically "Transformer" based models. These train by taking in a set of words, predicting the next word or set of words, and being punished/rewarded for how correct they are.
    * ChatGPT (and others) then use human evaluators to rank outputs from the model given the same prompt.

* Most SOTA image generators use a "diffusion" model. These train by
    * Taking an image.
    * Iteratively adding small amounts of random noise to the image
    * Asking the model to generate a "denoised" version of the image
    * Rewarding the model when it successfully produces the previous step, punishing it when it does not.

## This Results in Black Box Models

* A key thing to understand about ML is that the models are "black boxes"
* We can reliably produce them, and we can know why the training process works
* But we **don't** know how or why a model makes it's individual decisions -- introspecting on the model is incredibly difficult. 

## Sources of Bias & Error

* The biggest source of bias is the data itself.
    * The three examples in the next exercise will elucidate this point in great detail!
    * But in short, ML models only learn whatever patterns are in the data itself. If that data was collected by humans, it likely has human bias embedded inside of it. ML models will learn that bias. 

* Bias can also be introduced by evaluators who might:
    * Not carefully look at the results across different demographic cross tabs
    * Explicitly have their own motives (e.g. Chinese government training an algorithm to target Uighurs)
    * ...

* Errors can also be created by using an algorithm that can't adequately capture the relationship between the input data and the output data.
    * Many of these algorithms have some very explicit modeling expectations...
        * Linear regression expects a linear relationship.
        * K-Nearest Neighbors expects a geometric distance-based relationship.
        * ...

* All of these can, of course, happen at once.

## The Problem of Big Data

* Modern ML systems need huge amounts of data.
* But, in order to work well, they need that data to be of high quality.
* There is obvious tension between these two goals of having TONS of data and having it be high quality.
* In reality, most ML firms are just scraping data from the internet (some more haphazardly than others).
* This scraping results in TONS of societal biases being reflected in the training data
    * e.g. people on the internet are sometimes racist/sexist/etc.