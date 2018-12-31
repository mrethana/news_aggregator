import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.tokenize import RegexpTokenizer
import random


#all twitter handles to scrape
twitter_handles = ['@ATPScience1', '@waitrose', '@MicrobiomeInst', '@veganrecipescom', '@cldiet', '@Onnit', '@vegsoc', '@VeganKosher', '@TheVeganSociety', '@vegan', '@Keto_Recipes_', '@the52diet', '@IFdiet', '@microbiome', '@metagenomics', '@microbiome_news', '@TheGutStuff', '@MyGutHealth', '@PaleoFX',
'@PaleoFoundation', '@ThePaleoDiet', '@PaleoComfort', '@cavemanketo', '@KetoFlu', '@TheKetoKitchen_', '@EatKetoWithMe', '@KetoConnect', '@KetoDietZone', '@Ketogenic', '@USDANutrition', '@FoodRev', '@CSPI', '@simplyrecipes', '@FoodNetwork', '@CookingChannel', '@tasty', '@nytfood', '@finecooking', '@mrcookingpanda'
, '@FODMAPeveryday', '@FODMAPLife', '@FodmappedInfo', '@thefodmapdoctor', '@SimplyGlutenFre', '@gfliving', '@sibotest', '@manjulaskitchen', '@VegTimes', '@CookingLight', '@mealprepwl', '@thehealthygut', '@VitalGutHealth', '@pureguthealth', '@PaleoForBegin', '@PaleoLeap', '@ThePaleoMom', '@paleomagazine', '@PaleoHacks', '@paleogrubs',
'@naturalgourmet', '@Low_Carb_Keto', '@NutritionTwins', '@mckelhill', '@WomensFitnessAu', '@WomensHealthMag', '@MensHealthMag', '@mjfit', '@thugkitchen', '@Leslie_Klenke', '@insidePN', '@ThisMamaCooks', '@EdibleWildFood', '@TheEarthDieter', '@HarvardHealth', '@EverydayHealth', '@DailyHealthTips']

youtube_searches = ['@Dr.DonColbert', '@StephandAdam', '@NicholaLudlam-Raine', '@RachelAust', '@TheDietKitchen', '@SweetPotatoSoul', '@TheLeanMachines', '@CarlyRowena', '@HighCarbHannah', '@ColleenPatrick-Goudreau', '@ActiveVegetarian', '@VegetarianZen', '@ATPScience', '@WillCole', '@JimmyMoore', '@KetoForWomenShow', '@TheKetoDiet-HealthfulPursuit', '@TomBilyeu', '@PrimalBlueprint'
, '@DishingUpNutrition', '@PatrickHolford', '@realfoodforager', '@HolisticWellnessProject', '@CenterforNutritionStudies', '@DoctorOz', '@Clean&Delicious', '@MingleSeasoning', '@CleanFoodDirtyCity', '@MeowMeix', '@SproutedKitchen', '@MyNewRoots', '@AmeliaFreer', '@KatieLolas', '@caligirlgetsfit', '@KetoKarma', '@ohmyketo', '@GreenKitchenStories', '@MaxLugavere', '@2KetoDudes'
, '@DianeSanfilippo', '@Bulletproof', '@Dr.EricBergDC', '@NimaiDelgado', '@Dr.AnthonyGustin', '@MattFrazier', '@TheHealthyGut', '@MelanieAvalon', '@TheSIBODoctor', '@MarniWasserman', '@TheUltimateHealthPodcast', '@SeanCroxton', '@WellnessForce', '@AndyGalpin', '@OhSheGlows', '@FullyRawKristina', '@HEMSLEY+HEMSLEY', '@AbelJames', '@HealthiNation', '@FitMenCook'
, '@DeliciouslyElla', '@KimberlySnyder', '@Whole30®', '@MarkHyman,MD', '@doctorjoshaxe', '@JordanSyatt', '@TrentMcCloskey', '@CarterGood', '@RussCrandall', '@PatriciaBannan,RDN', '@EaStewart', '@DreenaBurton', '@DietitianCassie', '@DanielleOmar', '@DanChurchill', '@alexandracaspero', '@TheAtlantic', '@CandiceKumai', '@RobbWolf', '@AubreyMarcus'
, '@PeterAttia,MD', '@JoelKahn', '@biolayne', '@FoundMyFitness', '@ChrisKresser,L.Ac', '@PowerfulJRE', '@fourhourchef', '@TimFerriss', '@TheShawnModel', '@BenGreenfieldFitness', '@jorgecruise', '@Dr.Gundry', '@Alannmd', '@DrAnnLouise', '@mercola', '@drfuhrman', '@nomnompaleo', '@MariaEmmerich', '@JamieOliver', '@ThePaleoMom'
, '@NativePath', '@TheSugarfreemom', '@CookingKetoWithKristie', '@TheFoodbabe', '@katiewellnessmama', '@Waitrose&Partners', '@VeganRecipes', '@Onnit', '@TheVegetarianSociety', '@ShamayimVAretzInstitute', '@TheVeganSociety', '@TheGutStuff', '@PaleoFX', '@CavemanKeto', '@KetoConnect', '@USDA', '@FoodRevolutionNetwork', '@CSPITV', '@SimplyRecipes', '@FoodNetwork',
 '@CookingChannel', 'RecipeswithMelissaClark', '@FineCooking', '@HomeCookingShow', '@CookingPanda', '@FODMAPEveryday', '@FODMAPLife', '@FODMAPPEDFOODS', '@SimplyGlutenFreebyCarolKicinski', '@SIBOSolution(Dr.MelanieKeller)', '@ManjulasKitchen', '@VegetarianTimes', '@Tasty', '@SeaShepherd', '@GreenHealthyCooking', '@CookingLight', '@EatingWellMagazine', '@HealthyRecipes', '@PaleolithicDiet', '@PaleoMagazine',
 '@PaleoHacks', '@PaleoGrubs', '@nutritionstripped', '@WomensHealthMag', '@MensHealthMag', '@MensFitnessUS', '@skinnytaste', '@thugkitchen', '@PrecisionNutrition', '@UC5BpcDICcOLVFVmVNLRXM8w', '@rebootedbody', '@EverydayHealth', '@TheNewYorkTimes']


nutrition_cats = ['aminos','keto','pressure cooked carbs','sprouted carbs','mct','coconut','farm','corn-fed','corn fed','amino','cruciferous','wheat','vegetable','cooking','factory','anti-biotic','anti biotic','grass-fed','grass fed','plant','animal','blood','refined','simple'
,'complex carbs','foodmap','gluten','vegan','vegetarian','gut','paleo','ketogenic','infloamation','vegetable oil','organic','gluten free','vegan diet','vegetarian diet','intermittent fasting','night shade','root veggies','cruciferous vegetables','grains','glysophate','pesticides','factory farming','free range','anti-biotic free','anti biotic free',
'sprouts','beans','legumes','lectins','dark leafy greens','foodmap diet','paleo diet','ketogenic diet','micronutrient','macronutrient','diabetes','meal prep','leaky gut','fat on nutrion label','lean protein','cholestrol','natural sugars','brain fog','mct oil','coconut oil','pressure cooked carbs','sprouted carbs','sourdough','bcaas','essential amino acids'
,'wild fish','farm raised fish','corn-fed beef','wild game','bioavailability','amino acids','meat','sprouted','vitamins','supplements','auto-immune','hormone','gluconeogenesis','bad fat','good fat','anti-inflammatory','anti inflammatory','inflammation','energy','mood','gut brain connection','wheat belly','fermented','vegetable oils','cooking oils'
,'fat loss','grass-fed dairy','grass-fed protein','grass fed dairy','grass fed protein'
,'plant based protein','animal protein','protein','sugar','blood glucose','fiber','starch','refined sugar','refined carbs','simple carbs','complex carbs','carbs','white hdl fat','brown ldl fat','brown ldl','fats','prebiotic','enzymes','probiotic','microbiome','gut health']

podcast_names = ['https://www.bodyscience.com.au/podcast/' ,'https://www.onnit.com/podcast/' ,'The Microbiome Podcast' ,'https://thepaleodiet.com/media-gallery/' ,'Paleo Magazine Radio' ,'http://www.nutritiontwins.com/media-page/#radio' ,'Mens Health Live' ,'https://www.thugkitchen.com/forkedup' ,'Eat, Move and Live Better' ,'https://rebootedbody.com/show/' ,'http://liveplanted.com/podcast/' ,'Vegan Warrior Princesses Attack!' ,'Mark dillon’s plant based conversations'
,'Food for Thought: The Joys and Benefits of Living Vegan' ,'https://www.activevegetarian.com/category/podcast/' ,'Vegetarian Zen' ,'https://directory.libsyn.com/shows/view/id/thegutlovingpodcast' ,'https://www.lowfodmapdiets.com/category/podcast/' ,'https://atpscience.com/podcasts/' ,'Latest in Paleo' ,'Keto For Normies' ,'Keto Talk With Jimmy Moore & Dr. Will Cole' ,'Keto For Women Show' ,'The Keto Diet Podcast' ,'Impact Theory with Tom Bilyeu' ,'Primal Endurance Podcast' ,'The Primal Blueprint Podcast' ,'biolayne' ,'https://www.wholehealthrd.com/real-food-radio/' ,'Dishing Up Nutrition' ,'https://soundcloud.com/ketotransformations' ,'The Genius Life' ,'2 Keto Dudes'
,'Balanced Bites: Modern healthy living with Diane Sanfilippo & Liz Wolfe.' ,'Bulletproof Radio' ,'Dr Berg’s Healthy Keto and Intermittent Fasting Podcast' ,'Generation V' ,'Keto Answers Podcast: Low Carb Lifestyle' ,'No Meat Athlete Radio' ,'The Healthy Gut' ,'The Intermittent Fasting Podcast'
,'https://www.probioticlife.net/episodes/' ,'https://www.thesibodoctor.com/sibo-doctor-podcasts/?v=7516fd43adaa' ,'The Ultimate Health Podcast' ,'Underground Wellness Radio' ,'Wellness Force Radio' ,'Live.Life.Better.' ,'The Fat-Burning Man Show' ,'Deliciously Ella: The Podcast' ,'feel good podcast with kimberly snyder' ,'Beauty Inside Out with Kimberly Snyder' ,"Kimberly Snyder's Podcast" ,'House Call With Dr. Hyman' ,"The Doctor's Farmacy with Mark Hyman, M.D." ,'Wabi Sabi - The Perfectly Imperfect Podcast with Candice Kumai' ,'The Paleo Solution' ,'Aubrey Marcus Podcast' ,'The Peter Attia Drive' ,'Heart Doc VIP with Dr. Joel Kahn' ,'https://www.biolayne.com/media/podcasts/' ,'FoundMyFitness'
,'Revolution Health Radio' ,'The Joe Rogan Experience' ,'The Tim Ferriss Show' ,'The Model Health Show' ,'Ben Greenfield Fitness' ,'https://www.stitcher.com/podcast/the-dr-gundry-podcast' ,'https://drhoffman.com/listen/weekly-radio-show-podcast/' ,'Intelligent Medicine' ,"Dr. Joseph Mercola's Natural Health Articles" ,'Take Control of Your Health with Dr. Mercola' ,'Nom Nom Paleo Podcast' ,'The Wellness Mama Podcast']

movie_list = ['Somebody Feed Phil' , 'Meat Eater' , 'Salt, Fat, Heat, Acid' , 'For Grace' , 'Chef vs Science: The Ultimate Kitchen Challenge' , 'Ugly Delicious' , 'Avec Eric' , 'The Great British Baking Show' , 'Lords and Ladles' , 'Cooking on High' , 'The Mind of a Chef' , 'Anthony Bourdain Parts Unknown' , 'Jeremiah Tower: The Last Magnificent' , 'In Search of Israeli Cuisine' , 'Theater of Life' , 'Sour Grapes'
, 'Chefs Table' , 'Noma: My Perfect Storm' , 'The Birth of Saké' , 'Barbecue' , 'A Year in Champagne' , '42 grams' , 'Sugar Coated' , 'Somm' , 'More Than Honey' , 'Jiro Dreams of Sushi' , 'Spinning Plates' , 'The Future of Food' , 'Ingredients' , 'Simply Raw: Reversing Diabetes in 30 Days' , 'Sustainable' , 'A Place at the Table' , 'Farmageddon'
 , 'Bite Size' , 'Food Chains' , 'Plant Pure Nation' , 'Super Size Me' , 'Food Matters' , 'Food Choices' , 'In Defense of Food' , 'What the Health' , 'GMO OMG' , 'Cowspiracy' , 'Vegucated' , 'Fat, Sick & Nearly Dead' , 'Fed Up' , 'Food Inc.' , 'Hungry for Change' , 'Rotten'
 , 'Cooked' , 'Forks Over Knives' , 'The Magic Pill']

sources_list = ['abc-news',
 'associated-press',
 'axios',
 'bbc-news',
 'bbc-sport',
 'bleacher-report',
 'bloomberg',
 'breitbart-news',
 'business-insider',
 'buzzfeed',
 'cbc-news',
 'cbs-news',
 'cnbc',
 'cnn',
 'crypto-coins-news',
 'daily-mail',
 'engadget',
 'entertainment-weekly',
 'espn',
 'financial-post',
 'financial-times',
 'fox-news',
 'fox-sports',
 'google-news',
 'hacker-news',
 'ign',
 'independent',
 'mashable',
 'medical-news-today',
 'msnbc',
 'mtv-news',
 'national-geographic',
 'national-review',
 'nbc-news',
 'new-scientist',
 'newsweek',
 'new-york-magazine',
 'nfl-news',
 'nhl-news',
 'nrk',
 'politico',
 'recode',
 'reddit-r-all',
 'reuters',
 'techcrunch',
 'techradar',
 'the-american-conservative',
 'the-economist',
 'the-guardian-au',
 'the-guardian-uk',
 'the-huffington-post',
 'the-lad-bible',
 'the-new-york-times',
 'the-next-web',
 'the-sport-bible',
 'the-telegraph',
 'the-verge',
 'the-wall-street-journal',
 'the-washington-post',
 'the-washington-times',
 'time',
 'usa-today',
 'vice-news',
 'wired',
 'ynet']
sources_joined = ','.join(sources_list)

def tokenize_text(words):
    tokenizer = RegexpTokenizer('[A-Za-z]\w+')
    all_tokens = tokenizer.tokenize(words)
    case_insensitive = [token.lower() for token in all_tokens]
    bigrams = list(ngrams(case_insensitive,2))
    joined = [' '.join(gram) for gram in bigrams]
    trigrams = list(ngrams(case_insensitive,3))
    tri_joined = [' '.join(gram) for gram in trigrams]
    case_insensitive.extend(joined)
    case_insensitive.extend(tri_joined)
    return set(case_insensitive)

def random_difficulties(length_of_df):
    difficulties = []
    for i in list(range(0,length_of_df)):
        difficulties.append(random.choice(['Easy','Medium','Hard']))
    return difficulties

def find_categories(text_to_tokenize, categories):
    categories_dict = {1:'null',2:'null',3:'null',4:'null',5:'null'}
    words = tokenize_text(text_to_tokenize)
    intersection = list(words.intersection(categories))
    if len(intersection) > 0:
        for i in list(range(0,len(intersection))):
            categories_dict[i+1] = intersection[i]
    else:
        categories_dict[1] = 'general_nutrition'
    return categories_dict
