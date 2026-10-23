export default function StudentForm() {
  const inputStyle = { padding: 8, borderRadius: 6, border: "1px solid #bbb" };

  return (
    <>
      <h2 className="section-title">Register</h2>
      <form>
        <label htmlFor="name">Full name</label>
        <br />
        <input id="name" type="text" style={inputStyle} placeholder="e.g. Bilal Ahmed" />
        <br />
        <label>
          <input type="checkbox" defaultChecked /> I agree to the rules
        </label>
        <br />
        <button type="submit" tabIndex={0} disabled={false}>
          Submit
        </button>
      </form>
    </>
  );
}
