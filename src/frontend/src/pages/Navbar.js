import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <a className="navbar-brand" href="/">LifeMaxx</a>
      <div className="navbar-nav">
        <a className="nav-link" href="/Dashboard">Dashboard</a>
        <a className="nav-link" href="/Update">Update</a>
        <a className="nav-link" href="/Stats">Stats</a>
      </div>
    </nav>
  );
}

export default Navbar;