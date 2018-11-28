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


nutrition_cats = ['keto',  'mct', 'natural', 'corn-fed', 'cruciferous','paleolithic',
'vegetable', 'cooking', 'factory', 'fat', 'anti-biotic', 'grass-fed', 'gluten', 'vegan', 'vegetarian'
,'paleo', 'ketogenic', 'leaky gut', 'meal prep', 'micronutrient', 'macronutrient', 'pressure cooked carbs', 'sprouted carbs', 'mct oil', 'coconut oil', 'lean protein', 'fat on nutrion label', 'cholestrol', 'natural sugars', 'diabetes', 'brain fog', 'sourdough', 'bcaas', 'essential amino acids'
, 'wild fish', 'farm raised fish', 'corn-fed beef', 'wild game', 'bioavailability', 'amino acids', 'meat', 'grains', 'vitamins', 'supplements', 'sprouts', 'beans', 'legumes', 'lectins', 'night shade', 'auto-immune', 'hormone', 'gluconeogenesis', 'bad fat', 'good fat'
, 'root veggies', 'cruciferous vegetables', 'dark leafy greens', 'anti-inflammatory', 'infloamation', 'energy', 'mood', 'gut brain connection', 'wheat belly', 'fermented', 'vegetable oil', 'cooking oils', 'glysophate', 'pesticides', 'factory farming', 'sugar', 'fat loss', 'free range', 'anti-biotic free', 'organic'
, 'grass-fed dairy', 'grass-fed protein', 'plant based protein', 'animal protein', 'protein', 'blood glucose', 'fiber', 'starch', 'refined sugar', 'refined carbs', 'simple carbs', 'complex carbs', 'carbs', 'white hdl fat', 'brown ldl fat', 'fats', 'prebiotic', 'enzymes', 'probiotic', 'microbiome'
, 'foodmap diet', 'gluten free', 'vegan diet', 'vegetarian diet', 'gut health', 'intermittent fasting', 'paleo diet', 'ketogenic diet']

podcast_names = ['https://www.bodyscience.com.au/podcast/' ,'https://www.onnit.com/podcast/' ,'The Microbiome Podcast' ,'https://thepaleodiet.com/media-gallery/' ,'Paleo Magazine Radio' ,'http://www.nutritiontwins.com/media-page/#radio' ,'Mens Health Live' ,'https://www.thugkitchen.com/forkedup' ,'Eat, Move and Live Better' ,'https://rebootedbody.com/show/' ,'http://liveplanted.com/podcast/' ,'Vegan Warrior Princesses Attack!' ,'Mark dillon’s plant based conversations'
,'Food for Thought: The Joys and Benefits of Living Vegan' ,'https://www.activevegetarian.com/category/podcast/' ,'Vegetarian Zen' ,'https://directory.libsyn.com/shows/view/id/thegutlovingpodcast' ,'https://www.lowfodmapdiets.com/category/podcast/' ,'https://atpscience.com/podcasts/' ,'Latest in Paleo' ,'Keto For Normies' ,'Keto Talk With Jimmy Moore & Dr. Will Cole' ,'Keto For Women Show' ,'The Keto Diet Podcast' ,'Impact Theory with Tom Bilyeu' ,'Primal Endurance Podcast' ,'The Primal Blueprint Podcast' ,'biolayne' ,'https://www.wholehealthrd.com/real-food-radio/' ,'Dishing Up Nutrition' ,'https://soundcloud.com/ketotransformations' ,'The Genius Life' ,'2 Keto Dudes'
,'Balanced Bites: Modern healthy living with Diane Sanfilippo & Liz Wolfe.' ,'Bulletproof Radio' ,'Dr Berg’s Healthy Keto and Intermittent Fasting Podcast' ,'Generation V' ,'Keto Answers Podcast: Low Carb Lifestyle' ,'No Meat Athlete Radio' ,'The Healthy Gut' ,'The Intermittent Fasting Podcast'
,'https://www.probioticlife.net/episodes/' ,'https://www.thesibodoctor.com/sibo-doctor-podcasts/?v=7516fd43adaa' ,'The Ultimate Health Podcast' ,'Underground Wellness Radio' ,'Wellness Force Radio' ,'Live.Life.Better.' ,'The Fat-Burning Man Show' ,'Deliciously Ella: The Podcast' ,'feel good podcast with kimberly snyder' ,'Beauty Inside Out with Kimberly Snyder' ,"Kimberly Snyder's Podcast" ,'House Call With Dr. Hyman' ,"The Doctor's Farmacy with Mark Hyman, M.D." ,'Wabi Sabi - The Perfectly Imperfect Podcast with Candice Kumai' ,'The Paleo Solution' ,'Aubrey Marcus Podcast' ,'The Peter Attia Drive' ,'Heart Doc VIP with Dr. Joel Kahn' ,'https://www.biolayne.com/media/podcasts/' ,'FoundMyFitness'
,'Revolution Health Radio' ,'The Joe Rogan Experience' ,'The Tim Ferriss Show' ,'The Model Health Show' ,'Ben Greenfield Fitness' ,'https://www.stitcher.com/podcast/the-dr-gundry-podcast' ,'https://drhoffman.com/listen/weekly-radio-show-podcast/' ,'Intelligent Medicine' ,"Dr. Joseph Mercola's Natural Health Articles" ,'Take Control of Your Health with Dr. Mercola' ,'Nom Nom Paleo Podcast' ,'The Wellness Mama Podcast']

podcast_names2 = ['Revolution Health Radio' ,'The Joe Rogan Experience' ,'The Tim Ferriss Show']

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
