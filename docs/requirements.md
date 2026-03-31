# 📋 Requirements

This document specifies the functional requirements, non-functional requirements, and architectural constraints for the Wise Route system — a route optimization platform for delivery logistics. Each requirement is uniquely identified and classified by criticality in the traceability matrix at the end of this document.

---

## ⚙️ Functional Requirements

FR01 — The system shall support the full user lifecycle management: registration, retrieval, update, and account deletion.

FR02 — The system shall authenticate the user to allow access to the platform.

FR03 — The system shall support vehicle management (cars, motorcycles, or trucks).

FR04 — The system shall allow the registration of delivery points, where the user provides a name, address or coordinates, and the cargo weight for each point. The system shall geocode the provided address and display the marker on the map in real time.

FR05 — The system shall compute an optimized route that departs from the starting point, visits all points while respecting the vehicle capacity, and returns to the starting point, minimizing the total distance.

FR06 — The system shall display the optimized route as a polyline on the map, with markers numbered in the visit sequence.

FR07 — The system shall display, after optimization, the route metrics: total distance, distance saved compared to the naive route, stop sequence, and accumulated load per leg.

FR08 — The system shall maintain a history of computed routes, recording date, number of points, and key metrics.

FR09 — The system shall allow the user to save a set of points and the result as a named scenario, which can be reloaded later.

---

## 🛡️ Non-functional Requirements

NFR01 — The system shall return the optimization result for up to 20 points in less than 5 seconds.

NFR02 — The system shall provide a functional desktop interface that is responsive for mobile devices.

NFR03 — The system shall store passwords using bcrypt hashing, protect API routes with JWT, and not expose environment variables on the frontend.

---

## 🏗️ Architectural Constraints

AR01 — The system shall be composed of independent microservices (API, optimization engine, and optionally geocoding), each with its own runtime environment, orchestrated via Docker Compose.

AR02 — The system shall adopt an event-driven architecture for the optimization flow: the API shall publish an event upon receiving a request, and the optimization engine shall consume that event, process the optimization, and publish the response asynchronously.

AR03 — The system shall use RabbitMQ as the primary messaging mechanism for inter-service communication, allowing HTTP communication only in specific and duly justified cases.

AR04 — The system shall use an intelligent caching layer to reduce redundant calls and improve response time.

---

### 📊 Requirements Traceability Matrix

| ID    | Description                                     | Criticality      |
| ----- | ----------------------------------------------- | ---------------- |
| FR01  | User lifecycle management (CRUD)                | 🔴 High          |
| FR02  | User authentication                             | 🔴 High          |
| FR03  | Vehicle management                              | 🔴 High          |
| FR04  | Delivery point registration and geocoding       | 🔴 High          |
| FR05  | Optimized route calculation                     | 🔴 High          |
| FR06  | Route visualization on map                      | 🟡 Medium        |
| FR07  | Route metrics display                           | 🟡 Medium        |
| FR08  | Route history                                   | 🟡 Medium        |
| FR09  | Scenario save and reload                        | 🟡 Medium        |
| NFR01 | Optimization response under 5 seconds           | 🔴 High          |
| NFR02 | Responsive interface (desktop and mobile)       | 🟢 Low           |
| NFR03 | Password hashing, JWT protection, env security  | 🔴 High          |
| AR01  | Independent microservices with Docker Compose   | 🔴 High          |
| AR02  | Event-driven architecture for optimization flow | 🔴 High          |
| AR03  | RabbitMQ as primary messaging mechanism         | 🔴 High          |
| AR04  | Intelligent caching layer                       | 🟡 Medium        |
