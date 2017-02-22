# The responses.py file. Each response is a multiline string that
# corresponds to the keyword, except helptext because "help" is a
# reserved word in Python and the nutrition response, because we
# have two responses depending on whether it's called from inside or
# outside the /r/vegan sub


# Update this list when new trigger responses are created

triggerWords = set(["eggs", "canines", "ethics", "honey", "nutrition", "protein", "b12", "bj", "lions", "breakfast", "dinner", "swallow", "snacks", "help", "girlfriend", "boyfriend", "america", "usa", "england", "ireland", "scotland", "wales", "eire", "britain", "uk","france", "germany", "netherlands", "holland", "china", "canada", "spain", "australia", "bible", "labmeat", "maycontain", "joke", "soy", "sweden", "peta", "foodchain", "cheese", "dublin", "london", "charleston", "jackson", "eskimos", "inuit", "ni", "irc", "chat", "discord", "reading", "beginner", "beginners", "newbie", "nukes" ])

jokeNumber = 5

# Moved here because it's easier to maintain in one file, rather than altering Gary's code each time.

comment_footer_template = """



^^Bloop ^^Bleep! ^^I'm ^^Gary ^^the ^^/r/vegan ^^helper ^^bot. ^^Comments ^^and ^^suggestions ^^to ^^/u/pizza_phoenix. [^^General ^^information ^^and ^^latest ^^keywords ^^here.](http://www.mattrudge.net/gary) ^^Latest ^^keyword ^^update ^^22nd ^^February ^^2017.

"""


# ---------- Keywords ---------- 

helptext = """

I'm Gary - the /r/vegan helper bot. I was written to make it easier to respond to some common questions about veganism.

You can call me from within the /r/vegan sub by replying to any comment with:

@Gary! query

Where "query" is any of the following keywords:

* beginner (or beginner or newbie)
* boyfriend (or girlfriend)
* B12
* canines
* chat (or discord or irc)
* cheese
* eggs
* ethics
* foodchain
* god
* honey
* inuit (or eskimos)
* joke
* labmeat
* lions
* maycontain
* nukes (will not work in r/vegan)
* peta
* nutrition
* reading
* protein
* soy
* swallow (or bj - yes, the age old question)

You can also ask about any of the following countries, and I'll give you videos showing how animals are treated there:

* america (or usa)
* australia
* britain (or england, scotland, wales, uk)
* canada
* china
* france
* germany
* netherlands (or holland)
* spain
* sweden

Or ask for a meal idea, and I'll search some hand-picked vegan recipe sites to give you some ideas. So, try asking me about breakfast, dinner or snacks.

By default, I reply to you, and tag the OP so that they get alerted to the comment. You can override this behaviour by using the "-above" option, which will force Gary to reply directly to the OP. So:

@Gary! Eggs -above

will send reply to the OP instead of to you. To receive your answer as a PM, use the "-pm" option.

Also, if you're in a vegan debate on another subreddit and need a bit of backup, then you can call me by my username:

/u/gary_bot query

You can use the same keywords as above.

If you think I should respond to more keywords, then send a DM to /u/pizza_phoenix.


%s

"""

eggs = """

* The commercial egg industry is responsible for the deaths of millions of male chicks per year. Only the female ones are kept to produce eggs. [See this movie for more information](http://www.fowlplaymovie.com) or [read the YVFI article describing the conditions on egg farms.](http://yourveganfallacyis.com/en/eggs-are-not-unethical)
* Even backyard hens lay far more eggs than is healthy for them. Taking the egg signals their body to create another. If you leave their eggs with them, they'll eat the egg themselves to restore some of the resources they lost creating it in the first place and their laying rate will slow down to healthy levels! [More information here.](http://bitesizevegan.com/ethics-and-morality/can-vegans-eat-eggs-from-backyard-chickens-veggans/)
* Finally, even if you can argue that it is somehow ethical to steal what the chicken has produced, we don't need to to eat eggs to live or have a balanced diet. In fact, a [2009 Harvard study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2628696/pdf/295.pdf) demonstrated that consuming eggs increased the risk of getting type 2 diabetes. For those with diabetes, [egg consumption doubles the risk of death](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2386667/pdf/nihms44834.pdf), and even [a single egg per day](http://nutritionfacts.org/2011/08/31/bad-egg/) increases the risk of heart failure.


%s

"""

honey = """

* The philosophy of veganism is to do no *conscious* harm to any living thing. Commercial honey production is a long way from the image of a few hives in someone's back garden. All honey production harms the bees, which have been proven to have a complex nervous system. [See this link for more.](http://healthyeating.sfgate.com/wont-vegans-eat-honey-2938.html)
* Bees produce honey as their own food. In its lifetime, a honeybee may only produce about a teaspoon of honey. In the US, more than 400 million pounds of honey is consumed each year. [Here is more information](http://www.godfist.com/vegansidekick/guide.php#a7) and [here too.](http://yourveganfallacyis.com/en/honey-is-not-unethical)
* As with eggs, there is no dietary need for a human to eat honey. Doing so harms the creatures that produce it.


%s

"""

protein = """

* [This is probably the one question that vegans get asked most often!](http://imgur.com/ydJaoGw)
* Contrary to popular belief, it is not difficult to get sufficient protein on a vegan diet. Look at some of the world's largest mammals - no one wonders where their protein comes from! There is no trend of protein deficiency in the vegan community, but [there is a trend of unhealthy protein surplus in the non-vegan community.](http://www.huffingtonpost.ca/2012/08/13/too-much-protein-diets-_n_1772987.html) You could eat ~2000 cal of iceburg lettuce and get 145g protein in a day.
* "Protein combining" as a meal requirement is a [myth](http://nutritionfacts.org/video/the-protein-combining-myth/) and has been [debunked by one of its previous supporters.](https://en.wikipedia.org/wiki/Protein_combining#Criticism)
* If you eat a balanced vegan diet, you will have more than enough protein. Top protein sources for vegans include: beans, lentils, chickpeas, soya foods (tofu, tempeh, soy milk), cashew nuts, almonds, peanuts, pumpkin seeds, wheat, oats, buckwheat, quinoa, seitan and pasta. [Source 1](https://www.vegansociety.com/resources/nutrition-and-health/vitamins-minerals-and-nutrients/protein), [Source 2](http://www.vrg.org/nutrition/protein.php)


%s

"""

lions = """

Ah yes, the King of the jungle. Do you really want to model your behaviour on a lion or (insert random carnivorous predator here)? Really really? 

[I'm a lion!](http://imgur.com/xdCFSxJ)

[Totally a lion.](http://imgur.com/US4dY2F)

[You're not really a lion though, are you?](http://yourveganfallacyis.com/en/animals-eat-animals/resources)


%s

"""

b12 = """

* It's true that vitamin B12 is not made by plants, but it's not made by animals either! In fact, it's the byproduct of bacterial fermentation. The Institute of Medicine recommends that all adults over the age of 50 supplement B12, whether vegan or not.
* The subject about B12 is complicated, but it's not true that you can only get it from eating animals. Many plant-based foods are fortified with B12, and there are natural sources too.
* These links might be of interest: [Dr. Thomas Campbell's discussion on B12](http://nutritionstudies.org/12-questions-answered-regarding-vitamin-b12/), [Vegan Health & Fitness article](http://www.veganhealthandfitnessmag.com/b-12/) and [YVFI article on B12](http://yourveganfallacyis.com/en/vegans-cannot-get-enough-b12)


%s

"""

canines = """

So, humans have canine teeth, so therefore we're meant to eat meat, right? Well...not really. For a start, when was the last time you actually tore meat with your canine teeth? You might use your incisors, but most often the meat is cooked, softened and then passed back to our flat molars (which are great at chewing vegetation) to be ground. In fact, whereas carnivores have a purely up-and-down jaw action (watch your cat eating), humans - as omivores - also have a side-to-side action, perfect for grinding starchy vegetables.

[It's a fallacy that we need to eat meat just because we have canine teeth.](http://yourveganfallacyis.com/en/canines-make-me-a-meat-eater) In fact, [many herbivorous animals have much larger canine teeth than us](http://freefromharm.org/photo-galleries/9-reasons-your-canine-teeth-dont-make-you-a-meat-eater/), but our [canine teeth sure are scary!!](http://imgur.com/Dg6GeWb)


%s

"""

ethics = """

Most people claim to love animals, but while they do love their dogs and cats, they continue to eat chickens, cows and pigs. Why are some animals more deserving of compassion than others? After all, pigs and cows are [proven to be just as intelligent](http://www.huffingtonpost.com/2015/06/15/are-pigs-intelligent_n_7585582.html), loving, and capable of suffering as Fluffy and Fido.

* Ethical vegans oppose the abuse and slaughter of all animals, not just pets.
* Eating animal products supports [cruelty to animals](http://www.rollingstone.com/feature/belly-beast-meat-factory-farms-animal-activists). The animal agriculture industry keeps animals in horrific conditions: hens are commonly kept in tiny cages, dairy cows [have their babies ripped away](http://freefromharm.org/dairyfacts/) from them, [male baby chicks are ground up in "macerators"](http://www.independent.co.uk/life-style/food-and-drink/hatched-discarded-gassed-what-happens-to-male-chicks-in-the-uk-10088509.html), all so we can keep eating eggs, dairy, and meat.

The principle of excluding exploitation and/or cruelty to animals underlines all vegan ethics.


^^Contributed ^^by ^^/u/SummerMournings


%s


"""

nutrition = """

All the major dietetics and health organizations in the world agree that vegan and vegetarian diets are just as healthy as omnivorous diets. This is taken in its entirety from the /r/vegan sidebar information. Here are links to what some of them have to say on the subject:

**[Academy of Nutrition and Dietetics](https://www.ncbi.nlm.nih.gov/pubmed/27886704/)**

* *It is the position of the Academy of Nutrition and Dietetics that appropriately planned vegetarian, including vegan, diets are healthful, nutritionally adequate, and may provide health benefits for the prevention and treatment of certain diseases. These diets are appropriate for all stages of the life cycle, including pregnancy, lactation, infancy, childhood, adolescence, older adulthood, and for athletes.*

**[Dietitians of Canada](http://www.dietitians.ca/Nutrition-Resources-A-Z/Factsheets/Vegetarian/Eating-Guidelines-for-Vegans.aspx)**

* *A well planned vegan diet can meet all of these needs. It is safe and healthy for pregnant and breastfeeding women, babies, children, teens and seniors.*

**[The British National Health Service](http://www.nhs.uk/Livewell/Vegetarianhealth/Pages/Vegandiets.aspx)**

* *With good planning and an understanding of what makes up a healthy, balanced vegan diet, you can get all the nutrients your body needs.*

**[The British Nutrition Foundation](http://www.nutrition.org.uk/publications/briefingpapers/vegetarian-nutrition)**

* *A well-planned, balanced vegetarian or vegan diet can be nutritionally adequate ... Studies of UK vegetarian and vegan children have revealed that their growth and development are within the normal range.*

**[The Dietitians Association of Australia](http://daa.asn.au/for-the-public/smart-eating-for-you/nutrition-a-z/vegan-diets/)**

* *Vegan diets are a type of vegetarian diet, where only plant-based foods are eaten. They differ to other vegetarian diets in that no animal products are usually consumed or used. Despite these restrictions, with good planning it is still possible to obtain all the nutrients required for good health on a vegan diet.*

**[The United States Department of Agriculture](http://www.choosemyplate.gov/tips-vegetarians)**

* *Vegetarian diets (see context) can meet all the recommendations for nutrients. The key is to consume a variety of foods and the right amount of foods to meet your calorie needs. Follow the food group recommendations for your age, sex, and activity level to get the right amount of food and the variety of foods needed for nutrient adequacy. Nutrients that vegetarians may need to focus on include protein, iron, calcium, zinc, and vitamin B12.*

**[The National Health and Medical Research Council](http://www.nhmrc.gov.au/guidelines-publications/n55)**

* *Alternatives to animal foods include nuts, seeds, legumes, beans and tofu. For all Australians, these foods increase dietary variety and can provide a valuable, affordable source of protein and other nutrients found in meats. These foods are also particularly important for those who follow vegetarian or vegan dietary patterns. Australians following a vegetarian diet can still meet nutrient requirements if energy needs are met and the appropriate number and variety of serves from the Five Food Groups are eaten throughout the day. For those eating a vegan diet, supplementation of B12 is recommended.*

**[The Mayo Clinic](http://www.mayoclinic.org/healthy-living/nutrition-and-healthy-eating/in-depth/vegetarian-diet/art-20046446)**

* *A well-planned vegetarian diet (*see context*) can meet the needs of people of all ages, including children, teenagers, and pregnant or breast-feeding women. The key is to be aware of your nutritional needs so that you plan a diet that meets them.*

**[The Heart and Stroke Foundation of Canada](http://www.heartandstroke.com/site/c.ikIQLcMWJtE/b.3484249/k.2F6C/Healthy_living__Vegetarian_diets.htm)**

* *Vegetarian diets (*see context*) can provide all the nutrients you need at any age, as well as some additional health benefits.*

**[Harvard Medical School](http://www.health.harvard.edu/staying-healthy/becoming-a-vegetarian)**

* *Traditionally, research into vegetarianism focused mainly on potential nutritional deficiencies, but in recent years, the pendulum has swung the other way, and studies are confirming the health benefits of meat-free eating. Nowadays, plant-based eating is recognized as not only nutritionally sufficient but also as a way to reduce the risk for many chronic illnesses.*


%s

"""

nutritionrvegan = """

There is a wealth of information showing that vegan diets are nutritious and beneficial to health. Instead of reposting in its entirety here, please [click on this link](https://www.reddit.com/r/vegan/wiki/dieteticorgs) to see what the world's major nutrition and health organisations have to say about a vegan diet.

A vegan diet has to be appropriately planned to ensure that it is balanced, but that is true of all other diets too.


%s

"""

girlfriend = """

I wish I could help you find a vegan partner, but always remember that kindness and compassion for other living creatures are very attractive qualities. Believe in yourself, because I do!

[Here is something that might be of interest to you.](https://docs.google.com/spreadsheets/d/1VFfIw7TPi-5ItnroWPNW4nOPIv3DmyH8cjehjGQAwWo)


%s

"""

boyfriend = girlfriend

bj = """

"Veganism is a way of living that seeks to exclude, as far as possible and practicable, all forms of exploitation of, and cruelty to, animals for food, clothing and any other purpose."

* The Vegan Society

So, assuming that the semen is coming from a consenting human then, yes - you can swallow and be vegan.

%s

"""

swallow = bj

bible = """

While it's true that God did give permission to eat meat in Genesis 9:3, this was not a command. The original command was given at Genesis 1:28, which was to eat vegetation, seeds and fruit. God permitted the eating of meat, but he doesn't require it.

Scholars even point out that the "land flowing with milk and honey" was referring to plant nectar, rather than bee honey, and that the milk was probably referring to sheep or goat milk. The idea was to show that the land would be fertile, producing plenty of plants and fruit and that the flocks would also be fertile and giving birth to many young animals. Nowhere is it stated that these are for human consumption.

Proverbs 12:10 says: "Good people are good to their animals; the 'good-hearted' bad people kick and abuse them." (Message Bible) Animal abuse is not condoned by the scriptures.

Using the Bible to justify meat-eating is similar to using it to justify slavery. Both were permitted, but neither were required or commanded.

%s

"""

labmeat = """

"Veganism is a way of living that seeks to exclude, as far as possible and practicable, all forms of exploitation of, and cruelty to, animals for food, clothing and any other purpose."

* The Vegan Society

If no animal exploitation was involved, then ethically there would be no issue with lab-grown meat from a vegan standpoint. At the moment, though, lab-grown meat still requires the use of animal cells. 

Additionally, there is a common perception that all vegans secretly crave meat and that not eating it is an exercise in deprivation. In fact, many vegans don't like the taste and texture of meat and wouldn't want to eat it even if it was produced without any animal exploitation. So, while some vegans may be counting the days until they can enthusiastically chow down on ethically-produced lab-grown meat, a large number still probably would not.

%s

"""

maycontain = """

A common question is whether vegans can eat products say they *May contain* milk or eggs when these don't appear on the list of ingredients.

The reason food manufacturers put this on the label is to warn of potential cross-contamination. Perhaps the production line or machines are used to make both the vegan and the non-vegan products, so they cannot guarantee that all traces of milk and egg have been removed. This warning is primarily for people with food allergies.

If the ingredients list is free of products that are the result of animal exploitation, and you don't have a severe food allergy to either eggs or milk, then it's up to you whether you choose to buy and eat the product.

Being vegan is not about following a set of laws, but acting in harmony with your conscience and desire to exclude the exploitation of and cruelty to animals.


%s

"""

soy = """

It is a common and persistent myth that soy causes (or worsens) breast cancer, or that it causes excessive estrogen in men. This myth has been around for a long time, but [research suggests that there is no connection between soy intake and cancer or a drop in testosterone levels.](http://www.huffingtonpost.com/2014/07/15/soy-myths_n_5571272.html)

Asian countries have a much higher intake of soy than western nations with no ill effects. Soy is high in protein and tofu contains many beneficial micro-nutrients.



%s

"""

peta = """

PETA is certainly not a perfect organisation. The group has also received accusations of sexism over its use of [scantily-clad women in its campaigns.](https://en.wikipedia.org/wiki/People_for_the_Ethical_Treatment_of_Animals#cite_note-8)

The 'PETA kills animals' campaign, though, was funded by the [Centre for Consumer Freedom - a group financed by Tyson Foods, Wendy's, the group that owns Arby's and the Philip Morris tobacco company.](https://en.wikipedia.org/wiki/Center_for_Organizational_Research_and_Education) For why PETA euthanises animals, please see the [Why PETA Euthanizes](http://www.whypetaeuthanizes.com) website, which includes an official statement from PETA on the subject.

In short, they certainly raise awareness of animal suffering; however their methods are polarising. Many vegans would recommend donating to local shelters or animal charities that are shown to be more effective.


%s

"""

foodchain = """

We are meant to eat meat because we are top of the food chain and therefore have the 'right' to kill lesser animals to survive, right?

Well, does the [food chain](http://imgur.com/UvmPYCR) really exist for humans? Natural carnivores *need* to kill other animals to survive. Their physiology is designed for eating and processing raw meat. Humans are omnivores, so we have a choice. We do not need to eat animals to survive and be perfectly healthy. We are not an apex predator - in fact, we're not really a predator at all. We imprison animals and pay someone else to slaughter and butcher them for us. We don't eat an animal that was recently living, we choose to eat long-dead flesh. In nature, the animals that allow other creatures to kill their meat are scavengers, necrovores. It doesn't sound so appealing now, does it?

Just because we can do something, doesn't mean we should. As the YourVeganFallacyIs.com website says: ["By analogy, a bank robber might claim to be at the top of the corporate ladder since he had the ability to take what belonged to others and chose to do so."](http://yvfi.ca/foodchain)


%s

"""

cheese = """

Cheese, and all dairy products, [are addictive.](http://www.telegraph.co.uk/news/worldnews/northamerica/usa/11949643/Cheese-is-addictive-as-drugs-study-finds.html) This is because of the presence of casein, which releases opiates called casomorphins.

But why on earth are there addictive substances in dairy? This is further proof that cow's milk is not for us, but for baby cows. The casein breaks down into casomorphins, which [helps to ensure the infant's bond with its mother.](http://nutritionfacts.org/2012/06/21/cows-milk-casomorphin-crib-death-and-autism/)

Giving up cheese may be difficult for some people, but that is the same for giving up any addiction.


%s

"""

eskimos = """

Contrary to the oft-quoted myth, the traditional Inuit diet is actually harmful to health. The original 1970s study has been shown to be [seriously flawed in how the data was collected and interpreted](http://www.huffingtonpost.com/neal-barnard-md/eskimo-myth_b_5268420.html).

But, you might say, they live longer and have no heart disease or cancer! Again, not true. The life-expectancy of Inuit people is found to be [10 years less than other populations. Heart disease, strokes and osteoporosis are higher too with excessive mortality rates.](https://www.drmcdougall.com/misc/2015nl/apr/eskimos.htm)

Why is this myth so frequently repeated? As [Dr. Campbell says](http://nutritionstudies.org/masai-and-inuit-high-protein-diets-a-closer-look/), this is further affirmation that [people] love to hear good things about [their] bad habits.


%s

"""

inuit = eskimos

chat = """

If you want to chat with other vegans, then r/vegan runs an IRC channel. You can find out all the info [here.](https://www.reddit.com/r/vegan/wiki/chatroom)

Discord is a voice and text chat system designed for gamers. If you use that, then here is the [r/vegan invite link.](https://discord.gg/SCejk59)

Or you can just keep talking to me! Happy chatting.



%s

"""

irc = discord = chat

reading = """

Here is a list of recommended reading for those who want to become vegan or want to increase their knowledge about veganism and a vegan diet:

## Animal Rights

* Why We Love Dogs, Eat Pigs and Wear Cows - Dr. Melanie Joy
* Eating Animals - Jonathan Safran Foer
* Animal Liberation - Peter Singer

## General & Fiction

* Holy Cow - David Duchovny
* The Vegan Girl's Guide To Life - Melisser Elliott
* The Bees - by Laline Paull

## Nutrition

* Thrive: The Vegan Nutrition Guide to Optimal Performance in Sports and Life - Brendan Brazier
* The China Study - Dr. T. Colin Campbell
* Whole - Dr. T. Colin Campbell
* Becoming Vegan - Brenda Davis
* How Not To Die - Dr. Michael Greger
* The Everything Vegan Pregnancy Book - Reed Mangels

## Recipe Books

* Mayim's Vegan Table - Mayim's Bialik
* Thug Kitchen 101: Fast as F*ck - Thug Kitchen LLC
* Forks Over Knives: The Cookbook - Darshana Thacker and Del Sroufe


If you know of more books that should be on the list, please let us know.


%s

"""

beginner = """

First of all, I want to say how great it is that you're considering veganism. Here are some helpful links to get you started.

* [The Awesome and Incredible /r/vegan Beginner's Guide](https://www.reddit.com/r/vegan/wiki/beginnersguide)
* [The Vegan Starter Kit](http://vegankit.com/why/)
* [Why go vegan?](https://www.vegansociety.com/go-vegan/why-go-vegan) and
* [How to go vegan](https://www.vegansociety.com/go-vegan/how-go-vegan)

Put simply, go vegan for the animals, for the planet, for other people and for your own health and happiness. They're the best possible reasons.


%s

"""

beginners = newbie = beginner

nukes = """

Here are the big guns. Everything you wanted to know about the health effects of a vegan diet.

[Vegan diet in physiological health promotion](http://www.ncbi.nlm.nih.gov/pubmed/10943644)

[Change in quality of life and immune markers after a stay at a raw vegan institute: a pilot study](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2486444/)

[The role of diet and physical activity in breast, colorectal, and prostate cancer survivorship: a review](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3251953/)

[Interindividual differences in response to plant-based diets: implications for cancer risk](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2677005/)

[A Plant-Based Diet, Atherogenesis, and Coronary Artery Disease Prevention](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4315380/)

[Effects of a long-term vegetarian diet on biomarkers of antioxidant status and cardiovascular disease risk](http://www.ncbi.nlm.nih.gov/pubmed/15474873)

[Vegetarian diets and the incidence of cancer in a low-risk population](http://www.ncbi.nlm.nih.gov/pubmed/23169929)

[Reduced cancer risk in vegetarians: an analysis of recent reports](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3048091/)

[Meat Consumption and Cancer Risk](http://www.cancerproject.org/survival/cancer_facts/meat.php)

[Red meat and colon cancer](http://www.ncbi.nlm.nih.gov/pubmed/21558046)

[Study finds unsafe mercury levels in 84 percent of all fish](http://www.cbsnews.com/8301-18563_162-57563739/study-finds-unsafe-mercury-levels-in-84-percent-of-all-fish/)

[Restriction of meat, fish, and poultry in omnivores improves mood](http://www.nutritionj.com/content/11/1/9/abstract)

[Harvard School of Public Health >> milk is NOT the best source of calcium](http://www.hsph.harvard.edu/nutritionsource/calcium-and-milk/)

[Eating less meat and dairy may help reduce osteoporosis risk, Cornell studies show](http://news.cornell.edu/stories/1996/11/eating-less-meat-may-help-reduce-osteoporosis-risk)

[Milk-the promoter of chronic Western diseases](http://www.ncbi.nlm.nih.gov/pubmed/19232475)

[Dairy product, saturated fatty acid, and calcium intake and prostate cancer](http://www.ncbi.nlm.nih.gov/pubmed/18398033)

[Acne, dairy and cancer](http://www.ncbi.nlm.nih.gov/pubmed/18398033)

[Hormones in milk can be dangerous](http://news.harvard.edu/gazette/2006/12.07/11-dairy.html)

[Milk consumption: aggravating factor of acne and promoter of chronic diseases of Western societies](http://www.ncbi.nlm.nih.gov/pubmed/19243483)

[Milk Consumption and Prostate Cancer](http://pcrm.org/health/health-topics/milk-consumption-and-prostate-cancer)

[Dairy Linked to Acne Development](http://www.pcrm.org/health/medNews/dairy-linked-to-acne-development)

[Understanding the Problems with Dairy Products](http://www.pcrm.org/health/medNews/dairy-linked-to-acne-development)

[Nutritional Update for Physicians: Plant-Based Diets](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3662288/)

[Health effects of vegan diets](http://ajcn.nutrition.org/content/89/5/1627S.full)

[Vegetarians have lower levels of triglycerides, total cholesterol, and LDL cholesterol than omnivores](http://www.ncbi.nlm.nih.gov/pubmed/17364116)

[Vegetarian diet may promote allergy protection](http://www.ncbi.nlm.nih.gov/pubmed/21048771)

[Increased consumption of fruits and vegetables promotes cardiovascular health and longevity](http://ajcn.nutrition.org/content/early/2011/05/18/ajcn.110.009340.abstract)

[Vegetarian Diets Linked to Lower Mortality](https://www.nih.gov/news-events/nih-research-matters/vegetarian-diets-linked-lower-mortality)

[Vegetarians have significantly lower heart disease mortality and cancer incidence](http://www.karger.com/Article/Pdf/337301)

[A high-carb low-fat (vegan) diet can reduce total and LDL cholesterol and lead to modest weight reduction](http://www.ncbi.nlm.nih.gov/pubmed/9805219)

[Increased saturated fat can increase total cholesterol, in favor of LDL more than HDL](http://www.health.harvard.edu/staying-healthy/the-truth-about-fats-bad-and-good)

[Vegetarians live longer than omnivores, even when controlling for other health factors](http://www.mensjournal.com/health-fitness/health/go-vegetarian-live-longer-20140717)

[Increased consumption of animal products may lead to increased risk of Alzheimer's disease](http://www.ncbi.nlm.nih.gov/pubmed/24037034)

[High intake of fruits and vegetables associated with reduced risk of breast cancer](http://www.ncbi.nlm.nih.gov/pubmed/22706630)

[Frequent consumption of nuts may protect against risk of cardiovascular disease](http://www.ncbi.nlm.nih.gov/pubmed/1627021)

[Increasing legume intake can protect against coronary heart disease](http://www.ncbi.nlm.nih.gov/pubmed/11718588)

[Increasing dietary folate can protect against stroke and heart disease](http://www.ncbi.nlm.nih.gov/pubmed/11988588)

Increasing dietary fibre can protect against heart and cardiovascular disease: [1](http://www.ncbi.nlm.nih.gov/pubmed/12963562), [2](http://www.ncbi.nlm.nih.gov/pubmed/11755286)

Low intake of dietary cholesterol can prevent heart disease: [1](http://www.ncbi.nlm.nih.gov/pubmed/3052353), [2](http://www.ncbi.nlm.nih.gov/pubmed/16596800)

[Higher intake of fruit and vegetables lowers risk of cardiovascular disease](http://www.ncbi.nlm.nih.gov/pubmed/11010932)

[Diets that are rich in plant-based foods promote longevity](http://www.ncbi.nlm.nih.gov/pubmed/12514290)

[Higher consumption of fruits and vegetables can protect against cerebrovascular diseases](http://www.ncbi.nlm.nih.gov/pubmed/19646291)

[Higher consumption of fruits and vegetables leads to modest reduction in development of major chronic diseases](http://www.ncbi.nlm.nih.gov/pubmed/15523086)

[Higher consumption of fruits and vegetables protects against heart disease](http://www.ncbi.nlm.nih.gov/pubmed/11412050)

[Vegetarians have lower risk of ischemic heart disease](http://ajcn.nutrition.org/content/97/3/597.full.pdf)

[Vegans and vegetarians have lower blood pressure and prevalence of hypertension](http://www.ncbi.nlm.nih.gov/pubmed/12372158)

[Beneficial association between vegetarian diet and cardiovascular risk factors](http://www.ncbi.nlm.nih.gov/pubmed/ 25343719)

[African-American vegans have better cardiovascular disease risk factors than lacto-ovovegetarians](http://www.ncbi.nlm.nih.gov/pubmed/9791838)

[Physicians should recommend plant-based diets to their patients](http://www.ncbi.nlm.nih.gov/pubmed/23704846)

[Vegans and vegetarians have lower BMI than meat eaters](http://www.ncbi.nlm.nih.gov/pubmed/12833118)

[Vegans have lower levels of IGF-1 growth hormone and higher levels of IGF-binding proteins](http://cebp.aacrjournals.org/content/11/11/1441.full.pdf)

[Higher levels of IGF-1 increase risk of (prostate) cancer](http://www.ncbi.nlm.nih.gov/pubmed/12917205)

Plant-based diets can reduce risk of heart disease and stroke: [1](http://www.ncbi.nlm.nih.gov/pubmed/12936948), [2](http://www.ncbi.nlm.nih.gov/pubmed/25431999)

[Whole foods, plant-based diet relieves symptoms of osteoarthritis](http://www.ncbi.nlm.nih.gov/pubmed/25815212)

[Plant-based diets may reduce risk of metabolic syndrome](http://www.ncbi.nlm.nih.gov/pubmed/25084991)

[Vegetarian and vegan diets reduce risk of cancer](http://www.ncbi.nlm.nih.gov/pubmed/21407994)

Health benefits of vegetarian diet far outweigh the potential risks: [1](http://www.ncbi.nlm.nih.gov/pubmed/15806870), [2](http://www.ncbi.nlm.nih.gov/pubmed/24964573)

[Plant-based diets decrease risk of colorectal cancer](http://www.ncbi.nlm.nih.gov/pubmed/25592002)

[Plant-based diets are not nutritionally deficient](http://www.ncbi.nlm.nih.gov/pubmed/24361028)

[Vegetarian diets have significant benefits for weight reduction](http://www.ncbi.nlm.nih.gov/pubmed/26138004)

[Vegetarian diets reduce risk of colorectal cancer](http://www.ncbi.nlm.nih.gov/pubmed/25751512)

[Vegetarian diet is associated with lower blood pressure](http://www.ncbi.nlm.nih.gov/pubmed/24566947)

[Vegetarian diets have more beneficial effects on health than standard American/European diet](http://www.ncbi.nlm.nih.gov/pubmed/7635375)

[Beyond Meatless, the Health Effects of Vegan Diets: Findings from Adventist Cohorts](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4073139/)

[The Health Advantage of a Vegan Diet: Exploring the Gut Microbiota Connection](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4245565/)

[Vegetarian diets: what do we know of their effects on common chronic diseases?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2677008/)

[Vegans/vegetarians have lower risk of cancer](http://www.ncbi.nlm.nih.gov/pubmed/23169929)

[Vegan proteins may reduce risk of cancer, obesity, cardiovascular disease](http://www.ncbi.nlm.nih.gov/pubmed/10687887)

[Vegan diet leads to lower risk of cancer and cardiovascular disease](http://www.ncbi.nlm.nih.gov/pubmed/10943644)

[Vegetarians have better antioxidant and heart disease profiles than healthy omnivores](http://www.ncbi.nlm.nih.gov/pubmed/15474873)

[Plant-based diets can reverse cardiovascular disease](http://www.ncbi.nlm.nih.gov/pubmed/25198208)

[Diabetes, hypertension, obesity more prevalent among meat-eaters than vegetarians](http://www.ncbi.nlm.nih.gov/pubmed/23283037)

[Vegetarian and vegan diets have advantages in treating type 2 diabetes](http://www.ncbi.nlm.nih.gov/pubmed/20425575)

[Strong protective association between Taiwanese vegetarian diet and diabetes](http://www.ncbi.nlm.nih.gov/pubmed/24523914)

[Strong protective association between vegetarian diet and diabetes)](http://www.ncbi.nlm.nih.gov/pubmed/24523914)

[Lower intakes of saturated fat may reduce cognitive decline in individuals with type 2 diabetes](http://www.ncbi.nlm.nih.gov/pubmed/19336640)

[Diets higher in protein and animal protein increase diabetes risk](http://www.pcrm.org/health/medNews/animal-protein-linked-to-increased-diabetes-risk)

[Vegetarian and vegan diets present advantages for type 2 diabetes treatment](http://www.ncbi.nlm.nih.gov/pubmed/19386029)



%s

"""

# ---------- Countries ---------- 


america = """

There are animal abuses happening all over the world. Here are some sad examples from the USA:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=gYTkM1OHFQg
* https://www.youtube.com/watch?v=XPGIMCmpfxU
* https://www.youtube.com/watch?v=aE66ZC7RJQA
* https://www.youtube.com/watch?v=jiil6ONtDxU
* https://www.youtube.com/watch?v=JJ--faib7to
* https://www.youtube.com/watch?v=NOJhvrIkgYc
* https://www.youtube.com/watch?v=0L2mGC4zezM
* https://www.youtube.com/watch?v=bNY4Fjsdft4
* https://www.youtube.com/watch?v=6RNFFRGz1Qs
* https://www.youtube.com/watch?v=vBZW2FKs8qs
* https://www.youtube.com/watch?v=r6E8H3C1CrU
* https://www.youtube.com/watch?v=VHmVxfRSOmE
* https://www.youtube.com/watch?v=OJovxS9-RTQ
* https://www.youtube.com/watch?v=jx-b2o8MCpY
* https://www.youtube.com/watch?v=59LdaOb_Qt8
* https://www.youtube.com/watch?v=Ul2cmwJs140
* https://www.youtube.com/watch?v=7K-FCiSrwTY
* https://www.youtube.com/watch?v=OGc3samj8N8
* https://www.youtube.com/watch?v=vbP_SPCOQHw
* https://www.youtube.com/watch?v=BB5cA8gUAF0
* https://www.youtube.com/watch?v=0Ok6LTvWQY8

%s

"""

usa = america

britain = """

There are animal abuses happening all over the world. Here are some sad examples from the UK:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=pQK4261GXyg
* https://www.youtube.com/watch?v=Y17hygAj_AA
* https://www.youtube.com/watch?v=cSzh9_bmo4Q
* https://www.youtube.com/watch?v=IVGR1N2Pl00
* https://www.youtube.com/watch?v=FOJUj0zyAL0
* https://www.youtube.com/watch?v=TUxg93ghBVA
* https://www.youtube.com/watch?v=YwBqVzpQX-o
* https://www.youtube.com/watch?v=_Alcs_ttNQc
* https://www.youtube.com/watch?v=89LOIibt6T0
* https://www.youtube.com/watch?v=D7PjfphDsc0
* https://www.youtube.com/watch?v=6iTm21O6CGg
* https://www.youtube.com/watch?v=ewS5-DmKmOM
* https://www.youtube.com/watch?v=hI053DSGTVo

%s

"""

uk = england = scotland = wales = ni = britain

ireland = """

There are animal abuses happening all over the world. Here are some sad examples from Ireland:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=b45Mi1insoQ
* https://www.youtube.com/watch?v=NLgjYbxILjU
* https://www.youtube.com/watch?v=YBy5BqCv4us
* https://www.youtube.com/watch?v=g9EIZUKpnlI

%s

"""

eire = ireland

australia = """

There are animal abuses happening all over the world. Here are some sad examples from Australia:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=b-p59v_pKbg
* https://www.youtube.com/watch?v=i23-WToCBIk
* https://www.youtube.com/watch?v=-zHjY9Pc0Nk
* https://www.youtube.com/watch?v=KArL5YjaL5U
* https://www.youtube.com/watch?v=BHXHaJmExak
* https://www.youtube.com/watch?v=UtXuEuDVitQ
* https://www.youtube.com/watch?v=8JD-1JKhOJI
* https://www.youtube.com/watch?v=EBnjw9PF2OY
* https://www.youtube.com/watch?v=pMV8SHQCG9g
* https://www.youtube.com/watch?v=rQfD_zY9RFg
* https://www.youtube.com/watch?v=iiaix3KjbVI
* https://www.youtube.com/watch?v=OcNq24uctHU
* https://www.youtube.com/watch?v=uQKEh4HPnhI

%s

"""

canada = """

There are animal abuses happening all over the world. Here are some sad examples from Canada:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=Be_4O9-i8ho
* https://www.youtube.com/watch?v=HN0g13kMk6s
* https://www.youtube.com/watch?v=iCsEgQfaons
* https://www.youtube.com/watch?v=A9BhRZ4xkME
* https://www.youtube.com/watch?v=HMbWPA-lvKg
* https://www.youtube.com/watch?v=TK2TuqcNWPY

%s

"""

china = """

There are animal abuses happening all over the world. Here are some sad examples from China:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=PtAFHyXS31M
* https://www.youtube.com/watch?v=3lu-ZNIS2Qc
* https://www.youtube.com/watch?v=sasmdYzinp8
* https://www.youtube.com/watch?v=rtl6oVcnYwM
* https://www.youtube.com/watch?v=PENl5091uAM

%s

"""

france = """

There are animal abuses happening all over the world. Here are some sad examples from France:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=iJrxage7lx4
* https://www.youtube.com/watch?v=SzwV2ZwV1g4
* https://www.youtube.com/watch?v=BYqsIGuTlCE
* https://www.youtube.com/watch?v=k87wTVwGz0g

%s

"""

germany = """

There are animal abuses happening all over the world. Here are some sad examples from Germany:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=UejJc-eQiJQ
* https://www.youtube.com/watch?v=NBPn5EYbVW0
* https://www.youtube.com/watch?v=QC-JCBbOuNc

%s

"""

spain = """

There are animal abuses happening all over the world. Here are some sad examples from Spain:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=dR67NeU22g8
* https://www.youtube.com/watch?v=E2UHnOsfxhw
* https://www.youtube.com/watch?v=WNyTRLSE-YA
* https://www.youtube.com/watch?v=5AMJD8bNYF0

%s

"""

netherlands = """

There are animal abuses happening all over the world. Here is a sad example from the Netherlands:

(Warning NSFW/NSFL Content)

* https://www.youtube.com/watch?v=5uDBpkEuJGA

%s

"""

holland = netherlands

sweden = """

There are animal abuses happening all over the world. Here is a sad example from Sweden:

(Warning NSFW/NSFL Content)

* https://vimeo.com/142072652

%s

"""

# ---------- Jokes ----------

joke1 = """

How many omnis does it take to change a lightbulb?

None, they'd rather stay in the dark.



%s

"""

joke2 = """

How many vegans does it take to change a lightbulb?

I don't know, but where do you get your protein?



%s

"""

joke3 = """

I'm not vegan because I love animals, I'm vegan because I hate vegetables.



%s

"""

joke4 = """

Soy milk?

Hola milk, soy Gary


%s

"""

joke5 = """

Why was the vegan angry?
Because he had a bad tempeh


%s

"""

# ---------- Cities ----------

dublin = """


There are an increasing number of great places to eat for vegans in Dublin, Ireland:

* [Sova Food Vegan Butcher](https://www.facebook.com/SovaVeganButcher/) is a great, full vegan restaurant that also serves lunch.
* [Cornucopia](http://www.cornucopia.ie) is a long-established vegetarian restaurant with the majority of dishes being vegan.
* [Veginity Food Truck](https://www.facebook.com/VeginityDublin/), a great vegan food truck in South Dublin.
* [McGuinness's Takeaway](https://www.facebook.com/McGuinnesss-Takeaway-341338262890578/), a traditional chipper with an entire vegan menu. Vegan burgers are cooked in a dedicated frier to avoid contamination with meat products.
* [Firehouse Pizza](http://www.firehousepizza.ie) offers build-your-own pizzas with vegan mozzarella.

^^Please ^^let ^^me ^^know ^^if ^^any ^^of ^^these ^^places ^^are ^^closed ^^down, ^^or ^^if ^^you ^^want ^^to ^^add ^^a ^^new ^^^restaurant. ^^This ^^list ^^is ^^manually ^^maintained.


%s

"""

london = """


London is a paradise for vegans with many dedicated vegan restaurants available, here is a small selection:

* [Manna](http://mannav.com) is a long-established vegan restaurant in the Camden/Chalk Farm area. It's not cheap, but is great for a special meal.
* [222 Veggie Vegan](http://222veggievegan.com/) is a nice, small restaurant in the West Kensington area. It's not expensive and has a good buffet.
* [Vegan Hippo](https://veganhippo.com) does good burgers and cakes. It's in Soho.
* [Mildred's](http://www.mildreds.co.uk) is a vegetarian/vegan restaurant with several branches around the city.
* [Loving Hut](https://lovinghut.co.uk) is based in Archway, and serves Chinese cuisine.
* [Farmacy](http://farmacylondon.com) is near Notting Hill, and is probably not aimed at the budget-conscious.
* [Indian Veg](https://theindianveg.wordpress.com) formerly Indian Veg Bhelpoori is near the Angel tube station. It serves an excellent Indian buffet for less than a fiver.

^^Please ^^let ^^me ^^know ^^if ^^any ^^of ^^these ^^places ^^are ^^closed ^^down, ^^or ^^if ^^you ^^want ^^to ^^add ^^a ^^new ^^restaurant. ^^This ^^list ^^is ^^manually ^^maintained.


%s

"""

charleston = """

Here are some vegan eating options for Charleston, South Carolina:

* [Dellz Uptown](https://www.facebook.com/EatDellz) is not entirely vegan, but has a lot of vegan options.

^^Please ^^let ^^me ^^know ^^if ^^any ^^of ^^these ^^places ^^are ^^closed ^^down, ^^or ^^if ^^you ^^want ^^to ^^add ^^a ^^new ^^^restaurant. ^^This ^^list ^^is ^^manually ^^maintained.

^^Contributed ^^by: ^^/u/woofwoofgrrr


%s

"""

jackson = """

Here are some vegan eating options for Jackson, Mississippi:

* [Rainbow Co-op](http://www.rainbowcoop.org/) speciality vegetarian/vegan
* [High Noon Cafe](http://rainbowcoop.org/index.php/highnoon) a dedicated vegetarian/vegan restaurant
* [Liquid Light Cafe](http://www.run2thelight.com/) has vegan options
* [Babalu](https://www.facebook.com/BABALUfondren/) also has vegan options
* [Whole Foods](http://www.wholefoodsmarket.com/stores/jkn)

^^Please ^^let ^^me ^^know ^^if ^^any ^^of ^^these ^^places ^^are ^^closed ^^down, ^^or ^^if ^^you ^^want ^^to ^^add ^^a ^^new ^^^restaurant. ^^This ^^list ^^is ^^manually ^^maintained.

^^Contributed ^^by: ^^/u/before-the-fall


%s

"""

