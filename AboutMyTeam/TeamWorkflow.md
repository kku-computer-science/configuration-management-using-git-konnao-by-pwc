# Team Workflow  
Configuration Management using Git – Group Project

เอกสารฉบับนี้จัดทำขึ้นเพื่ออธิบายโครงสร้างของทีม  
การแบ่งหน้าที่ความรับผิดชอบ และกระบวนการทำงานร่วมกัน  
โดยใช้ Git และ GitHub เป็นเครื่องมือหลักในการควบคุมเวอร์ชัน (Version Control)

---

## 1. รายชื่อสมาชิกในทีม (Team Members)

| ลำดับ | ชื่อ - นามสกุล       | รหัสนักศึกษา   | หน้าที่รับผิดชอบ              |
|------|--------------------|-------------|----------------------------|
| 1 | ณิชกานต์ จูประพัทธศรี     | 663380209-7 | Bubble Sort Algorithm      |
| 2 | ณัฐพงศ์ เหลื่อมล้ำ        | 663380208-9 | Quick Sort Algorithm       |
| 3 | นายนราวิชญ์ ศิริพล       | 663380214-4 | Sort Manager & Integration |

---

## 2. เป้าหมายของโปรเจกต์ (Project Objective)

- พัฒนาโปรแกรมที่สามารถเลือกอัลกอริทึมการเรียงลำดับได้จากผู้ใช้  
- รองรับอัลกอริทึมอย่างน้อย 2 แบบ ได้แก่  
  - Bubble Sort  
  - Quick Sort  
- ใช้ Git และ GitHub เพื่อบริหารจัดการซอร์สโค้ดร่วมกันแบบเป็นทีม  
- ฝึกการทำงานด้วย Branch, Commit, Merge และ Pull Request  
- รวมซอร์สโค้ดทั้งหมดเข้าสู่ branch `main` ก่อนส่งงาน  

---

## 3. โครงสร้าง Repository (Repository Structure)

```text
configuration-management-using-git-konnao-by-pwc/
│
├── AboutMyTeam/
│   └── TeamWorkflow.md
│
├── Project/
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   └── sort_manager.py
│
└── README.md
````

---

## 4. การแบ่งงานและความรับผิดชอบ (Responsibility)

### สมาชิกที่ 1 : ณิชกานต์ จูประพัทธศรี (6633802097)

* วางโครงสร้างไฟล์เบื้องต้น
* พัฒนาอัลกอริทึม Bubble Sort
* สร้างไฟล์ `bubble_sort.py`
* ทดสอบความถูกต้องของอัลกอริทึม
* Commit และ Push งานบน branch `Nichagan_2097`

### สมาชิกที่ 2 : ณัฐพงศ์ เหลื่อมล้ำ (6633802089)

* พัฒนาอัลกอริทึม Quick Sort
* สร้างไฟล์ `quick_sort.py`
* ทดสอบความถูกต้องของอัลกอริทึม
* Commit และ Push งานบน branch `Natthapong_2089`

### สมาชิกที่ 3 : นายนราวิชญ์ ศิริพล (6633802144)

* พัฒนาไฟล์ `sort_manager.py` สำหรับรวมอัลกอริทึมทั้งหมด
* ตรวจสอบความถูกต้องของโค้ดทั้งหมด
* เตรียม Repository ให้พร้อมสำหรับการส่งงาน
* Commit และ Push งานบน branch `Narawit_2144`

---

## 5. กระบวนการทำงานร่วมกัน (Working Process)

### 5.1 ขั้นตอนเริ่มต้นการทำงาน

```bash
git clone <Team Repository URL>
git checkout <your-branch-name>
git branch
```

---

### 5.2 ขั้นตอนการทำงานมาตรฐานของสมาชิก

```bash
git pull origin main
git status
git add .
git commit -m "Add bubble sort implementation"
git push origin <your-branch-name>
```

---

## 6. การรวมงานเข้าสู่ main (Merge Process)

```bash
git checkout main
git pull origin main
```

จากนั้นทำการ Merge ผ่าน Pull Request บน GitHub

---

## 7. การจัดการเมื่อเกิด Merge Conflict

```bash
git add .
git commit -m "Resolve merge conflict"
```

---

## 8. ช่องทางการสื่อสารภายในทีม

* Line
* Discord
* Messenger

---

## 9. มาตรฐานการตั้งชื่อ Commit (Commit Message Convention)

* ใช้ภาษาอังกฤษ
* ขึ้นต้นด้วยคำกริยา เช่น

  * Add
  * Update
  * Fix
  * Refactor

---

## 10. สรุปแนวทางการทำงานของทีม

* สมาชิกทุกคนต้องทำงานบน branch ของตนเองเท่านั้น
* ห้าม push เข้า branch `main` โดยตรง
* ต้องใช้ Pull Request ก่อน merge ทุกครั้ง
* มีการตรวจสอบโค้ดก่อนรวมเข้าสู่ main
* ตรวจสอบโครงสร้างไฟล์ให้เป็นไปตามที่กำหนด

```


