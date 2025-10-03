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

> ⚠️ Note: In your implementation, categories management UI is only shown to **Admin**.  

---

## 🖼️ Screenshots

Use these images (already in your repo) to illustrate your app:

**Login Page**  
![Login Page](./Login%20Page.png)  

**Category Management (Admin Only)**  
![Category Page](./Category%20Page.png)  

---

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
- .NET SDK (6, 7 or the version your project targets)  
- SQL Server or LocalDB  
- IDE (Visual Studio, Rider, or VS Code)  
- EF Core CLI tools (optional but helpful)  

### Steps

1. **Clone the repository**  
   ```bash
   git clone https://github.com/abhishekdwaghmare2000/EcommerceApp_MVC_APP.git
   cd EcommerceApp_MVC_APP
