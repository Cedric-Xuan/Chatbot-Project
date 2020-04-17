# 美食小天地--LINE Chatbot

- [美食小天地--LINE Chatbot](#-------line-chatbot)
  * [Student info](#student-info)
  * [📝 Introduction](#-introduction)
  * [✏️ Get the point from marking criteria](#-Get-the-point-from-marking-criteria)
  * [🍉 Demo](#-demo)
  * [🔧 Technology](#-technology)
  * [💾 Capacity of service](#-capacity-of-service)
        * [Expand Cloud Storage:](#-expand-cloud-storage-)
        * [Improve the processing ability of Flask](#improve-the-processing-ability-of-flask)
  * [💡 Description of different fuction](#-description-of-different-fuction)
        * [1.All style](#1all-style)
        * [2.Certain style](#2certain-style)
        * [3.Recent coupons information](#3recent-coupons-information)
        * [4.Detail information of restaurants](#4detail-information-of-restaurants)
        * [5.popular dishes](#5popular-dishes)
        * [6.Environment](#6environment)
        * [7.Location](#7location)
        * [8.Telphone](#8telphone)
        * [9.Nearby high rating restaurants](#9nearby-high-rating-restaurants)

## Student info

Posting our team info for TA firstly.

|       Name       | Student number |
| :--------------: | :------------: |
| **XUAN Yongzhe** |  **19409370**  |
| **HAN Zhenxin**  |  **19434294**  |
| **LIN Shidong**  |  **19430000**  |



## 📝 Introduction

With the spread of **COVID-19**, the catering industry in Hong Kong is becoming more and more difficult. In order to support the catering industry **recovery** in Hong Kong, we developed a chat robot based on LINE channel so that we can learn the latest catering information without leaving the house.



Our group proposes a Line channel about the **Hong Kong Gourmet Circle**. User can gain information about **Hong Kong delicious food** via communicating with our chat bot, including restaurant information (address, menu, picture, and video) and food information (dish name and picture), also, we add web crawler to get latest hot coupons of restaurants. 



## ✏️ Get the point from marking criteria

| Item                                           | Mark | In our project                                               |
| ---------------------------------------------- | ---- | ------------------------------------------------------------ |
| Ability to handle X different types of queries | 1%   | [All style](#1All-style); [a certain style](#2Certain-style); [popular dishes](#5popular-dishes); [telphone](#8Telphone); [location](#7Location); [environment picture/video](#6Environment); [detail information of restaurants](#4Detail-information-of-restaurants); [recent coupons information](#3Recent-coupons-information); [nearby high rating restaurants](#9Nearby-high-rating-restaurants), totally 9 of them. |
| Usage of redis server                          | 1%   | As we mention in [technology](#-Technology) table, we use redis to store the record of user behavior. |
| Consumption of other service other than redis  | 2%   | We use [MongoDB, Alibaba OSS, CentOS cloud server and google maps API](#-Technology) as our other service. |
| Compliance of other constrains                 | 1%   | As you can see, we developed this project all follow teacher's requirement. |
| Usefulness of the bot to the real world        | 7%   | [Helping HK catering industry recover from COVID-19's effect.](#-Introduction) |
| Appropriate usage of technologies              | 2%   | No matter is Redis, MongoDB or OSS, we have exactly [purposes ](#-Technology)of usage |
| Attractiveness and completeness                | 2%   | The [screenshot](#-Description-of-different-fuction) of our channel show the attractiveness, and we use many [technologies](#-Technology) to achieve completeness |
| Presentation                                   | 1%   | Update later~                                                |
| sub-total                                      | 17%  | We try our best to chase the point above, so we believe we can get all point above. |
| milestone4.pdf                                 | 10%  | We spend many time on writing [milestone4.pdf](https://github.com/Cedric-Xuan/Chatbot-Project/blob/master/7940_milestone4.pdf) |
| Total for Milestone 4                          | 27%  |                                                              |



## 🍉 Demo

​	**Scan the QR code to fellow the LINE Channel.**



![LINE](/img/LINE_QR.png)



​											



## 🔧 Technology

The technologies we currently as follow:

| Technology/material                 |                            Usage                             |
| :---------------------------------- | :----------------------------------------------------------: |
| Heroku                              |          provide a platform to support our chatbot.          |
| Python                              | Use pyhton to develop our chatbot, to process different type of message and query, and set controls of LINE channel. |
| Linux / Alibaba Cloud server        |                Support our MongoDB database.                 |
| MongoDB                             |               Store the json data of gourmet.                |
| Redis                               | Record user behavior via usage count of each function, store latest hot coupons. |
| Alibaba OSS(Object Storage Service) |          Store large file, such as image and video.          |
| Google Maps API                     | Recommend 3 nearby restaurants to user in the certain location or address. |
| LINE Messaging API                  | LINE API provide the information transmission between chatbot and LINE channel. |
| Web crawler                         |            Get latest hot coupons of restaurants             |



## 💾 Capacity of service

#####  Expand Cloud Storage:

Talking about the storage capacity, we use OSS (object storage service), which is provided by Alibaba Cloud, we upload large data, such as video and image, into OSS.



We also have rented a cloud server for this project, it is a 2 core 4G memory CentOS server. We install MongoDB in it, and the hard disk capacity of our server is 40G, so the capacity of storage is large enough for this service.



#####  Improve the processing ability of Flask

If many users send requests at the same time, the system may have the problem of high concurrency. The blocking may happen when we meet this problem. In order to improve the processing ability in this high workload situation, we are able to change the mode of the Flask in Heroku, leading to turn off debug mode and turn on the multiple thread mode.



##  💡 Description of different fuctions

In this part, we will introduce the fuction of our chatbot, post all specific screenshot of demonstration, and we also welcome you to test it in our channel.

##### 1.All style

We can choose different functions via the initial menu, made by rich-menu in Line.

In this menu, we have four different type of dishes, Chinese food, Japeness food, Western food and Thai food, user can query different type of food via click different button.

<img src="/img/All_list_img.jpg" width = "280" height = "569" /> 



##### 2.Certain style

When you select specific type of cuisine, for example, Western food, you will get the restuarant list.

<img src="/img/Food_type_img.jpg" width = "280" height = "569" />



##### 3.Recent coupons information

If you choose "Gain western coupons", then you can get some coupons of different restuarants.

<img src="/img/Conpon_img.jpg" width = "280" height = "569" />

##### 4.Detail information of restaurants

If you choose specific restuarant, for example, "登堂", then you can continue select popular dishes, environment, location and call restuarant.

<img src="/img/Specific_restuarant_img.jpg" width = "280" height = "569" />



##### 5.popular dishes

Get popular dishes of the restuarant(Show in the bottom of interface).

<img src="/img/popular_dishes_img.jpg" width = "280" height = "569" />

##### 6.Environment

Get the picture/video of restuarant.

<img src="/img/Environment_img.jpg" width = "280" height = "569" />

##### 7.Location

Get the address of restuarant.

<img src="/img/Location_img.jpg" width = "280" height = "569" />

##### 8.Telphone

Get the address of restuarant, and you can make a phone call.

<img src="/img/Phone_img.jpg" width = "280" height = "569" />

##### 9.Nearby high rating restaurants

Recommend three high rating restaurants near the query address randomly.<br>You can send keyword "nearby address" or send location message directly.

<img src="/img/Nearby_img.jpg" width = "280" height = "569" />    <img src="/img/Nearby2_img.jpg" width = "280" height = "569" />



