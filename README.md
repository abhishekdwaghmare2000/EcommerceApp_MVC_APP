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
<img width="1920" height="951" alt="User Roles of Application" src="https://github.com/user-attachments/assets/374497ac-af19-45f2-8fd8-91cabf020ccd" />
<img width="1920" height="978" alt="Register Page" src="https://github.com/user-attachments/assets/8077764d-9d5b-4f6e-b073-6790fbe80221" />
<img width="1917" height="982" alt="Product Page" src="https://github.com/user-attachments/assets/384ce87b-6de9-4687-a449-310b9fc93d9d" />
<img width="1920" height="963" alt="Login Page" src="https://github.com/user-attachments/assets/9c4d35d9-bd47-43a0-a35e-274f76b2024a" />
<img width="1920" height="961" alt="Home Page" src="https://github.com/user-attachments/assets/12bcd4cd-73fb-4621-a153-8138d232cdcc" />
<img width="1920" height="974" alt="Company Page" src="https://github.com/user-attachments/assets/f41b6ab0-66d4-4f9b-a8c0-6b711546e771" />
<img width="1907" height="963" alt="Category Page" src="https://github.com/user-attachments/assets/e89b2bd3-1dcc-4cb2-9845-0990f871e1c5" />




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
