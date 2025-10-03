# 🛍️ EcommerceApp_MVC_APP

A multi-role eCommerce web application built with **ASP.NET Core MVC**.  
This app demonstrates role-based authorization, category/product management, and business logic such as deferred payments for companies.

---

## 🎯 Features & Highlights

- Authentication & Authorization with **ASP.NET Core Identity**  
- Four distinct roles: **Admin**, **Customer**, **Employee**, **Company**  
- Role-based UI and access control  
- CRUD operations on **categories** and **products**  
- **Company order flow**: after placing an order, companies have **30 days** to make payment  
- Employee accounts with registration, login, and limited access pages  
- Clean UI with Razor views + Bootstrap  

---

## 👥 Roles & Responsibilities

| Role       | Access / Permissions                                                                 |
|------------|-----------------------------------------------------------------------------------------|
| **Admin**    | Full control: manage categories, products, users, roles, etc.                           |
| **Customer** | Browse products, place orders; **no access** to category/product admin features         |
| **Company**  | Place orders with special logic: has 30 days to complete payment                        |
| **Employee** | Can login/register; access to pages like Home, Category, Product, and Company pages     |

---

## 🖼️ Screenshots
<img width="1920" height="1080" alt="User Roles of Application" src="https://github.com/user-attachments/assets/c3b658ec-f4a6-475c-8819-78de0e29ad19" />

<img width="1920" height="1080" alt="Register Page" src="https://github.com/user-attachments/assets/6e8d0889-ee79-4926-844a-b179bee7928f" />

<img width="1920" height="1080" alt="Product Page" src="https://github.com/user-attachments/assets/7d5d8eef-ac4a-4e38-8cc4-1978ac790fd5" />

<img width="1920" height="1080" alt="Login Page" src="https://github.com/user-attachments/assets/f511c61a-b926-47c6-9004-af5fd4b57955" />

<img width="1920" height="1080" alt="Home Page" src="https://github.com/user-attachments/assets/0d168d02-5850-48e0-9d03-7d4a017e2eec" />

<img width="1920" height="1080" alt="Company Page" src="https://github.com/user-attachments/assets/d8c7d195-59f0-4a64-9883-ea550890124f" />

<img width="1920" height="1080" alt="Category Page" src="https://github.com/user-attachments/assets/93246827-cdad-4ce3-8c1d-58d5231539e8" />



## 🛠️ Tech Stack

| Layer       | Technology / Frameworks                                      |
|-------------|---------------------------------------------------------------|
| Backend     | ASP.NET Core MVC, C#                                          |
| Frontend    | Razor Views, Bootstrap, HTML, CSS                             |
| Database    | SQL Server + Entity Framework Core (Code First / Migrations) |
| Auth / Authz| ASP.NET Core Identity                                         |
| Tools       | Visual Studio, .NET CLI, EF Core migrations                  |

---

## 🚀 Setup & Running Locally

### Prerequisites
- .NET SDK  
- SQL Server or LocalDB  
- IDE (Visual Studio, Rider, or VS Code)  
- EF Core CLI tools 

### Steps

1. **Clone the repository**  
   ```bash
   git clone https://github.com/abhishekdwaghmare2000/EcommerceApp_MVC_APP.git
   cd EcommerceApp_MVC_APP
