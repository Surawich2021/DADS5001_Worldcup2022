![worldcup01](https://user-images.githubusercontent.com/77851559/204706658-5cecb3b2-0f52-451c-b892-83816b1ba7fd.jpg)


# Topic:
 - การบันทึกข้อมูลผลการแข่งขันฟุตบอลโลก World Cup 2022
 - การเรียกดูรายงานสรุปผลการแข่งขันฟุตบอลโลก World Cup 2022

# Dataset:
worldcup2022_rawdata.json from link : https://fixturedownload.com/results/fifa-world-cup-2022

# Challenge:
1. ใช้เวลาในการทำความเข้าใจโครงสร้างข้อมูล JSON

2. ใช้เวลาในการเรียนรู้ Python Library Pymongo, PySimpleGUI

3. บางครั้ง MongoDB Cloud connection ที่สิงค์โปร์ทำงานช้ามาก


# Github link:
https://github.com/Surawich2021/DADS5001_Worldcup2022


![worldcup02](https://user-images.githubusercontent.com/77851559/204709971-7337f0d9-0ee6-44ea-b40b-a9fae8e8409d.jpg)
  ฟุตบอลโลก World Cup 2022 (อาหรับ: 2022 كأس العالم لكرة القدم, Kaʾs al-ʿālam li-kurat al-qadam 2022) เป็นการแข่งขันฟุตบอลชายทีมชาติของทุกชาติสมาชิกฟีฟ่าที่จะจัดขึ้นทุกสี่ปี โดยครั้งนี้จัดขึ้นที่ประเทศกาตาร์ ตั้งแต่วันที่ 20 พฤศจิกายน ถึง 18 ธันวาคม 2022 นี่จะเป็นฟุตบอลโลกครั้งแรกที่จัดในโลกอาหรับ และเป็นครั้งที่สองที่จัดในทวีปเอเชียต่อจากฟุตบอลโลก 2002 ที่เกาหลีใต้และญี่ปุ่น นอกจากนี้ ยังเป็นครั้งสุดท้ายที่มีทีมร่วมแข่งขัน 32 ทีม เนื่องจากจะมีการเพิ่มขึ้นเป็น 48 ทีมในฟุตบอลโลก 2026 และด้วยสภาพอากาศที่ร้อนจัดในฤดูร้อนของประเทศกาตาร์ ทำให้ฟุตบอลโลกครั้งนี้จัดขึ้นตั้งแต่ปลายเดือนพฤศจิกายนถึงกลางเดือนธันวาคม ทำให้เป็นครั้งแรกที่จะไม่จัดในช่วงกลางปี โดยกรอบเวลาของการแข่งขันจะลดลงเหลือ 29 วัน
  
  ในครั้งนี้ถึงแม้ทีมชาติอิตาลีซึ่งเป็นแชมป์ฟุตบอลยุโรปครั้งล่าสุดจะไม่ได้ผ่านเข้ารอบสุดท้ายก็ตาม แต่ทีมชาติดังๆอย่างประเทศ บราซิล (แชมป์โลก5สมัย) ฝรั่งเศส (แชมป์เก่า) สเปน โปรตุเกส เนเธอร์แลนด์ อาร์เจนตินา เยอรมัน อังกฤษ โครเอเชีย เบลเยียม ก็ยังเข้าร่วมการแข่งขันกันอย่างครบถ้วน โดยการแข่งขันรอบแรกจะแบ่งออกเป็น 8 กลุ่ม กลุ่มละ 4 ทีมพบกันหมด เพื่อหาผู้ชนะที่มีคะแนนดีที่สุดจากแต่ล่ะกลุ่ม กลุ่มล่ะ 2 ทีม เพื่อผ่านการคัดเลือกเข้ารอบถัดไป 16 ทีมสุดท้ายและประกบคู่หาผู้ชนะจาก 8 คู่, 4 คู่, 2คู่  ในแต่ล่ะรอบเพื่อหาทีมเข้ารอบถัดไปเรื่อยๆ จนเหลือ 2 ทีมสุดท้ายที่จะเป็นคู่ชิงชนะเลิศ ที่สนามกีฬานานาชาติลูซัยล์ (Lusail Iconic Stadium) ทางตอนเหนือของกรุงโดฮา ประเทศกาตาร์ในวันที่ 18 ธันวาคม 2022   
![worldcup06](https://user-images.githubusercontent.com/77851559/204718059-b0f83c0e-da0a-48ce-a16a-5633e008f040.jpg)




# ขั้นตอนการใส่ข้อมูลตารางการแข่งขันฟุตบอลโลก World Cup2022 เข้าฐานข้อมูล MongoDB:

![program01](https://user-images.githubusercontent.com/77851559/204712061-c245be38-d018-4320-a0c3-bb5e0eab6059.png)
*รูปที่ 1. นำข้อมูลดิบ JSON raw data จากใน link https://fixturedownload.com/results/fifa-world-cup-2022 มาตรวจสอบโครงสร้าง โดยใช้โปรแกรม JSON EDITOR ONLINE https://jsoneditoronline.org/#left=local.masexo แล้ว download file ที่ได้มาเก็บไว้ในเครื่อง Local PC*

![program02](https://user-images.githubusercontent.com/77851559/204712790-516543d3-55af-43d0-ad52-0470acfd75fd.png)
*รูปที่ 2. นำข้อมูลดิบ JSON raw data ที่ได้ มาจัด Format ใหม่ให้พร้อมใช้งานผ่านโปรแกรม Visual Studio Code*

![program03](https://user-images.githubusercontent.com/77851559/204713038-cbfa0a70-e14b-4257-92b3-048fea985948.png)
*รูปที่ 3. ข้อมูล JSON จะอยู่ในรูปแบบพร้อมใช้งาน เพื่อนำเข้าสู่ MongoDB* 

![program04](https://user-images.githubusercontent.com/77851559/204714254-f1d451d4-9820-4f12-a880-dafb22c5bd76.png)
*รูปที่ 4. เขียนชุดคำสั่งบน Jupython Notebook โดยใช้ Python Library os, json และ pymongo เพื่อนำไฟล์ในเครื่อง Local PC เข้าสู่ MongoDB*

![program05](https://user-images.githubusercontent.com/77851559/204714986-d4c9b3a4-bee9-4732-ab7c-722916031c23.png)
*รูปที่ 5. ตรวจสอบข้อมูลใน MongoDB ว่าข้อมูลถูก upload ครบถ้วนถูกต้องตามต้องการหรือไม่*

# ขั้นตอนการเขียน GUI เพื่อทำ CRUD ข้อมูลตารางการแข่งขันฟุตบอลโลก World Cup2022:
เขียนชุดคำสั่งบน Jupython Notebook โดยใช้ Python Library PySimpleGUI กับ pymongo เพื่อสร้าง GUI ให้ user เข้าไปบันทึกข้อมูล โดยมี mode ให้เลือก 8 mode ด้วยกันคือ

1. Create

2. Retrive All

3. Retrive

4. Update

5. Delete All

6. Delete

7. Report

8. Exit

![program06 1](https://user-images.githubusercontent.com/77851559/204768478-08151627-2ac2-472f-a080-db9c3cc080ab.png)

*รูปที่ 6.1 ชุดคำสั่ง GUIหน้าแรก เพื่อเลือก Mode ในการใช้งาน*

![program06 2](https://user-images.githubusercontent.com/77851559/204769019-36201481-de07-4365-ae29-3a62fe3d93c8.png)

*รูปที่ 6.2 ตัวอย่าง GUIหน้าแรก เพื่อเลือก Mode ในการใช้งาน*

![program06 3](https://user-images.githubusercontent.com/77851559/204769333-9574533b-f403-4d84-bc75-e2adf3c6b2dc.png)

*รูปที่ 6.3 ผลลัพธ์กรณีกดเลือกปุ่ม Exit เพื่อเลือกออกจาก Mode ในการใช้งาน*

![program06 4](https://user-images.githubusercontent.com/77851559/204769491-a832c5f0-caee-4de4-852d-f8631f13857c.png)

*รูปที่ 6.4 ตัวอย่าง GUI เพื่อเลือกยืนยันว่าจะออกจาก Mode ในการใช้งาน*


- ในกรณีที่กดปุ่ม Create user จะต้องทำการบันทึกข้อมูลรายละเอียดการแข่งขันตามตัวอย่างดังรูปต่อไปนี้

![program07 1](https://user-images.githubusercontent.com/77851559/204771204-a7b788cf-210e-42e6-83bf-d526dede1dbd.png)

*รูปที่ 7.1 ชุดคำสั่งใน Create Mode*

![program07 2](https://user-images.githubusercontent.com/77851559/204774458-20374a6d-7395-4de4-afbb-ee78b964b0f9.png)

*รูปที่ 7.2 ตัวอย่าง GUI เพื่อสร้างข้อมูลใหม่ใน Create Mode*

![program07 3](https://user-images.githubusercontent.com/77851559/204774646-e92c443c-67f2-4280-9a1d-2cbc1ed79532.png)

*รูปที่ 7.3 หลังจากกด Submit จะได้ตัวอย่าง GUI เพื่อยืนยันข้อมูลที่เพิ่งสร้างไป*

![program07 4](https://user-images.githubusercontent.com/77851559/204774841-457d42ea-0d05-4b90-bb27-c244d6dd474e.png)

*รูปที่ 7.4 ทำการตรวจสอบข้อมูลที่เพิ่งสร้างไปใน Cloud MongoDB*

- ในกรณีที่กดปุ่ม Retrive All user จะได้ข้อมูลทั้งหมดตามตัวอย่างดังรูปต่อไปนี้

![program08 1](https://user-images.githubusercontent.com/77851559/204775608-9cfa60f8-57c0-4cc8-8ec1-2b68343a4dd9.png)

*รูปที่ 8.1 ชุดคำสั่งและผลลัพธ์ใน Retrive All Mode*


- ในกรณีที่กดปุ่ม Retrive user จะต้องใส่ข้อมูลใน selection screen เพื่อทำการค้นหาข้อมูลตามตัวอย่างดังรูปต่อไปนี้

![program09 1](https://user-images.githubusercontent.com/77851559/204777702-1ba20bb1-64c9-4921-bae4-e0dec8146506.png)

*รูปที่ 9.1 ชุดคำสั่งและผลลัพธ์ใน Retrive Mode*

![program09 2](https://user-images.githubusercontent.com/77851559/204777848-7c5693cb-3e89-470f-850f-7f7e55113d02.png)

*รูปที่ 9.2 ตัวอย่าง GUI เพื่อค้นหาข้อมูลใน Retrive Mode*

![program09 3](https://user-images.githubusercontent.com/77851559/204778043-bab71f80-3ba0-4991-9b94-d7d50ef3c57c.png)

*รูปที่ 9.3 หลังจากกด Submit จะได้ตัวอย่าง GUI เพื่อยืนยันข้อมูลที่ต้องการจะค้นหา*

![program09 4](https://user-images.githubusercontent.com/77851559/204778207-0902e579-d200-40be-ba83-b58baedd133a.png)

*รูปที่ 9.4 ผลลัพธ์ของการค้นหาข้อมูล*

- ในกรณีที่กดปุ่ม Update user จะต้องใส่ข้อมูลใน selection screen เพื่อทำการค้นหาข้อมูลที่ต้องการจะ update ตามตัวอย่างดังรูปต่อไปนี้

![program10 1](https://user-images.githubusercontent.com/77851559/204780703-6b5af699-138a-4f0c-b174-11781fda1c9b.png)

*รูปที่ 10.1 ชุดคำสั่งและผลลัพธ์ใน Update Mode*

![program10 2](https://user-images.githubusercontent.com/77851559/204780820-d02178fe-4c4b-40d2-aafc-8b11b9dbfb29.png)

*รูปที่ 10.2 ตัวอย่าง GUI เพื่อค้นหาข้อมูลที่ต้องการจะ update ใน Update Mode*

![program10 3](https://user-images.githubusercontent.com/77851559/204780967-360311ab-33ff-4d11-b032-a906a7194151.png)

*รูปที่ 10.3 ตัวอย่าง GUI เพื่อใส่ข้อมูลค่าใหม่ที่ต้องการจะ update ใน Update Mode*

![program10 4](https://user-images.githubusercontent.com/77851559/204781136-42ab84d8-4d56-4329-9a87-91d94e8e40f4.png)

*รูปที่ 10.4 ตัวอย่าง GUI เพื่อยืนยันการ update ข้อมูล ใน Update Mode*

![program10 5](https://user-images.githubusercontent.com/77851559/204781282-f3b2c45e-8046-4ef8-8b19-95b7e50c5445.png)

*รูปที่ 10.5 ผลลัพธ์ของการค้นหาข้อมูล*

![program10 6](https://user-images.githubusercontent.com/77851559/204781464-5d3e537d-dce0-49d9-8947-450932adc07a.png)

*รูปที่ 10.6 ทำการตรวจสอบข้อมูลที่เพิ่ง updateไป ใน Cloud MongoDB*

- ในกรณีที่กดปุ่ม Delete All user จะเป็นการล้างข้อมูลทั้งหมดในฐานข้อมูล จะต้องระมัดระวังมากก่อนที่จะกดปุ่มนี้ มิฉะนั้นจะเกิดความเสียหายกัับฐานข้อมูลได้ ถ้าเราเผลอกดไปโดยไม่เจตนา ตามตัวอย่างดังรูปต่อไปนี้


![program11 1](https://user-images.githubusercontent.com/77851559/204782810-d7daaf2e-d0a8-4a2c-b3ba-b94059de088d.png)

*รูปที่ 11.1 ชุดคำสั่งใน Delete All Mode*

![program11 2](https://user-images.githubusercontent.com/77851559/204782965-4b006a50-7253-49d4-b9e4-c3ae9b5fd766.png)

*รูปที่ 11.2 ชุดคำสั่งและผลัพธ์ของ Delete All Mode*

![program11 3](https://user-images.githubusercontent.com/77851559/204783163-f425e9e5-584c-4af1-94a6-d78cb6fddc01.png)

*รูปที่ 11.3 ทำการตรวจสอบข้อมูลที่เพิ่งลบไปทั้งหมดไป ใน Cloud MongoDB*

- ในกรณีที่กดปุ่ม Delete user จะต้องเลือกกรอกข้อมูลที่ต้องการจะลบทิ้งโดยการอ้าง Match Number ตามตัวอย่างดังรูปต่อไปนี้

![program12 1](https://user-images.githubusercontent.com/77851559/204784406-4df6d064-2479-4c6e-8a17-5e8f2fcefe1f.png)

*รูปที่ 12.1 ชุดคำสั่งใน Delete Mode*

![program12 2](https://user-images.githubusercontent.com/77851559/204784552-9e4da946-546e-4465-993c-66d59d219b50.png)

*รูปที่ 12.2 ตัวอย่าง GUI เพื่อใส่ Match Number ที่ต้องการจะลบใน Delete Mode*


# ขั้นตอนการออกแบบ Report สรุปผลรวมประตูที่แต่ล่ะกลุ่มทำได้ในรอบแรกของฟุตบอลโลก World Cup 2022:

![program13 1](https://user-images.githubusercontent.com/77851559/204858445-f26b8c84-b44a-4dc4-87d5-df9486e5369e.png)

*รูปที่ 13.1 ชุดคำสั่งใน Report Mode*

![program13 2](https://user-images.githubusercontent.com/77851559/204859215-601c4854-7136-41c0-b1be-fd5b8054a981.png)

*รูปที่ 13.2 ชุดคำสั่งใน Report Mode พร้อมกับผลลัพธ์ (ต่อ)*

![program13 3](https://user-images.githubusercontent.com/77851559/204859566-8b1c267f-34f2-4752-a077-0bd9da3aa89a.png)

*รูปที่ 13.3 กราฟเส้น และ กราฟแท่ง เพื่อสรุปผลรวมประตูที่แต่ล่ะกลุ่มทำได้ในรอบแรกของฟุตบอลโลก World Cup 2022*

# Link Youtube ตัวอย่างการใช้งาน Application:



# บทสรุป:

สำหรับตัวอย่างนี้เป็นเพียงการนำเครื่องมือ Python มาพัฒนา Basic Application สำหรับฐานข้อมูลประเภท NoSQL บน MongoDB เพื่อบันทึกข้อมูลฟุตบอลโลก World Cup 2022 และออกรายงานพื้นฐานง่ายๆ  ซึ่งในครั้งนี้ต้องขอขอบคุณอาจารย์ ผศ.ดร.เอกรัฐ รัฐกาญจน์ ผู้อำนวยการหลักสูตรการวิเคราะห์ข้อมูลและวิทยาการข้อมูล คณะสถิติประยุกต์ สถาบันบัณฑิตพัฒนบริหารศาสตร์ ที่ช่วยเหลือให้คำแนะนำ ทำให้ผู้เขียนสามารถนำความรู้พื้นฐานนี้ นำไปต่อยอดองค์ความรู้ของการทำ Data Analytics Application อื่นๆในอนาคตได้มากขึ้นไปอีกครับ

![worldcup03](https://user-images.githubusercontent.com/77851559/204710240-2e912d1a-6f35-4904-afbd-b89f9293e1ff.jpg)
