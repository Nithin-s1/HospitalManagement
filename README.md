# 🏥 Hospital Management System

A modern, full-scale Hospital Management System built with a monorepo architecture using Turborepo. This project provides a comprehensive solution for healthcare management with web, mobile, and API applications.

## 🏗️ Architecture

This monorepo contains:

### Apps
- **`apps/api`** - Express.js + TypeScript REST API with health check and extensible folder structure
- **`apps/web`** - React + TypeScript + Vite web application
- **`apps/mobile`** - React Native + TypeScript + Expo mobile application

### Packages
- **`packages/config`** - Shared ESLint, Prettier, and TypeScript configurations
- **`packages/types`** - Shared TypeScript types (User, Patient, Appointment, etc.)
- **`packages/utils`** - Shared utility functions (date formatting, validation, etc.)
- **`packages/ui`** - Shared UI component library for web and mobile
- **`packages/api-client`** - Typed API client for consuming the backend API

## 🚀 Getting Started

### Prerequisites

- Node.js >= 18.0.0
- npm >= 10.0.0

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Nithin-s1/HospitalManagement.git
cd HospitalManagement
```

2. Install dependencies:
```bash
npm install
```

3. Build all packages:
```bash
npm run build
```

## 📦 Available Scripts

### Root Level

- `npm run dev` - Start development servers for all apps
- `npm run build` - Build all apps and packages
- `npm run lint` - Lint all apps and packages
- `npm run test` - Run tests for all apps and packages
- `npm run clean` - Clean all build artifacts and node_modules
- `npm run format` - Format all code with Prettier

### Individual Apps

#### API (apps/api)
```bash
cd apps/api
npm run dev      # Start development server on port 3001
npm run build    # Build for production
npm run start    # Start production server
```

#### Web (apps/web)
```bash
cd apps/web
npm run dev      # Start development server on port 3000
npm run build    # Build for production
npm run preview  # Preview production build
```

#### Mobile (apps/mobile)
```bash
cd apps/mobile
npm run dev      # Start Expo development server
npm run ios      # Run on iOS simulator
npm run android  # Run on Android emulator
npm run web      # Run on web browser
```

## 🔧 Development

### Running the Full Stack

1. **Start the API server:**
```bash
cd apps/api
npm run dev
```
The API will be available at `http://localhost:3001`

2. **Start the web app:**
```bash
cd apps/web
npm run dev
```
The web app will be available at `http://localhost:3000`

3. **Start the mobile app:**
```bash
cd apps/mobile
npm run dev
```
Follow the Expo CLI instructions to run on a device or simulator.

### API Endpoints

- `GET /` - API information
- `GET /health` - Health check endpoint

## 📁 Project Structure

```
hospital-management/
├── apps/
│   ├── api/              # Express API
│   │   └── src/
│   │       ├── config/   # Configuration files
│   │       ├── controllers/ # Request handlers
│   │       ├── routes/   # API routes
│   │       └── services/ # Business logic
│   ├── web/              # React web app
│   │   └── src/
│   └── mobile/           # React Native app
│       └── src/
├── packages/
│   ├── config/           # Shared configs
│   ├── types/            # Shared TypeScript types
│   ├── utils/            # Shared utilities
│   ├── ui/               # Shared UI components
│   └── api-client/       # API client library
├── package.json          # Root package.json with workspaces
├── turbo.json           # Turborepo configuration
└── tsconfig.json        # Base TypeScript config
```

## 🛠️ Tech Stack

- **Frontend:** React, TypeScript, Vite
- **Mobile:** React Native, Expo, TypeScript
- **Backend:** Node.js, Express, TypeScript
- **Monorepo:** Turborepo
- **Build Tools:** TypeScript, Vite, tsx
- **Code Quality:** ESLint, Prettier

## 🔐 Environment Variables

### API (apps/api/.env)
```
PORT=3001
NODE_ENV=development
API_VERSION=v1
```

## 📝 Shared Types

The `@hospital/types` package provides shared TypeScript types:

- **UserRole** - Enum for user roles (ADMIN, DOCTOR, NURSE, PATIENT, RECEPTIONIST)
- **User** - User entity interface
- **Patient** - Patient entity interface
- **Appointment** - Appointment entity interface with status enum

## 🎨 Shared UI Components

The `@hospital/ui` package provides reusable components:

- **Button** - Customizable button component with variants (primary, secondary, danger)

## 🧰 Utility Functions

The `@hospital/utils` package provides helpful utilities:

- **formatDate** - Format dates to readable strings
- **calculateAge** - Calculate age from date of birth
- **isPastDate** - Check if a date is in the past
- **isValidEmail** - Validate email format
- **isValidPhone** - Validate phone number format

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Nithin S - [Nithin-s1](https://github.com/Nithin-s1)

## 🙏 Acknowledgments

- Built with Turborepo for efficient monorepo management
- Uses modern React patterns and TypeScript for type safety
- Follows best practices for scalable application architecture