# 美食小天地--LINE Chatbot



## Student info

Posting our team info for TA firstly.

|       Name       | Student number |
| :--------------: | :------------: |
| **XUAN Yongzhe** |  **19409370**  |
| **HAN Zhenxin**  |  **19434294**  |
| **LIN Shidong**  |  **19430000**  |



## 📝 Introduction

With the spread of **COVID-19**, the catering industry in Hong Kong is becoming more and more difficult. In order to support the catering industry **recovery** in Hong Kong, we developed a chat robot based on LINE channel so that we can learn the latest catering information without leaving the house.



Our group proposes a Line channel about the **Hong Kong Gourmet Circle**. User can gain information about **Hong Kong delicious food** via communicating with our chat bot, including restaurant information (address, menu, picture, and video) and food information (dish name and picture). 



## ✏️ Get the point from marking criteria

| Item                                           | Mark | In our project                                               |
| ---------------------------------------------- | ---- | ------------------------------------------------------------ |
| Ability to handle X different types of queries | 1%   | [We main ....](#标题1)                                       |
| Usage of redis server                          | 1%   | As we mention in [technology](#-Technology) table, we use redis to store the record of user behavior. |
| Consumption of other service other than redis  | 2%   | We use [MongoDB, Alibaba OSS, CentOS cloud server and google maps API as our other service](#-Technology). |
| Compliance of other constrains                 | 1%   |                                                              |
| Usefulness of the bot to the real world        | 7%   | [Helping HK catering industry recover from COVID-19's effect.](#-Introduction) |
| Appropriate usage of technologies              | 2%   |                                                              |
| Attractiveness and completeness                | 2%   | The [screenshot](#-Screenshot-of-LINE-channel) of our channel show the attractiveness, and we use many [technologies](#-Technology) to achieve completeness |
| Presentation                                   | 1%   |                                                              |
| sub-total                                      | 17%  |                                                              |
| milestone4.pdf                                 | 10%  | We spend many time on writing [milestone4.pdf](https://github.com/Cedric-Xuan/Chatbot-Project/blob/master/7940_milestone4.pdf) |
| Total for Milestone 4                          | 27%  |                                                              |



## 🍉 Demo

![LINE](/img/LINE_QR.png)



## 🔧 Technology

The technologies we currently as follow:

| Technology/material                 |                            Usage                             |
| :---------------------------------- | :----------------------------------------------------------: |
| Heroku                              |          provide a platform to support our chatbot.          |
| Python                              | Use pyhton to develop our chatbot, to process different type of message and query, and set controls of LINE channel. |
| Linux / Alibaba Cloud server        |                Support our MongoDB database.                 |
| MongoDB                             |               Store the json data of gourmet.                |
| Redis                               |     Record user behavior via usage count of each function.    |
| Alibaba OSS(Object Storage Service) |          Store large file, such as image and video.          |
| Google Maps API                     |Recommend 3 nearby restaurants to user in the certain location or address.|
| LINE Messaging API                  | LINE API provide the information transmission between chatbot and LINE channel. |



## 💾 Capacity of service

##### Expand Cloud Storage:

Talking about the storage capacity, we use OSS (object storage service), which is provided by Alibaba Cloud, we upload large data, such as video and image, into OSS.



We also have rented a cloud server for this project, it is a 2 core 4G memory CentOS server. We install MongoDB in it, and the hard disk capacity of our server is 40G, so the capacity of storage is large enough for this service.



#####  Improve the processing ability of Flask

If many users send requests at the same time, the system may have the problem of high concurrency. The blocking may happen when we meet this problem. In order to improve the processing ability in this high workload situation, we are able to change the mode of the Flask in Heroku, leading to turn off debug mode and turn on the multiple thread mode.



##  💡 Screenshot of LINE channel

​         <img src="/img/LINE1.jpg" width = "280" height = "569" />                                    <img src="/img/LINE2.jpg" width = "280" height = "569" />

