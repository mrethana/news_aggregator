import tweepy
from apikeys import *

auth = tweepy.OAuthHandler(twitter_1, twitter_2)
auth.set_access_token(twitter_3, twitter_4)


all_handles = ['@ATPScience1', '@waitrose', '@MicrobiomeInst', '@veganrecipescom', '@cldiet', '@Onnit', '@vegsoc', '@VeganKosher', '@TheVeganSociety', '@vegan', '@Keto_Recipes_', '@the52diet', '@IFdiet', '@microbiome', '@metagenomics', '@microbiome_news', '@TheGutStuff', '@MyGutHealth', '@PaleoFX',
'@PaleoFoundation', '@ThePaleoDiet', '@PaleoComfort', '@cavemanketo', '@KetoFlu', '@TheKetoKitchen_', '@EatKetoWithMe', '@KetoConnect', '@KetoDietZone', '@Ketogenic', '@USDANutrition', '@FoodRev', '@CSPI', '@simplyrecipes', '@FoodNetwork', '@CookingChannel', '@tasty', '@nytfood', '@finecooking', '@mrcookingpanda'
, '@FODMAPeveryday', '@FODMAPLife', '@FodmappedInfo', '@thefodmapdoctor', '@SimplyGlutenFre', '@gfliving', '@sibotest', '@manjulaskitchen', '@VegTimes', '@CookingLight', '@mealprepwl', '@thehealthygut', '@VitalGutHealth', '@pureguthealth', '@PaleoForBegin', '@PaleoLeap', '@ThePaleoMom', '@paleomagazine', '@PaleoHacks', '@paleogrubs',
'@naturalgourmet', '@Low_Carb_Keto', '@NutritionTwins', '@mckelhill', '@WomensFitnessAu', '@WomensHealthMag', '@MensHealthMag', '@mjfit', '@thugkitchen', '@Leslie_Klenke', '@insidePN', '@ThisMamaCooks', '@EdibleWildFood', '@TheEarthDieter', '@HarvardHealth', '@EverydayHealth', '@DailyHealthTips']
