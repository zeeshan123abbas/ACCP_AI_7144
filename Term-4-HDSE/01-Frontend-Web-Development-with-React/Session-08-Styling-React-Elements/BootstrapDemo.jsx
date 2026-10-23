// npm install bootstrap   then add once in main.jsx:
// import "bootstrap/dist/css/bootstrap.min.css";

export default function BootstrapDemo() {
  return (
    <div className="container py-4">
      <div className="row g-3">
        {["Azure", "React", "Node.js"].map((m) => (
          <div className="col-12 col-md-4" key={m}>
            <div className="card h-100 shadow-sm">
              <div className="card-body">
                <h5 className="card-title">{m}</h5>
                <button className="btn btn-primary btn-sm">Open</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
