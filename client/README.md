# PathPilot AI - Frontend

React frontend for the PathPilot AI career pathway generator.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd client
npm install
```

### 2. Run Development Server

```bash
npm run dev
```

The app will be available at: http://localhost:5173

## 📁 Project Structure

```
client/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Navbar.jsx       # Navigation bar
│   │   ├── PathwayForm.jsx  # Pathway generation form
│   │   ├── WeekCard.jsx     # Weekly plan display
│   │   ├── ResourceCard.jsx # Learning resource card
│   │   ├── ProjectCard.jsx  # Guided project card
│   │   └── ProgressBar.jsx  # Progress tracking bar
│   ├── pages/               # Main pages
│   │   ├── HomePage.jsx     # Landing page
│   │   ├── GeneratePage.jsx # Pathway generation page
│   │   └── PathwayPage.jsx  # Pathway display page
│   ├── utils/               # Utility functions
│   │   ├── api.js           # API communication
│   │   └── localStorage.js  # LocalStorage helpers
│   ├── App.jsx              # Main app with routing
│   ├── main.jsx             # App entry point
│   └── index.css            # Global styles
├── public/                  # Static assets
├── package.json             # Dependencies
└── vite.config.js          # Vite configuration
```

## 🔗 Pages & Routes

- **/** - Home page (landing page)
- **/generate** - Generate pathway form
- **/pathway** - View generated pathway

## 🛠️ Technologies

- **React 19** - UI library
- **Vite** - Build tool and dev server
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client for API calls
- **Tailwind CSS** - Utility-first CSS framework

## 📡 API Integration

The frontend connects to the FastAPI backend at `http://localhost:8000`.

Make sure the backend is running before using the app:

```bash
cd ../server
python main.py
```

## 💾 Data Storage

Currently uses **localStorage** for storing generated pathways. No database connection yet.

## 🎨 Styling

Uses Tailwind CSS with a dark theme:
- Primary colors: Blue (#3B82F6) and Purple (#9333EA)
- Background: Slate shades (950, 900, 800)
- Accent colors for different resource types

## 🔧 Available Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

## 📝 Key Features

### HomePage
- Hero section with CTA buttons
- Feature highlights
- "How it works" section
- Conditional "View My Pathway" button if pathway exists

### GeneratePage
- Comprehensive form with validation
- Career goal input
- Skill level selection
- Timeline configuration (weeks, days/week, hours/day)
- Learning preferences (checkboxes)
- Budget preference
- Loading state during generation
- Error handling

### PathwayPage
- Pathway overview with progress tracking
- Expandable weekly cards
- Learning objectives
- Daily plans
- Curated resources
- Guided projects
- Resume bullet points
- Portfolio checklist
- Recommended certifications

## 🔄 User Flow

1. User lands on **HomePage**
2. Clicks "Generate My Pathway" → navigates to **/generate**
3. Fills out the **PathwayForm**
4. Form submits to backend API
5. Response saved to localStorage
6. User redirected to **/pathway**
7. **PathwayPage** displays the generated roadmap

## 🐛 Troubleshooting

### Cannot connect to backend
- Make sure FastAPI server is running at http://localhost:8000
- Check CORS configuration in backend
- Verify API endpoint URLs in `src/utils/api.js`

### Pathway not displaying
- Check browser console for errors
- Verify localStorage has data: `localStorage.getItem('generatedPathway')`
- Try generating a new pathway

### Styling issues
- Make sure Tailwind CSS is properly configured
- Check `vite.config.js` for Tailwind plugin
- Clear browser cache and restart dev server

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

This creates an optimized build in the `dist/` folder.

### Preview Production Build

```bash
npm run preview
```

## 📦 Dependencies

### Production
- `react` - UI library
- `react-dom` - React DOM renderer
- `react-router-dom` - Routing
- `axios` - HTTP client
- `tailwindcss` - CSS framework
- `@tailwindcss/vite` - Tailwind Vite plugin

### Development
- `vite` - Build tool
- `@vitejs/plugin-react` - React plugin for Vite
- `eslint` - Code linting
- Various ESLint plugins

## 🎯 Next Steps

- [ ] Add progress tracking (mark weeks as completed)
- [ ] Add export functionality (PDF/JSON)
- [ ] Add pathway sharing
- [ ] Connect to MongoDB for persistence
- [ ] Add user authentication
- [ ] Add pathway editing
- [ ] Add multiple pathway support

## 📄 License

Part of the PathPilot AI project for the IBM Bob Hackathon.
