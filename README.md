# 🏥 Smart Porter — โรงพยาบาลชุมชน
**ระบบเรียกเปลอัจฉริยะ (Mae Taeng Community Hospital)**

> ระบบเรียกเปลแบบ Grab สำหรับโรงพยาบาลชุมชน รองรับ PWA — ติดตั้งบนมือถือได้โดยไม่ต้องผ่าน App Store

---

## 📲 การ Deploy บน GitHub Pages (ใช้งานฟรี!)

### ขั้นตอนที่ 1 — สร้าง GitHub Repository
1. เข้า [github.com](https://github.com) → สร้างบัญชีถ้ายังไม่มี
2. คลิก **New Repository**
3. ตั้งชื่อ: `smart-porter` (หรืออะไรก็ได้)
4. เลือก **Public**
5. คลิก **Create repository**

### ขั้นตอนที่ 2 — Upload ไฟล์
```
วิธีง่ายที่สุด: ลาก & วางไฟล์ทั้งหมดลงใน GitHub
```
1. เปิด repository ที่สร้างไว้
2. คลิก **uploading an existing file**
3. ลากโฟลเดอร์ `porter-pwa` ทั้งหมดขึ้น
4. คลิก **Commit changes**

โครงสร้างไฟล์ที่ต้องมี:
```
smart-porter/
├── index.html        ← แอปหลัก
├── manifest.json     ← PWA manifest
├── sw.js             ← Service Worker (ทำให้ใช้ offline ได้)
└── icons/
    ├── icon-72.png
    ├── icon-96.png
    ├── icon-128.png
    ├── icon-144.png
    ├── icon-152.png
    ├── icon-192.png
    ├── icon-384.png
    └── icon-512.png
```

### ขั้นตอนที่ 3 — เปิด GitHub Pages
1. ใน repository → คลิก **Settings** (แถบด้านบน)
2. เลื่อนลงหา **Pages** (เมนูซ้าย)
3. ใต้ Source เลือก **Deploy from a branch**
4. Branch: เลือก `main` → Folder: `/ (root)`
5. คลิก **Save**
6. รอประมาณ 1-3 นาที แล้วได้ URL:

```
https://[username].github.io/smart-porter/
```

**ตัวอย่าง URL จริง:**
```
https://maetaeng-hospital.github.io/smart-porter/
```

---

## 📱 ติดตั้งเป็นแอปบนมือถือ (PWA)

### Android (แนะนำ)
1. เปิด Chrome บนมือถือ
2. เข้าไปที่ URL ของระบบ
3. Chrome จะถามว่า **"ติดตั้งแอปบนหน้าจอหลัก?"** → กด **ติดตั้ง**
4. แอปจะปรากฏบน Home Screen เหมือนแอปปกติ ✅

> หากไม่มี popup: กดเมนู ⋮ → "เพิ่มลงในหน้าจอหลัก"

### iPhone/iPad (iOS 16.4+)
1. เปิด Safari
2. เข้าไปที่ URL
3. กดปุ่ม **Share** (กล่องมีลูกศรขึ้น)
4. เลือก **"Add to Home Screen"**
5. กด **Add** ✅

---

## 🛒 เผยแพร่บน Google Play Store

ใช้ **PWABuilder** (ฟรี, ไม่ต้องเขียนโค้ด Android):

1. เข้า [pwabuilder.com](https://www.pwabuilder.com)
2. ใส่ URL ของ GitHub Pages
3. คลิก **Package for Stores**
4. เลือก **Android** → Download `.apk` หรือ `.aab`
5. สร้าง Google Play Developer Account ($25 ครั้งเดียว)
6. Upload ที่ [play.google.com/console](https://play.google.com/console)

> **ใช้ TWA (Trusted Web Activity)** — Google รับรอง approach นี้แล้ว

---

## 🛒 เผยแพร่บน Apple App Store

1. เข้า [pwabuilder.com](https://www.pwabuilder.com) → เลือก **iOS**
2. ต้องการ Mac + Xcode (หรือ Mac Cloud service)
3. Apple Developer Account ($99/ปี)
4. Submit ผ่าน Xcode → App Store Connect

> **แนะนำ**: เริ่มจาก Android + GitHub Pages ก่อน ใช้ได้ฟรี และครอบคลุมมือถือเจ้าหน้าที่ส่วนใหญ่

---

## 🔧 Custom Domain (ถ้าต้องการ URL สวย)

ถ้าโรงพยาบาลมี Domain เช่น `maetaeng.go.th`:
1. GitHub Pages Settings → Custom domain → ใส่ `porter.maetaeng.go.th`
2. ที่ DNS Provider: เพิ่ม CNAME record ชี้ไปที่ `[username].github.io`

---

## ✅ Checklist ก่อน Go-Live

- [ ] ทดสอบบนมือถือ Android + iPhone
- [ ] ทดสอบ WiFi ทุกชั้น/ทุกแผนกในรพ.
- [ ] ทดสอบโหมด Offline (ดับ WiFi แล้วเปิดแอป)
- [ ] เจ้าหน้าที่เปลทุกคน Login ทดสอบ
- [ ] ทดสอบเสียงเตือนบนมือถือหลายยี่ห้อ
- [ ] แจ้ง IT ขอ whitelist URL ใน Firewall

---

## 🗺️ Roadmap (พัฒนาต่อ)

| Phase | Feature | เทคโนโลยี |
|-------|---------|-----------|
| ✅ v1.0 | UI/UX พื้นฐาน, PWA | HTML+JS |
| 🔜 v1.5 | Real-time sync ระหว่างผู้ใช้ | Firebase Realtime DB |
| 🔜 v2.0 | AI Matching, Heatmap | Node.js + ML |
| 🔜 v2.5 | แผนที่ภายในอาคาร | Indoor positioning |
| 🔜 v3.0 | ระบบ Login, สิทธิ์ผู้ใช้ | Auth + Database |

---

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **PWA**: Web App Manifest + Service Worker
- **Hosting**: GitHub Pages (ฟรี, HTTPS อัตโนมัติ)
- **Notifications**: Web Push API
- **Offline**: Cache API + Service Worker

---

*พัฒนาสำหรับ: โรงพยาบาลชุมชนแม่แตง จ.เชียงใหม่*  
*Version: 1.0.0 | License: MIT*
