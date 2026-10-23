# Module 02: Server-side Programming with Node.js

![Node.js 20](https://img.shields.io/badge/Node.js-20_LTS-339933?logo=nodedotjs&logoColor=white) ![Express](https://img.shields.io/badge/Express-4.x-000000?logo=express&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-Mongoose_8-47A248?logo=mongodb&logoColor=white) ![npm](https://img.shields.io/badge/npm-10-CB3837?logo=npm&logoColor=white) ![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=black)

> Term 4 (HDSE) · 12 sessions × 2 hours · [⬅ Term Home](../README.md)

This module teaches you to write the backend of modern web applications with Node.js. You start with how servers work and how Node runs JavaScript outside the browser, then learn modules, file uploads, email, Express, asynchronous programming and REST API design. You finish by connecting to MongoDB, adding AI features, securing APIs with JWT and deploying real applications from GitHub to Render.

## 🎯 What You Will Learn

- Explain client-server architecture and the Node.js event-driven model
- Use core, local and third-party modules and manage packages with npm
- Handle query strings, send emails and accept file uploads
- Build web servers and APIs with Express middleware and routers
- Write correct asynchronous code with Promises and async/await
- Design RESTful APIs with proper methods and status codes
- Store data in MongoDB with Mongoose and integrate AI services safely
- Secure APIs with hashed passwords and JWT, and deploy to Render

## 📋 Prerequisites

- Modern JavaScript (ES6+): functions, arrays, objects, destructuring, modules, Promises
- Basic understanding of HTTP and JSON
- Git and GitHub basics
- Helpful: the React module of this term (for full-stack practice)

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| Node.js 20 LTS | runtime for all examples | [https://nodejs.org/en/download](https://nodejs.org/en/download) |
| Visual Studio Code | editor (add the REST Client extension) | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| MongoDB Community Server | local database | [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community) |
| MongoDB Compass | visual database browser | [https://www.mongodb.com/products/tools/compass](https://www.mongodb.com/products/tools/compass) |
| Postman | API testing | [https://www.postman.com/downloads/](https://www.postman.com/downloads/) |
| Git | version control | [https://git-scm.com/downloads](https://git-scm.com/downloads) |

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Client-Server Architecture and Introduction to Node.js | [Open notes](./Session-01-Client-Server-Architecture-and-Introduction-to-Nodejs/README.md) |
| 02 | Node.js Architecture and Programming Basics | [Open notes](./Session-02-Nodejs-Architecture-and-Programming-Basics/README.md) |
| 03 | Modules, Packages and Built-in Modules | [Open notes](./Session-03-Modules-Packages-and-Built-in-Modules/README.md) |
| 04 | Query Strings, Email, File Uploads and Local Modules | [Open notes](./Session-04-Querystring-Email-File-Uploads-and-Local-Modules/README.md) |
| 05 | Practice Lab: Node.js Fundamentals | [Open notes](./Session-05-Practice-Lab-Nodejs-Fundamentals/README.md) |
| 06 | The Express.js Framework | [Open notes](./Session-06-Expressjs-Framework/README.md) |
| 07 | Asynchronous Programming and the Event Loop | [Open notes](./Session-07-Asynchronous-Programming-and-the-Event-Loop/README.md) |
| 08 | RESTful and HTTP APIs | [Open notes](./Session-08-RESTful-and-HTTP-APIs/README.md) |
| 09 | Node.js with MongoDB and Integrating AI Capabilities | [Open notes](./Session-09-MongoDB-CRUD-APIs-and-AI-Integration/README.md) |
| 10 | Node.js in Action: Cloud App with AI Recommendations | [Open notes](./Session-10-Nodejs-in-Action-Cloud-App-with-AI-Recommendations/README.md) |
| 11 | Node.js in Action: Full Application Development and Deployment | [Open notes](./Session-11-Nodejs-in-Action-Full-Application-and-Deployment/README.md) |
| 12 | Practice Lab: Express, Async, APIs, MongoDB and Deployment | [Open notes](./Session-12-Practice-Lab-Express-APIs-and-Deployment/README.md) |

## 🚀 Module Mini-Project

**Campus Events Platform API**

1. Express REST API with layered folders (routes, controllers, models, middleware).
2. Users register/login (bcrypt + JWT); organisers create events, students book seats without overbooking.
3. Upload an event banner image (Multer, size/type checks) and send a booking confirmation email (Nodemailer/Ethereal).
4. An AI endpoint that writes a short event description, with output validation and a fallback.
5. Automated tests with `node --test`, a `requests.http` file and API documentation in the README.
6. Code on GitHub, deployed on Render with MongoDB Atlas.

## 🔗 Resources (official documentation)

- [Node.js documentation](https://nodejs.org/docs/latest-v20.x/api/)
- [Node.js event loop guide](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [Express documentation](https://expressjs.com/)
- [Mongoose documentation](https://mongoosejs.com/docs/)
- [MongoDB Node.js driver](https://www.mongodb.com/docs/drivers/node/current/)
- [Nodemailer](https://nodemailer.com/)
- [Render: deploy a Node Express app](https://render.com/docs/deploy-node-express-app)
- [OpenAI API reference](https://platform.openai.com/docs/api-reference)

---

[⬅ Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
