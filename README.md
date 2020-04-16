# 美食小天地--LINE Chatbot



## 📝 Introduction

With the spread of **COVID-19**, the catering industry in Hong Kong is becoming more and more difficult. In order to support the catering industry **recovery** in Hong Kong, we developed a chat robot based on LINE channel so that we can learn the latest catering information without leaving the house.



Our group proposes a Line channel about the **Hong Kong Gourmet Circle**. User can gain information about **Hong Kong delicious food** via communicating with our chat bot, including restaurant information (address, menu, picture, and video) and food information (dish name and picture). 



## Student info

Posting our team info for TA firstly.

|       Name       | Student number |
| :--------------: | :------------: |
| **XUAN Yongzhe** |  **19409370**  |
| **HAN Zhenxin**  |  **19434294**  |
| **LIN Shidong**  |  **19430000**  |



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
| Redis                               |                                                              |
| Alibaba OSS(Object Storage Service) |          Store large file, such as image and video.          |
| Google Maps API                     |                                                              |
| LINE Messaging API                  | LINE API provide the information transmission between chatbot and LINE channel. |



## ✏️ Capacity of service

##### Expand Cloud Storage:

Talking about the storage capacity, we use OSS (object storage service), which is provided by Alibaba Cloud, we upload large data, such as video and image, into OSS.



We also have rented a cloud server for this project, it is a 2 core 4G memory CentOS server. We install MongoDB in it, and the hard disk capacity of our server is 40G, so the capacity of storage is large enough for this service.



#####  Improve the processing ability of Flask

If many users send requests at the same time, the system may have the problem of high concurrency. The blocking may happen when we meet this problem. In order to improve the processing ability in this high workload situation, we are able to change the mode of the Flask in Heroku, leading to turn off debug mode and turn on the multiple thread mode.



##  💡 Screenshot of LINE channel

<img src="/img/LINE1.jpg" alt="LINE" style="zoom: 25%;" />

<img src="/img/LINE2.jpg" alt="LINE" style="zoom:25%;" />

