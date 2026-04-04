# 📋 Requirements

## Overview

This document specifies the functional requirements and non-functional requirements for the Wise Route system — a route optimization platform for delivery logistics. Each requirement is uniquely identified and classified by criticality in the traceability matrix at the end of this document.

---

## ⚙️ Functional Requirements

FR01 — The system shall support the full user lifecycle management: registration, retrieval, update, and account deletion.

FR02 — The system shall authenticate the user to allow access to the platform.

FR03 — The system shall support vehicle management (cars, motorcycles, or trucks).

FR04 — The system shall allow the registration of delivery points, where the user provides a name, address or coordinates, and the cargo weight for each point. The system shall geocode the provided address and display the marker on the map in real time.

FR05 — The system shall compute an optimized route based on a defined set of input parameters (including starting point, delivery points, and vehicle constraints), generating a solution that departs from the starting point, visits all points while respecting the vehicle capacity, and returns to the starting point, minimizing the total distance.

FR06 — The system shall display the optimized route as a polyline on the map, with markers numbered according to the visit sequence.

FR07 — The system shall display, after optimization, route metrics including total distance, distance saved compared to the naive route, stop sequence, accumulated load per leg, and execution-related metrics such as processing time and optimization status.

FR08 — The system shall maintain a history of computed routes, recording the input characteristics (such as number of points), execution timestamp, and resulting key metrics.

FR09 — The system shall allow the user to save a set of points and the result as a named scenario, which can be reloaded later.

FR10 — The system shall record and expose optimization execution information, including processing time, execution status, and timestamps, for each computed route.

---

## 🛡️ Non-functional Requirements

NFR01 — The system shall return the optimization result for up to 20 points in less than 5 seconds.

NFR02 — The system shall provide a functional desktop interface that is responsive for mobile devices.

NFR03 — The system shall store passwords using bcrypt hashing, protect API routes with JWT, and never expose secrets or credentials (e.g., API keys, database credentials, private tokens) to the client. Only a whitelist of explicitly designated public configuration values may be included in the frontend bundle; all secrets shall remain server-side.

NFR04 — The system shall process long-running operations such as route optimization asynchronously, with core services communicating through a decoupled messaging mechanism.

NFR05 — The system shall be horizontally scalable and support independent deployment of its core components.

NFR06 — The system shall minimize redundant external API calls through caching and optimize overall response time.

---

### 📊 Requirements Traceability Matrix

| ID    | Description                                                  | Criticality |
| ----- | ------------------------------------------------------------ | ----------- |
| FR01  | User lifecycle management (CRUD)                             | 🔴 High     |
| FR02  | User authentication                                          | 🔴 High     |
| FR03  | Vehicle management                                           | 🔴 High     |
| FR04  | Delivery point registration and geocoding                    | 🔴 High     |
| FR05  | Optimized route calculation                                  | 🔴 High     |
| FR06  | Route visualization on map                                   | 🟡 Medium   |
| FR07  | Route metrics display                                        | 🟡 Medium   |
| FR08  | Route history                                                | 🟡 Medium   |
| FR09  | Scenario save and reload                                     | 🟡 Medium   |
| FR10  | Optimization execution info                                  | 🔴 High     |
| NFR01 | Optimization response under 5 seconds                        | 🔴 High     |
| NFR02 | Responsive interface (desktop and mobile)                    | 🟢 Low      |
| NFR03 | Password hashing, JWT protection, env security               | 🔴 High     |
| NFR04 | Asynchronous processing with decoupled messaging             | 🔴 High     |
| NFR05 | Horizontal scalability and independent component deployment  | 🔴 High     |
| NFR06 | Caching to minimize redundant calls and optimize performance | 🔴 High     |
