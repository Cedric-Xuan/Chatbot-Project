<<<<<<< HEAD

# Hong Kong gourmet circle

## Introduction

Our group proposes a Line channel about the Hong Kong Gourmet Circle. User can gain information about Hong Kong delicious food via communicating with our chat bot, including restaurant information (address, menu, picture, and video) and food information (dish name and picture).

**Guidance Text:**

When the user fellow the chat bot channel, the chat bot will automatically reply:

*<u>“Welcome to Hong Kong Gourmet Circle Chat bot Channel! You can input the food type like ’Thailand’ or ‘Thailand food’ to search the restaurant that you are interested in!”</u>*



## Specific queries logic

**①Step 1:**

+ Input: food types
  + (For example: *<u>Thailand Food/Thailand</u>* ) 
  + Input data type: text

+ Output: restaurant name list and restaurant address list
  + Output data type: text 
+ Objective: make user know more about the name and the location of restaurants corresponding the type he search.

**②Step 2:**

+ Input:restaurant name 
  + Input data type:  text
  + (For example:<u>*TAI WAI Roast Duck Restaurant*</u>)

+ Output: main menu about popular dishes list in the corresponding restaurant
  + Output：main menu about popular dishes
  + Output data type:text
+ Objective: make user know more about the menu and popular dishes corresponding the restaurant he search.

**③Step 3:**

+ Input: restaurant name + food name 
  + (For example: <u>*TAI WAI Roast Duck Restaurant + Roast Duck*</u>)
  + Data type: text

+ output: food photo
  + Output data type:image
+ Objective: make user obtain the photography corresponding the dish in the certain restaurant he search.

**④Step 4:**

+ Input: restaurant name + environmental + type
  + (For example：<u>*Roast Duck Restaurant+environmental+image/video*</u>)
  + Data type: text 

+ Output: the environmental photograph or video of the corresponding restaurant
  + Output data type: image/video:video_camera:

