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



# ขั้นตอนการออกแบบ Report สรุปผลการแข่งขันฟุตบอลโลก World Cup2022:



# Link Youtube ขั้นตอนการใช้งาน Application:


จากการนำเครื่องมือ Python มาพัฒนา Basic Application สำหรับฐานข้อมูลประเภท NoSQL บน MongoDB เพื่อบันทึกข้อมูลฟุตบอลโลก World Cup 2022 และออกรายงานครั้งนี้ ต้องขอขอบคุณอาจารย์ ผศ.ดร.เอกรัฐ รัฐกาญจน์ ผู้อำนวยการหลักสูตรการวิเคราะห์ข้อมูลและวิทยาการข้อมูล คณะสถิติประยุกต์ สถาบันบัณฑิตพัฒนบริหารศาสตร์ ที่ช่วยเหลือให้คำแนะนำเพื่อไปต่อยอดองค์ความรู้ของการทำ Data Analytics Application ครั้งนี้ด้วยครับ

![worldcup03](https://user-images.githubusercontent.com/77851559/204710240-2e912d1a-6f35-4904-afbd-b89f9293e1ff.jpg)
