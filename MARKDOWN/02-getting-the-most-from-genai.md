# How To Get The Most From GenAI

* Because models "hallucinate" it's critical to approach their outputs with reasonable skepticism.
* Because models train on truly massive datasets, they "know" a LOT of things.
    * But, that also means that domain knowledge is incredibly useful in getting AI's to generate quality outputs.
* Because the models are not "intuitive" you should specify clearly what results you want.
    * Most Generative AI systems are "pedantic" and will give you *exactly* what you ask for, not more, not less.
    * Sometimes giving them more flexibility can be interesting, but usually it doesn't give you what you want.
* Prompting for things that are likely in the training data generally yields better results.

## Lets Look At Some Examples

Consider the following progression of prompts and results made using DALL-E 2 and 3:

> A corgi

![](assets/corgie1.png)

> a corgi with high depth of field

![](assets/corgi2.png)

> a corgi with high depth of field and Rembrandt short lighting

![](assets/corgi3.png)

> a full body shot of a happy corgi in a field of flowers with Rembrandt short lighting

![](assets/corgi4.png)

> a full body shot of a happy corgi in a field of flowers with Rembrandt short lighting and high depth of field

![](assets/corgi5.png)

## Generators are great at imitating styles

* Note that there are a large number of ongoing lawsuits related to GenAI and copyright. Be judicious when copying styles.

> A stylish woman in the style of a renaissance painting

![](assets/renaissanceWoman.png)

> A stylish woman in the style of Picasso

![](assets/picassoWoman.png)

> A stylish woman in the style of a Pixar movie

![](assets/StylishPixar.webp)

# The same is true of written material

ChatGPT:

Prompt: Write a short story, 300 words or less, about a man who won the lottery

<blockquote>
In a small, unremarkable town, Thomas lived a life of routine as a grocery store clerk. His existence was a series of predictable days until a whimsical purchase changed everything. Thomas bought a lottery ticket on a day when his dreams felt particularly out of reach, tucking it away in his wallet as a tiny beacon of hope.

Weeks passed, and the lottery draw slipped by unnoticed. It wasn't until a mundane apartment cleanup that Thomas rediscovered the ticket and, on a whim, checked the numbers. To his utter disbelief, he had won. The realization was a slow dawn, transforming his world from monochrome to technicolor. Thomas's win turned him into a local celebrity overnight, but the money didn't change who he was at his core.

Choosing wisdom over extravagance, Thomas donated to local charities, explored the world, and, most importantly, opened a small bookstore. This became a cherished community spot, a tangible reflection of his lifelong passion.

Years later, Thomas's life was rich with experiences, far removed from the predictability of his former existence. He found happiness not in the wealth itself but in the opportunities it brought to live authentically and give generously.

Thomas's story is a reminder that life's most profound changes often come from the most unexpected places. Winning the lottery didn't just alter his life; it allowed him to impact others positively, proving true wealth lies in giving and living fully.
</blockquote>

Prompt: Rewrite the story in the style of an Axios article

<blockquote>
**Title: Small Town Clerk Turns Lottery Win into Community Haven**

**Why it matters:** In an unexpected twist of fate, a grocery store clerk from a nondescript town turned a lottery win into a life-changing opportunity not just for himself, but for his entire community, proving that true wealth lies in the impact one has on others.

**The big picture:** Thomas, a man whose life was defined by routine, found his world turned upside down when he discovered a forgotten lottery ticket in his apartment. The ticket, bought on a whim, ended up being worth millions, catapulting him from obscurity to local fame overnight.

**By the numbers:**

* **1 lottery ticket:** The catalyst that transformed Thomas's life.
* **Millions in winnings:** Though the exact sum remains undisclosed, Thomas's win was substantial enough to reshape his future.
* **1 small bookstore:** The dream Thomas turned into reality, using his winnings to open a community space that quickly became a local treasure.

**Between the lines:** Unlike many lottery winners who succumb to the temptations of sudden wealth, Thomas approached his windfall with a sense of responsibility and purpose. He recognized the opportunity to make a lasting difference in his town.

**What they're saying:** "The money didn't change who I was. It simply allowed me to do more for the people around me," Thomas shared. His sentiment reflects a deeper understanding of value and happiness, rooted in community and personal passion rather than material wealth.

**The impact:** Thomas's story is more than just a feel-good tale of luck and generosity. It's a reminder of the transformative power of giving back and pursuing one's passions. His bookstore has become a hub for connection and learning in the town, embodying the idea that the greatest impact comes from sharing one's fortune.

**The bottom line:** In a world where wealth often equates to personal gain, Thomas's journey underscores the profound satisfaction and joy found in using resources to enrich the lives of others. His legacy is a testament to the idea that the richest individuals are those who contribute to the fabric of their communities.
</blockquote>

Prompt: Rewrite the story as a story for kindergartners

<blockquote>
Once upon a time, in a cozy little town, there lived a man named Thomas. Thomas worked at a grocery store, helping people find their favorite snacks and fruits. Every day seemed the same for Thomas, like flipping the pages of a book with no pictures. But Thomas had a secret wish—he dreamed of adventures and a splash of color in his days.

One sunny day, Thomas decided to buy a magical ticket. This wasn't just any ticket; it was a special lottery ticket that could make wishes come true. He tucked the ticket into his wallet, like a tiny treasure, and almost forgot about it as the days danced by.

Then, one day, while cleaning his small apartment, Thomas found the magical ticket again. With a fluttery heart, he checked the numbers and—surprise!—his ticket was the winner! Thomas's eyes sparkled like stars; his dream was about to come true.

With his newfound treasure, Thomas didn't buy a castle or a mountain of toys. Instead, he thought of his friends and neighbors in the town. "What can make everyone happy?" he wondered.

Thomas had an idea brighter than the sunniest day. He used his treasure to open a magical place—a bookstore! But this was no ordinary bookstore. It was a place where every book was an adventure, waiting to whisk you away to lands of dragons, talking animals, and secret gardens.

The children of the town loved Thomas's bookstore. It became their favorite place to explore, dream, and discover new stories. Thomas didn't just keep his treasure; he shared it, making his town a happier, more magical place.

And Thomas? He found that the greatest joy didn't come from what he bought, but from the smiles and laughter of his friends enjoying the stories. He realized that sharing your treasure makes your heart fuller and your days brighter.

So, Thomas and the children of the town lived happily ever after, with their hearts and shelves full of stories, proving that the best adventures come from sharing your dreams with others.
</blockquote>

# Some Tips

### Remember to be skeptical!!
* Evaluate the outputs.
* Be especially wary of using GenAI in domains where you are not well versed.
* Check for common forms of social bias.

### Be detailed in your prompts.

* Set explicit limits.
    * 500 words or less
    * Aspect ratios
    * 6th grade reading level
    * ...
* Ask for specific formatting
    * HTML
    * Bullet Lists
    * MLA Style Citations
    * ...
* Ask for specific styles
* Consider defining things like race, gender, ethnicity explicitly to avoid GenAI's inherent social biases.
* Long prompts work well, don't be afraid of using them.
* Utilize domain knowledge: 
    * GenAI's often know esoteric jargon.
    * They respond well to domain specific prompting.

### Be iterative.

* Many models allow you to generate variations, or ask for modifications.
* Working in steps can be easier than defining everything in one prompt.
* Sometimes small changes to a prompt can result in large changes in output.
* Don't be afraid to do some things manually. 
    * If you're a talented photoshop user, let AI start and add your own final touches. 
    * Let ChatGPT produce a rough draft or an outline, and you write the rest.

### Give the model samples first.

* e.g. upload samples of your own writing or your companies style and ask it to imitate that style.
    * Sample prompt: Analyze the text below for style, voice, and tone. Then write a new paragraph in 800 words in the same style, voice, and tone on Topic -[Topic]. [Paragraph]

### Use "system" Prompts

* ChatGPT: use "system:" to make a system prompt, which tells the machine to use that for the whole conversation
    * System: Write like an axios article
    * System: Take the opposite view of claims I make, as if this were a debate
    * System: Write using language that is accessible at a 6th grade reading level

* Other systems have similar capabilities, try to find documentation for the systems you use.

### Find Out What Works For Others!

* We're all learning more about how to better use these tools every day.
* Find other people who are using GenAI and ask them what works
    * Or look online for similar resources.

## Some Tasks that GenAI can help with

* Ask for edits or proofreading on your writing. 
* Ask it to find bugs in code, or write tests for a function
* Ask for a summary of input text.
* Generating custom images for articles, presentations, etc. 
* Generating slides for a slideshow


