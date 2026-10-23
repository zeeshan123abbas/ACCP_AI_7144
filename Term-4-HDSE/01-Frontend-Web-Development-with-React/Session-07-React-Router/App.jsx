import { BrowserRouter, Routes, Route, NavLink, Outlet, Link } from "react-router-dom";
import { Courses, CourseDetail } from "./Courses.jsx";

function Layout() {
  const linkStyle = ({ isActive }) => ({ marginRight: 12, fontWeight: isActive ? "bold" : "normal" });
  return (
    <>
      <nav style={{ padding: 12, background: "#f1f3f5" }}>
        <NavLink to="/" end style={linkStyle}>Home</NavLink>
        <NavLink to="/courses" style={linkStyle}>Courses</NavLink>
        <NavLink to="/about" style={linkStyle}>About</NavLink>
      </nav>
      <main style={{ padding: 16 }}>
        <Outlet />
      </main>
    </>
  );
}

const Home = () => <h1>Welcome to the Term 4 portal</h1>;
const About = () => <p>Built with React Router.</p>;
const NotFound = () => (
  <>
    <h1>404 - Page not found</h1>
    <Link to="/">Go home</Link>
  </>
);

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/courses/:id" element={<CourseDetail />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
